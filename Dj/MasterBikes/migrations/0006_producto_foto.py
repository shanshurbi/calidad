# Generated by Django 5.0.6 on 2024-06-24 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterBikes', '0005_estado_tipoproducto_alter_usuario_nickname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='foto',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
