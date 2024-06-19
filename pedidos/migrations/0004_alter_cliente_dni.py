# Generated by Django 5.0.4 on 2024-06-13 02:53

import pedidos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0003_alter_cliente_dni'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='dni',
            field=models.CharField(max_length=8, null=True, unique=True, validators=[pedidos.validators.validar_dni], verbose_name='DNI'),
        ),
    ]