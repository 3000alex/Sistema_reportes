# Generated by Django 3.0.3 on 2020-03-03 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigadores', '0008_auto_20200227_1820'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo14',
            name='conferenciaProyecto',
            field=models.CharField(blank=True, max_length=500, verbose_name='Conferencia o proyecto'),
        ),
        migrations.AddField(
            model_name='modelo14',
            name='fecha',
            field=models.CharField(blank=True, max_length=200, verbose_name='fecha'),
        ),
        migrations.AddField(
            model_name='modelo14',
            name='rol',
            field=models.CharField(blank=True, max_length=500, verbose_name='rol'),
        ),
    ]