from django.contrib import admin
from productos.models import Categoria, Marca, Producto, ImagenProducto, Color, Medida, Presentacion
from django.contrib import messages
from django.utils.html import format_html
# Register your models here.


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'active', 'descripcion']
    search_fields = ['nombre']
    list_filter = ['active']


admin.site.register(Categoria, CategoriaAdmin)


admin.site.register(Marca)


class ImagenProductoInline(admin.TabularInline):
    model = ImagenProducto


class PresentacionInline(admin.TabularInline):
    model = Presentacion


class ProductoAdmin(admin.ModelAdmin):
    # las columnas del listado
    list_display = ['titulo', 'codigo', 'activo', 'slug', 'categoria', 'marca', 'colorear_precio']
    # agregar caja de texto de búsqueda
    search_fields = ['titulo', 'codigo', 'categoria__nombre', 'marca__nombre']
    # filtrar por datos
    list_filter = ['categoria', 'marca']
    # inlines
    inlines = [ImagenProductoInline, PresentacionInline]
    # acciones
    actions = ["activar_productos", "inactivar_productos"]
    # list_per_page = 2 # registros por página

    def colorear_precio(self, obj):
        color = ''
        if obj.precio >= 1000:
            color = 'green'
        else:
            color = 'red'

        return  format_html('<strong style="color: {}">{}</strong>', color, obj.precio)
    
    colorear_precio.short_description = 'Precio personalizado'

    @admin.action(description="Activar productos seleccionados")
    def activar_productos(self, request, queryset):
        queryset.update(activo=True) # se estaría actualizando en la base de datos

        self.message_user(
            request,
            "Se activar los productos seleccionados",
            messages.SUCCESS
        )

    @admin.action(description="Inactivar productos seleccionados")
    def inactivar_productos(self, request, queryset):
        queryset.update(activo=False) # se estaría actualizando en la base de datos

        self.message_user(
            request,
            "Se inactivaron los productos seleccionados",
            messages.SUCCESS
        )
       


admin.site.register(Producto, ProductoAdmin)


admin.site.register(Medida)
admin.site.register(Color)
admin.site.register(Presentacion)


class ImagenProductoAdmin(admin.ModelAdmin):
    list_display = ['producto', 'orden', 'imagen']


admin.site.register(ImagenProducto, ImagenProductoAdmin)
