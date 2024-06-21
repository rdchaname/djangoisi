from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from online.forms import RegistrarseForm, IniciarSesionForm, ConfirmarPedidoForm
from django.contrib.auth.models import User
from pedidos.models import Cliente, Pedido, DetallePedido
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from productos.models import Producto, ImagenProducto, Presentacion
from django.core.exceptions import ObjectDoesNotExist

def portada(request):
    # consulta la lista de productos
    # MODELO
    # select id, titulo, precio from productos where activo = 1 and precio NOT IN (0.00) order by titulo DESC, precio ASC
    productos = Producto.objects.filter(activo=True) \
                        .exclude(precio=0.00) \
                        .order_by('-titulo', 'precio') 
    # print(productos)
    return render(request, "online/portada.html", {"productos": productos})


def detalle_producto(request, slug_producto):
    try:
        # monitor-gamerklasjkldajkldalkda
        producto = Producto.objects.get(slug=slug_producto)
        imagenes = ImagenProducto.objects.filter(producto=producto)
        # select  distinct * from medidas
        medidas = producto.medidas.distinct()
        colores = producto.colores.distinct()
        return render(request, "online/detalle_producto.html", {"producto": producto, "imagenes": imagenes, "medidas": medidas, "colores": colores})    
    except ObjectDoesNotExist as error:
        return render(request, "online/404.html")
    

def registrarse(request):
    return render(request, "online/registrarse.html")


def iniciar_sesion(request):
    return render(request, "online/iniciar_sesion.html")


def registro(request):
    if request.method == 'POST':
        # relacionar los datos que llegan del formulario HTML con un form de DJANGO
        formulario = RegistrarseForm(request.POST)
        
        if formulario.is_valid():
            nombres = formulario.cleaned_data["nombres"]
            apellido_paterno = formulario.cleaned_data["apellido_paterno"]
            apellido_materno = formulario.cleaned_data["apellido_materno"]
            email = formulario.cleaned_data["email"]
            password = formulario.cleaned_data["password"]
            
            # crear el usuario
            usuario = User.objects.create_user(
                username=email,
                first_name=nombres,
                last_name=apellido_paterno + " " + apellido_materno,
                email=email,
                password=password,
            )
            
            # crear al cliente y relacionarlo con el usuario
            cliente = Cliente()  
            cliente.nombres = nombres
            cliente.apellido_paterno = apellido_paterno
            cliente.apellido_materno = apellido_materno
            cliente.email = email
            cliente.usuario = usuario
            cliente.save()
            
            url = reverse('iniciar_sesion')
            return HttpResponseRedirect(url)
        else:
            return render(request, "online/registrarse.html", {"formulario": formulario})
            # url = reverse("registrarse")
            # return HttpResponseRedirect(url)
    else:
        url = reverse("registrarse")
        return HttpResponseRedirect(url)
    
    
    
def ingresar(request):
    if request.method == 'POST':
        formulario = IniciarSesionForm(request.POST)
        if formulario.is_valid():
            email = formulario.cleaned_data["email"]
            password = formulario.cleaned_data["password"]
            usuario_logeado = authenticate(username=email, password=password)
            login(request, usuario_logeado) # esta linea inicia sesión            
            
            url = reverse("mi_cuenta")
            data = {
                "url" : url,
                "mensaje": "Inicio de sesión correcto"
            }
            return JsonResponse(data, status=200)
        else:
            data = {}
            lista_errores = {}
            print(formulario.errors.items())
            for campo, errores in formulario.errors.items():
                print(campo)
                campo_errores = []
                for error in errores:
                    campo_errores.append(error)
                    
                lista_errores[campo] = campo_errores
            
            data["errores"] = lista_errores
            data["mensaje"] = "Eror en los datos enviados"
            
            print(data)
            
            # entidad improcesable 422
            return JsonResponse(data, status=422)
    else:
        url = reverse("iniciar_sesion")
        return HttpResponseRedirect(url)
    
    
def cerrar_sesion(request):
    logout(request)
    url = reverse("iniciar_sesion")
    return HttpResponseRedirect(url)


@login_required(login_url="/iniciar_sesion")
def mi_cuenta(request):
    return render(request, "online/mi_cuenta.html")




def agregar_item(request):
    if request.method == 'POST':
        producto_id = int(request.POST.get("producto_id"))
        color_id = int(request.POST.get("color_id"))
        medida_id = int(request.POST.get("medida_id"))
        cantidad = int(request.POST.get("cantidad"))
        
        try:
            # 01 verificar si presentación existe
            presentacion = Presentacion.objects.get(producto_id=producto_id, color_id=color_id, medida_id=medida_id)
            
            """
            [
                item1, item2, item3......
            ]
            4
            {
                "presentacion_id": 1
                "cantidad": 2
                "precio"
                "subtotal"
                "titulo"
                "imagen"
            }
            {
                "presentacion_id": 1
                "cantidad": 3
                "precio"
                "subtotal"
                "titulo"
                "imagen"
            }
            """
            
            carrito = request.session.get("carrito_pedido", [])
            
            precio = float(presentacion.producto.precio)
            subtotal = precio * float(cantidad)
            titulo_producto = presentacion.__str__()
            imagen = ImagenProducto.objects.filter(producto_id=presentacion.producto.id).order_by('orden')[0].imagen.url
            
            elemento_nuevo = True
            posicion_existente = 0
            
            for indice, item in enumerate(carrito):
                if item["presentacion_id"] == presentacion.id:
                    elemento_nuevo = False
                    posicion_existente = indice
                    cantidad = cantidad + item["cantidad"]
            
            
             # 02 verificar stock disponible
            if presentacion.stock < cantidad:
                respuesta = {"mensaje": "Stock no disponible"}
                return JsonResponse(respuesta, status=409)
            
            if elemento_nuevo:
                item = {
                    "presentacion_id": presentacion.id,
                    "cantidad": cantidad,
                    "precio": precio,
                    "subtotal": subtotal,
                    "titulo": titulo_producto,
                    "imagen": imagen
                }
                carrito.append(item)
            else:
                carrito[posicion_existente] = {
                    "presentacion_id": presentacion.id,
                    "cantidad": cantidad,
                    "precio": precio,
                    "subtotal": subtotal,
                    "titulo": titulo_producto,
                    "imagen": imagen
                }
                
            # actualizar la variabla de session
            request.session["carrito_pedido"] = carrito
            
            respuesta = {"mensaje": "Item agregado correctamente"}
            return JsonResponse(respuesta)
        
        except ObjectDoesNotExist as error:
            respuesta = {"mensaje": "Presentación de producto no existe"}
            return JsonResponse(respuesta, status=404)
    else:
        pass
    


def carrito(request):
    return render(request, "online/carrito.html")



def quitar_item(request):
    if request.method == 'POST':
        indice = int(request.POST.get("indice"))
        
        try:
            carrito = request.session.get("carrito_pedido",[])
            
            del carrito[indice]
            
            request.session["carrito_pedido"] = carrito
            
            respuesta = {"mensaje": "Item eliminado correctamente"}
            return JsonResponse(respuesta)
        
        except Exception as error:
            respuesta = {"mensaje": "Error al intentar quitar item"}
            return JsonResponse(respuesta, status=500)
        
    else:
        pass

 
@login_required(login_url="/iniciar_sesion")
def confirmar_pedido(request):
    usuario_logeado = request.user # datos de la tabla auth_user
    cliente = Cliente.objects.get(usuario=usuario_logeado)
    return render(request, "online/confirmar_pedido.html", {"usuario_logeado":usuario_logeado, "cliente": cliente})


@login_required(login_url="/iniciar_sesion")
def guardar_pedido(request):
    if request.method == 'POST':
        formulario = ConfirmarPedidoForm(request.POST)
        if formulario.is_valid():
            # 01 Verificar
            carrito = request.session.get("carrito_pedido", [])
            
            for item in carrito:
                presentacion_id = item["presentacion_id"]
                cantidad = item["cantidad"]
                titulo = item["titulo"]
                presentacion = Presentacion.objects.get(id=presentacion_id)
                if presentacion.stock < cantidad:
                    mensaje = "El producto %s no tiene stock disponible, revisar carrito" % (titulo)
                    data = {"mensaje": mensaje}
                    return JsonResponse(data, status=409) # conflicto
                
            # 2 actualizar los datos del cliente
            usuario = request.user
            cliente = Cliente.objects.get(usuario=usuario)
            cliente.nombres = formulario.cleaned_data["nombres"]
            cliente.apellido_paterno = formulario.cleaned_data["apellido_paterno"]
            cliente.apellido_materno = formulario.cleaned_data["apellido_materno"]
            cliente.email = formulario.cleaned_data["email"]
            cliente.dni = formulario.cleaned_data["dni"]
            cliente.celular = formulario.cleaned_data["celular"]
            cliente.telefono_fijo = formulario.cleaned_data["telefono_fijo"]
            cliente.direccion = formulario.cleaned_data["direccion"]
            cliente.fecha_nacimiento = formulario.cleaned_data["fecha_nacimiento"]
            cliente.save()
            
            # 3 actualizar los datos del usuario
            usuario.first_name = formulario.cleaned_data["nombres"]
            usuario.last_name = formulario.cleaned_data["apellido_paterno"] + " " + formulario.cleaned_data["apellido_materno"]
            usuario.email = formulario.cleaned_data["email"]
            usuario.save()
            
            total = 0.00
            for item in carrito:
                total = total + float(item["subtotal"])
                
            # 4 registrar pedido
            pedido = Pedido()
            pedido.total = total
            pedido.cliente = cliente
            pedido.numero = "000000001" # ???
            pedido.observacion = request.POST.get("observacion", "")
            pedido.save()
            
            # 5 registrar detalle del pedido
            for item in carrito:
                detalle_pedido = DetallePedido()
                detalle_pedido.precio_unitario = item["precio"]
                detalle_pedido.cantidad = item["cantidad"]
                detalle_pedido.presentacion_id = item["presentacion_id"]
                detalle_pedido.pedido = pedido
                detalle_pedido.save()
            
            # 6 limpiar variables de session
            request.session["carrito_pedido"] = []
            
            url = reverse("mi_cuenta")
            data = {
                "mensaje": "Pedido registrado correctamente",
                "url": url
            }
            return JsonResponse(data)
        else:
            data = {}
            lista_errores = {}
            print(formulario.errors.items())
            for campo, errores in formulario.errors.items():
                print(campo)
                campo_errores = []
                for error in errores:
                    campo_errores.append(error)
                    
                lista_errores[campo] = campo_errores
            
            data["errores"] = lista_errores
            data["mensaje"] = "Eror en los datos enviados"
            
            print(data)
            
            # entidad improcesable 422
            return JsonResponse(data, status=422)
    else:
        pass
