# Generated by Django 5.0.6 on 2024-06-26 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterBikes', '0013_alter_reparacion_problema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despacho',
            name='pedido',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
