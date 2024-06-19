from django.core.exceptions import ValidationError


def validar_dni(value):
    if value is not None and value != '':
        if len(value) != 8:
            raise ValidationError("El DNI debe tener 8 caracteres")
