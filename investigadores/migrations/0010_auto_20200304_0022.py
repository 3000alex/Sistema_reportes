# Generated by Django 3.0.3 on 2020-03-04 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('investigadores', '0009_auto_20200302_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='modelo16',
            name='coordinacion',
            field=models.CharField(blank=True, max_length=500, verbose_name='Coordinacion'),
        ),
        migrations.AddField(
            model_name='modelo16',
            name='grado',
            field=models.CharField(blank=True, max_length=500, verbose_name='Grado'),
        ),
    ]