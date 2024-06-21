from django.db import models
from django.contrib.auth.models import User
from pedidos.validators import validar_dni
from django.utils import timezone
from productos.models import Presentacion


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombres = models.CharField(max_length=100, verbose_name='Nombres')
    apellido_paterno = models.CharField(
        max_length=70, verbose_name='Apellido paterno')
    apellido_materno = models.CharField(
        max_length=70, verbose_name='Apellido materno')
    email = models.EmailField(max_length=60, verbose_name='Correo electrónico')
    dni = models.CharField(max_length=8, verbose_name='DNI',
                           unique=True, validators=[validar_dni], null=True)
    celular = models.CharField(
        max_length=30, verbose_name='Celular', null=True, blank=True)
    telefono_fijo = models.CharField(
        max_length=30, verbose_name='Teléfono fijo', null=True, blank=True)
    direccion = models.CharField(
        max_length=200, verbose_name='Dirección', null=True, blank=True)
    fecha_nacimiento = models.DateField(
        verbose_name='Fecha de nacimiento', null=True, blank=True)
    usuario = models.OneToOneField(
        User, on_delete=models.RESTRICT, verbose_name="Usuario")

    def __str__(self):
        return self.apellido_paterno + ' ' + self.apellido_materno + ' ' + self.nombres

    class Meta:
        db_table = 'cliente'
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class Pedido(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(verbose_name="Fecha", default=timezone.now)
    # 000000001, 0000000002
    numero = models.CharField(verbose_name="Número", max_length=10)
    total = models.DecimalField(verbose_name="Total", max_digits=9, decimal_places=2)
    cliente = models.ForeignKey(Cliente, on_delete=models.RESTRICT)
    observacion = models.TextField(verbose_name="Observación", null=True)
    
    
    def __str__(self):
        return  self.numero
    
    
    class Meta:
        db_table = 'pedido'
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        
        
        
class DetallePedido(models.Model):
    id = models.AutoField(primary_key=True)
    precio_unitario = models.DecimalField(verbose_name="Precio unitario", max_digits=9, decimal_places=2)
    cantidad = models.PositiveSmallIntegerField(verbose_name="Cantidad")
    presentacion = models.ForeignKey(Presentacion, on_delete=models.RESTRICT)
    pedido = models.ForeignKey(Pedido, on_delete=models.RESTRICT)
    
    
    def __str__(self):
        return  self.pedido.numero
    
    
    class Meta:
        db_table = 'detalle_pedido'
        verbose_name = 'Detalle de pedido'
        verbose_name_plural = 'Detalles de pedidos'