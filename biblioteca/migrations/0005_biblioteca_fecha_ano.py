# Generated by Django 3.0.2 on 2020-02-08 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0004_auto_20200207_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='biblioteca',
            name='fecha_ano',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Fecha'),
        ),
    ]
