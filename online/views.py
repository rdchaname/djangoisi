from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from online.forms import RegistrarseForm
from django.contrib.auth.models import User
from pedidos.models import Cliente

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
            url = reverse("registrarse")
            return HttpResponseRedirect(url)
    else:
        url = reverse("registrarse")
        return HttpResponseRedirect(url)