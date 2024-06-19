from django.db import models
from autoslug import AutoSlugField
from bitacora.models import Bitacora

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=70)
    active = models.BooleanField(default=True)
    descripcion = models.CharField(max_length=300, default='')

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'categoria'
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'


class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    def delete(self):
        # personalizar
        return super().delete()

    # sobre escribiendo el método SAVE de DJANGO
    # nuevo/actualizando
    def save(self):
        if self.id is None:
            # nuevo
            bitacora = Bitacora()
            bitacora.accion = 'nuevo'
            bitacora.modelo = 'Marca'
            bitacora.descripcion = 'nombre:' + self.nombre 
            bitacora.usuario = "admin"
            bitacora.save()
        else:
            # actualizando
            bitacora = Bitacora()
            bitacora.accion = 'actualizar'
            bitacora.modelo = 'Marca'
            bitacora.descripcion = 'nombre:' + self.nombre 
            bitacora.usuario = "admin"
            bitacora.save()

        # esta linea es la que realiza la accion en el modelo
        return super().save()

    class Meta:
        db_table = 'marca'
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'


class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=200, verbose_name='Título')
    precio = models.DecimalField(max_digits=9, decimal_places=2)
    categoria = models.ForeignKey(
        Categoria, on_delete=models.RESTRICT, verbose_name='Categoría')  # categoria_id
    marca = models.ForeignKey(Marca, on_delete=models.RESTRICT)  # marca_id
    descripcion = models.TextField()
    activo = models.BooleanField(default=True, verbose_name='¿Está activo?')
    slug = AutoSlugField(populate_from='titulo',
                         always_update=True, unique=True)
    codigo = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.titulo

    # sobre escribiendo el método SAVE de DJANGO
    # nuevo/actualizando
    def save(self):
        if self.id is None:
            # nuevo
            bitacora = Bitacora()
            bitacora.accion = 'nuevo'
            bitacora.modelo = 'Producto'
            bitacora.descripcion = 'titulo:' + self.titulo + ',precio:' + str(self.precio)
            bitacora.usuario = "admin"
            bitacora.save()
        else:
            # actualizando
            bitacora = Bitacora()
            bitacora.accion = 'actualizar'
            bitacora.modelo = 'Producto'
            bitacora.descripcion = 'titulo:' + self.titulo + ',precio:' + str(self.precio)
            bitacora.usuario = "admin"
            bitacora.save()

        # esta linea es la que realiza la accion en el modelo
        return super().save()

    class Meta:
        db_table = 'producto'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'


class ImagenProducto(models.Model):
    id = models.AutoField(primary_key=True)
    imagen = models.ImageField(upload_to='productos')
    orden = models.PositiveSmallIntegerField()
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)

    def __str__(self):
        return self.producto.titulo + " Imagen " + str(self.orden)

    class Meta:
        db_table = 'imagen_producto'
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imágenes'


class Medida(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'medida'
        verbose_name = 'Medida'
        verbose_name_plural = 'Medidas'


class Color(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'color'
        verbose_name = 'Color'
        verbose_name_plural = 'Colores'


class Presentacion(models.Model):
    id = models.AutoField(primary_key=True)
    medida = models.ForeignKey(Medida, on_delete=models.RESTRICT)
    color = models.ForeignKey(Color, on_delete=models.RESTRICT)
    producto = models.ForeignKey(Producto, on_delete=models.RESTRICT)
    stock = models.PositiveIntegerField()

    def __str__(self):
        return self.producto.titulo + "(" + self.medida.nombre + " - " + self.color.nombre + ")"

    class Meta:
        db_table = 'presentacion'
        verbose_name = 'Presentación'
        verbose_name_plural = 'Presentaciones'
