from django import forms
from django.contrib.auth.models import User
from pedidos.models import Cliente
from django.contrib.auth import authenticate

class RegistrarseForm(forms.Form):
    nombres = forms.CharField(max_length=100, required=True)
    apellido_paterno = forms.CharField(max_length=70, required=True)
    apellido_materno = forms.CharField(max_length=70, required=True)
    email = forms.EmailField(max_length=60, required=True)
    password = forms.CharField(max_length=128, required=True)
    confirmar_password = forms.CharField(max_length=128, required=True)
    
    def clean(self):
        data = super().clean()
        password = data.get("password")
        confirmar_password = data.get("confirmar_password")
        email = data.get("email")
        
        # 01: que el campo "password" y "confirmar_password" sean iguales
        if password != confirmar_password:
            self.add_error("password", "Las contraseñas no coinciden")
            self.add_error("confirmar_password", "Las contraseñas no coinciden")
        
        # 02: que no exista otro usuario con el mismo "email"
        coincidencias = User.objects.filter(username=email).count()
        clientes = Cliente.objects.filter(email=email).count()
        
        if (coincidencias > 0 or clientes > 0):
            self.add_error("email", "Correo electrónico ya se encuentra en uso")
            
            
class IniciarSesionForm(forms.Form):
    email = forms.EmailField(max_length=60, required=True)
    password = forms.CharField(max_length=128, required=True)

    
    def clean(self):
        data = super().clean()
        email = data.get("email")
        password = data.get("password")
        
        # validar que los datos de inicio de sesión sean válidos
        usuario_valido = authenticate(username=email, password=password)
        
        if usuario_valido is None:
            self.add_error('email', 'Datos de inicio de sesión son incorrectos')
            
            
            
class ConfirmarPedidoForm(forms.Form):
    nombres = forms.CharField(max_length=100, required=True)
    apellido_paterno = forms.CharField(max_length=70, required=True)
    apellido_materno = forms.CharField(max_length=70, required=True)
    email = forms.EmailField(max_length=60, required=True)
    dni = forms.CharField(max_length=8, required=True, )
    celular = forms.CharField(max_length=30, required=True, )
    telefono_fijo = forms.CharField(max_length=30,required=True, )
    direccion = forms.CharField(max_length=200, required=True,)
    fecha_nacimiento = forms.DateField( required=True)
    
    def clean(self):
        data = super().clean()
        dni = data.get("dni")
        
        # validar que los datos de inicio de sesión sean válidos
        cantidad = Cliente.objects.filter(dni=dni).count() # ????
        
        if cantidad > 0:
            self.add_error('dni', 'DNI ya esta siendo usado por otro cliente')