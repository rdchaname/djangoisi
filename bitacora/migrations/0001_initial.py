# Generated by Django 5.0.4 on 2024-05-30 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bitacora',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('accion', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
                ('modelo', models.CharField(max_length=30)),
                ('fecha', models.DateField()),
                ('usuario', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Bitacora',
                'verbose_name_plural': 'Bitacora',
                'db_table': 'bitacora',
            },
        ),
    ]
