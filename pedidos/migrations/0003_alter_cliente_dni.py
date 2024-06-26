# Generated by Django 5.0.4 on 2024-05-30 02:38

import pedidos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0002_alter_cliente_celular_alter_cliente_direccion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(max_length=8, unique=True, validators=[pedidos.validators.validar_dni], verbose_name='DNI'),
        ),
    ]
