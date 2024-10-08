# Generated by Django 5.0.6 on 2024-06-27 17:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MasterBikes', '0017_remove_arriendo_id_forma_pago_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='FormaPago',
            fields=[
                ('id_forma_pago', models.AutoField(db_column='idFormaPago', primary_key=True, serialize=False)),
                ('forma', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'Formas de pago',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id_producto', models.AutoField(db_column='idProducto', primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(blank=True, max_length=30, null=True)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('foto', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Talla',
            fields=[
                ('id_talla', models.AutoField(db_column='idTalla', primary_key=True, serialize=False)),
                ('talla', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TipoBici',
            fields=[
                ('id_tipo_bici', models.AutoField(db_column='idTipoBici', primary_key=True, serialize=False)),
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
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id_tipo_usuario', models.AutoField(db_column='idTipoUsuario', primary_key=True, serialize=False)),
                ('tipo', models.CharField(db_column='Tipo de Usuario', max_length=30)),
                ('descripcion', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(db_column='idPago', primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('domicilio', models.BooleanField()),
                ('id_forma_pago', models.ForeignKey(db_column='idFormaPago', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.formapago')),
            ],
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id_despacho', models.AutoField(db_column='idDespacho', primary_key=True, serialize=False)),
                ('pedido', models.DateTimeField(blank=True, null=True)),
                ('envio', models.DateTimeField(blank=True, null=True)),
                ('recibo', models.DateTimeField(blank=True, null=True)),
                ('id_pago', models.ForeignKey(db_column='idPago', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.pago')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_detalle', models.AutoField(db_column='idDetalle', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('id_pago', models.ForeignKey(db_column='idPago', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.pago')),
                ('id_producto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.producto')),
            ],
        ),
        migrations.AddField(
            model_name='producto',
            name='id_tipo_producto',
            field=models.ForeignKey(db_column='idTipoProducto', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.tipoproducto'),
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rut', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('id_tipo_usuario', models.ForeignKey(db_column='idTipoUsuario', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.tipousuario')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reparacion',
            fields=[
                ('id_reparacion', models.AutoField(db_column='idReparacion', primary_key=True, serialize=False)),
                ('modelo_bicicleta', models.CharField(max_length=80)),
                ('problema', models.CharField(blank=True, max_length=150, null=True)),
                ('fecha', models.DateTimeField()),
                ('id_estado', models.ForeignKey(db_column='idEstado', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.estado')),
                ('rut', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.usuario')),
            ],
            options={
                'verbose_name_plural': 'Reparaciones',
            },
        ),
        migrations.AddField(
            model_name='pago',
            name='rut',
            field=models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.usuario'),
        ),
        migrations.CreateModel(
            name='Arriendo',
            fields=[
                ('id_arriendo', models.AutoField(db_column='idArriendo', primary_key=True, serialize=False)),
                ('direccion', models.CharField(max_length=80)),
                ('inicio', models.DateField()),
                ('termino', models.DateField()),
                ('id_forma_pago', models.ForeignKey(db_column='idFormaPago', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.formapago')),
                ('id_talla', models.ForeignKey(db_column='idTalla', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.talla')),
                ('id_tipo_bici', models.ForeignKey(db_column='idTipoBici', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.tipobici')),
                ('rut', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.usuario')),
            ],
        ),
    ]
