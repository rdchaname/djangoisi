# Generated by Django 5.0.4 on 2024-06-21 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0011_alter_categoria_options_alter_color_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='colores',
            field=models.ManyToManyField(through='productos.Presentacion', to='productos.color'),
        ),
        migrations.AddField(
            model_name='producto',
            name='medidas',
            field=models.ManyToManyField(through='productos.Presentacion', to='productos.medida'),
        ),
    ]