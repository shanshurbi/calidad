# Generated by Django 5.0.6 on 2024-06-24 21:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterBikes', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id_estado', models.AutoField(db_column='idEstado', primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id_tipo_producto', models.AutoField(db_column='idTipoProducto', primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nickname',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id_reparacion', models.AutoField(db_column='idReparacion', primary_key=True, serialize=False)),
                ('modelo_bicicleta', models.CharField(max_length=80)),
                ('problema', models.CharField(max_length=150)),
                ('fecha', models.DateTimeField()),
                ('id_estado', models.ForeignKey(db_column='idEstado', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.estado')),
                ('rut', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(blank=True, max_length=30, null=True)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('id_tipo_producto', models.ForeignKey(db_column='idTipoProducto', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.tipoproducto')),
            ],
        ),
    ]
