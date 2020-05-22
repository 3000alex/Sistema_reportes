# Generated by Django 3.0.5 on 2020-05-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Biblioteca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fecha')),
                ('fecha_ano', models.CharField(blank=True, max_length=50, null=True, verbose_name='Fecha')),
                ('doi', models.CharField(blank=True, max_length=100, null=True, verbose_name='doi')),
                ('bibcode', models.CharField(blank=True, max_length=80, null=True, unique=True, verbose_name='bibcode')),
                ('titulo', models.TextField(blank=True, max_length=15000, null=True, verbose_name='titulo')),
                ('autores', models.TextField(blank=True, max_length=15000, null=True, verbose_name='autores')),
                ('estudiantes_en_articulo', models.CharField(blank=True, max_length=150, null=True, verbose_name='Estudiantes en el articulo')),
                ('revista_publicacion', models.CharField(blank=True, max_length=150, null=True)),
                ('paginas', models.CharField(blank=True, max_length=150, null=True)),
                ('volumen', models.CharField(blank=True, max_length=150, null=True)),
                ('url', models.CharField(blank=True, max_length=550, null=True)),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
            ],
            options={
                'verbose_name': 'biblioteca',
                'verbose_name_plural': 'bibliotecas',
                'ordering': ['-fecha'],
            },
        ),
    ]