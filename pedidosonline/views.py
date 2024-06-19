from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from productos.models import Producto
from django.core import serializers

# ACCIONES


def portada(request):
    return HttpResponse("Página de portada")


def saludo(request):
    return HttpResponse("Bienvenido a mi web")


def listado_usuarios(request):
    nombre = request.GET.get("nombre")
    tipo = request.GET.get("tipo")
    if nombre is None:
        return HttpResponse("No se esta enviando valor para el nombre", status=400)

    print(nombre)
    descripcion = "Buscar los clientes con el nombre " + nombre
    return HttpResponse(descripcion)


def editar_usuario(request, id, nombre):
    return HttpResponse("Editando usuario con id " + str(id))


def login(request):
    # consulta a la BD
    nombre_proyecto = "ISI Python"
    titulo_formulario = "Iniciar sesión"
    return render(request, "login.html", {
        "nombreProyecto": nombre_proyecto,
        "tituloFormulario": titulo_formulario,
        "saludo": "Buenas noches",
        "enlaces": ["Enlace 1", "Enlace 2", "Enlace 3"]
    })


def lista_productos(request):
    # select * from productos
    # queryset
    productos = Producto.objects.all() # ORM

    # serializacion
    qs_json = serializers.serialize('json', productos)
    # return JsonResponse(qs_json)
    return HttpResponse(qs_json, content_type='application/json')
