# Generated by Django 3.0.5 on 2020-07-13 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['apellido'], 'verbose_name': 'Investigador', 'verbose_name_plural': 'Investigadores'},
        ),
    ]
