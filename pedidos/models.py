from django.db import models
from django.contrib.auth.models import User
from pedidos.validators import validar_dni


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
