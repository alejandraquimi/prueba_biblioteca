# Generated by Django 4.2.7 on 2023-11-16 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_rename_auto_libro_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='confirmado',
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name='prestamo',
            name='reservado',
            field=models.BooleanField(null=True),
        ),
    ]
