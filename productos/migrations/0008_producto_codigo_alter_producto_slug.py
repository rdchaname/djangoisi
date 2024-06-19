# Generated by Django 5.0.4 on 2024-05-23 00:56

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0007_producto_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='codigo',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='producto',
            name='slug',
            field=autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='titulo', unique=True),
        ),
    ]