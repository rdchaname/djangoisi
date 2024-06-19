from django import forms

class RegistrarseForm(forms.Form):
    nombres = forms.CharField(max_length=100, required=True)
    apellido_paterno = forms.CharField(max_length=70, required=True)
    apellido_materno = forms.CharField(max_length=70, required=True)
    email = forms.EmailField(max_length=60, required=True)
    password = forms.CharField(max_length=128, required=True)
    confirmar_password = forms.CharField(max_length=128, required=True)
    
    # que el campo "password" y "confirmar_password" sean iguales
    # que no exista otro usuario con el mismo "email"
    