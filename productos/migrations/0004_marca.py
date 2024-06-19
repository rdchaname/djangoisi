# Generated by Django 5.0.4 on 2024-05-16 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_rename_activo_categoria_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'marca',
            },
        ),
    ]