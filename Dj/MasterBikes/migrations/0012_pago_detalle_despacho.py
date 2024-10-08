# Generated by Django 5.0.6 on 2024-06-26 01:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterBikes', '0011_remove_detalle_id_pago_remove_detalle_id_producto_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id_pago', models.AutoField(db_column='idPago', primary_key=True, serialize=False)),
                ('total', models.IntegerField()),
                ('domicilio', models.BooleanField()),
                ('id_forma_pago', models.ForeignKey(db_column='idFormaPago', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.formapago')),
                ('rut', models.ForeignKey(db_column='rut', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Detalle',
            fields=[
                ('id_detalle', models.AutoField(db_column='idDetalle', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('subtotal', models.IntegerField()),
                ('id_producto', models.ForeignKey(db_column='idProducto', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.producto')),
                ('id_pago', models.ForeignKey(db_column='idPago', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.pago')),
            ],
        ),
        migrations.CreateModel(
            name='Despacho',
            fields=[
                ('id_despacho', models.AutoField(db_column='idDespacho', primary_key=True, serialize=False)),
                ('pedido', models.DateTimeField()),
                ('envio', models.DateTimeField()),
                ('recibo', models.DateTimeField()),
                ('id_pago', models.ForeignKey(db_column='idPago', on_delete=django.db.models.deletion.CASCADE, to='MasterBikes.pago')),
            ],
        ),
    ]
