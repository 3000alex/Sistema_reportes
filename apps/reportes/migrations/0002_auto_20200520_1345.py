# Generated by Django 3.0.5 on 2020-05-20 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reportes', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='modelo3',
            old_name='nombre_de_conferancia',
            new_name='nombre_de_conferencia',
        ),
    ]
