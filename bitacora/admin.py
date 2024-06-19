from django.contrib import admin
from bitacora.models import Bitacora

# Register your models here.
class BitacoraAdmin(admin.ModelAdmin):
    list_display = ['modelo', 'accion', 'descripcion', 'fecha', 'usuario']

admin.site.register(Bitacora, BitacoraAdmin)
