from django.db import models


class Bitacora(models.Model):
    id = models.AutoField(primary_key=True)
    accion = models.CharField(max_length=50)
    descripcion = models.TextField()
    modelo = models.CharField(max_length=30)
    fecha = models.DateTimeField(auto_now_add=True)
    usuario = models.CharField(max_length=100)

    def __str__(self):
        return self.accion + ' - ' + self.modelo
    

    class Meta:
        db_table = 'bitacora'
        verbose_name = 'Bitacora'
        verbose_name_plural = 'Bitacora'
