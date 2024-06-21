# Generated by Django 5.0.4 on 2024-06-21 02:18

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0004_alter_cliente_dni'),
        ('productos', '0012_producto_colores_producto_medidas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(default=django.utils.timezone.now, verbose_name='Fecha')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('total', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Total')),
                ('observacion', models.TextField(null=True, verbose_name='Observación')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pedidos.cliente')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'db_table': 'pedido',
            },
        ),
        migrations.CreateModel(
            name='DetallePedido',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Precio unitario')),
                ('cantidad', models.PositiveSmallIntegerField(verbose_name='Cantidad')),
                ('presentacion', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='productos.presentacion')),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='pedidos.pedido')),
            ],
            options={
                'verbose_name': 'Detalle de pedido',
                'verbose_name_plural': 'Detalles de pedidos',
                'db_table': 'detalle_pedido',
            },
        ),
    ]
