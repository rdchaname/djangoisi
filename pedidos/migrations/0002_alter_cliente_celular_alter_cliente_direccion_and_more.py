# Generated by Django 5.0.4 on 2024-05-30 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='celular',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Celular'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Dirección'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='fecha_nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='telefono_fijo',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='Teléfono fijo'),
        ),
    ]