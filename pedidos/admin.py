from django.contrib import admin
from pedidos.models import Cliente


class ClienteAdmin(admin.ModelAdmin):
    list_display = ['dni', 'apellido_paterno', 'apellido_materno', 'nombres']
    fieldsets = (
        # datos personales: apellido_paterno, apellido_materno, nombres, dni
        (
            "DATOS PERSONALES",
            {
                "fields": (
                    ("apellido_paterno", "apellido_materno", "nombres"),
                    "dni"
                )
            }
        ),
        # datos de contacto: email, celular, telefono_fijo, direccion
        (
            "DATOS DE CONTACTO",
            {
                "fields": (
                    ("email", "celular", "telefono_fijo"),
                    "direccion"
                )
            }
        ),
        # datos de usuario: usuario
        (
            "DATOS DE USUARIO",
            {
                "fields": ("usuario", )
            }
        ),
        # otros: fecha_nacimiento
        (
            "OTROS DATOS",
            {
                "fields": ("fecha_nacimiento", )
            }
        )
    )


admin.site.register(Cliente, ClienteAdmin)
