# Generated by Django 3.0.5 on 2020-05-20 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombre')),
                ('apellido', models.CharField(blank=True, max_length=50, verbose_name='Apellido')),
                ('nombreCorto', models.CharField(blank=True, max_length=50, verbose_name='Nombre corto')),
                ('correoAlternativo', models.EmailField(blank=True, max_length=50, verbose_name='Correo alternativo')),
                ('categoria', models.CharField(blank=True, choices=[('Investigador posdoctoral', 'Investigador posdoctoral'), ('Cátedra CONACyT', 'Cátedra CONACyT'), ('Investigador Asociado C', 'Investigador Asociado C'), ('Investigador Titular A', 'Investigador Titular A'), ('Investigador Titular B', 'Investigador Titular B'), ('Investigador Titular C', 'Investigador Titular C'), ('Investigador Titular D', 'Investigador Titular D')], default='Sin especificar', max_length=50, verbose_name='Categoria')),
                ('nivelSni', models.CharField(blank=True, choices=[('Candidato', 'Candidato'), ('Nivel 1', 'Nivel 1'), ('Nivel 2', 'Nivel 2'), ('Nivel 3', 'Nivel 3'), ('Emérito', 'Emérito')], default='Sin nombreamiento', max_length=50, verbose_name='Nivel de SNI')),
                ('orcId', models.CharField(blank=True, max_length=50, verbose_name='Orc ID')),
                ('arxivId', models.CharField(blank=True, max_length=50, verbose_name='Arxiv ID')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
