from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from online.forms import RegistrarseForm, IniciarSesionForm
from django.contrib.auth.models import User
from pedidos.models import Cliente
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required

def portada(request):
    return render(request, "online/portada.html")


def detalle_producto(request, slug_producto):
    return render(request, "online/detalle_producto.html")


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


# confirmar_pedido