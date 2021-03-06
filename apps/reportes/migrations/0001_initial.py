# Generated by Django 3.0.5 on 2020-05-27 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Glosario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seccion', models.CharField(choices=[('I. INVESTIGACIÓN CIENTÍFICA', 'I. INVESTIGACIÓN CIENTÍFICA'), ('II. FORMACIÓN DE RECURSOS HUMANOS', 'II. FORMACIÓN DE RECURSOS HUMANOS'), ('III. DESARROLLO TECNOLÓGICO E INNOVACIÓN(agregar patentes en REGISTRO)', 'III. DESARROLLO TECNOLÓGICO E INNOVACIÓN(agregar patentes en REGISTRO)'), ('IV. APOYO INSTITUCIONAL', 'IV. APOYO INSTITUCIONAL'), ('V. INFORMACIÖN ADICIONAL', 'V. INFORMACIÖN ADICIONAL')], max_length=200, verbose_name='Seccion perteneciente')),
                ('numerales', models.TextField(max_length=5000, verbose_name='Nombre del numeral')),
                ('explicacion', models.TextField(max_length=5000, verbose_name='Explicación')),
            ],
            options={
                'verbose_name': 'glosario',
                'verbose_name_plural': 'Glosarios',
                'ordering': ['numerales'],
            },
        ),
        migrations.CreateModel(
            name='Numeral',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=190, verbose_name='Nombre del numeral')),
                ('nombre_seccion', models.CharField(choices=[('Investigacion Cientifica', 'Investigacion Cientifica'), ('Formacion de Recursos Humanos', 'Formacion de Recursos Humanos'), ('Desarrollo Tecnologico e Innovacion', 'Desarrollo Tecnologico e Innovacion'), ('Apoyo Institucional', 'Apoyo Institucional'), ('Informacion Adicional', 'Informacion Adicional')], max_length=150, verbose_name='Nombre de la seccion')),
                ('orden', models.FloatField(verbose_name='Orden')),
            ],
            options={
                'verbose_name': 'Numeral',
                'verbose_name_plural': 'Numerales',
                'ordering': ['orden'],
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_periodo', models.CharField(max_length=150, verbose_name='Nombre del periodo')),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True, verbose_name='Fecha del inicio de periodo')),
            ],
            options={
                'verbose_name': 'Periodo del reporte',
                'verbose_name_plural': 'Periodos de los reportes',
                'ordering': ['fecha_inicio'],
            },
        ),
        migrations.CreateModel(
            name='ReporteEnviado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporte', models.FileField(blank=True, upload_to='reportes/pdfs/', verbose_name='reporte')),
                ('anexo', models.FileField(blank=True, upload_to='reportes/anexos/', verbose_name='anexos')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='fecha')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo', verbose_name='periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Reporte Enviado',
                'verbose_name_plural': 'Reportes Enviados',
                'ordering': ['usuario'],
            },
        ),
        migrations.CreateModel(
            name='Modelo9',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.TextField(blank=True, max_length=15000, verbose_name='titulo')),
                ('autores', models.TextField(blank=True, max_length=15000, verbose_name='autores')),
                ('numero_reportes', models.CharField(blank=True, max_length=500, verbose_name='numero de reportes')),
                ('fecha', models.CharField(blank=True, max_length=500, verbose_name='fecha')),
                ('url', models.CharField(blank=True, max_length=500, verbose_name='url')),
                ('doi', models.CharField(blank=True, max_length=500, verbose_name='doi')),
                ('revista_publicacion', models.CharField(blank=True, max_length=500, verbose_name='revista o publicacion')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 9',
                'verbose_name_plural': 'Campos del Modelo 9',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo8',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=500, verbose_name='nombre')),
                ('descripcion', models.TextField(blank=True, max_length=15000, verbose_name='descripcion')),
                ('participantes', models.TextField(blank=True, max_length=500, verbose_name='participantes')),
                ('financiamiento', models.CharField(blank=True, max_length=500, verbose_name='financiamiento')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 8',
                'verbose_name_plural': 'Campos del Modelo 8',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo7',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autores', models.TextField(blank=True, max_length=15000, verbose_name='autores')),
                ('descripcion', models.TextField(blank=True, max_length=15000, verbose_name='descripcion')),
                ('url', models.CharField(blank=True, max_length=500, verbose_name='url')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 7',
                'verbose_name_plural': 'Campos del Modelo 7',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo6',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=500, verbose_name='Nombre')),
                ('titulo_de_tesis', models.CharField(blank=True, max_length=500, verbose_name='titulo de la tesis')),
                ('grado', models.CharField(blank=True, choices=[('licenciatura', 'licenciatura'), ('maestría', 'maestría'), ('doctorado', 'doctorado')], max_length=500, verbose_name='Tipo de grado')),
                ('institucion', models.CharField(blank=True, max_length=500, verbose_name='Institucion')),
                ('fecha', models.CharField(blank=True, max_length=500, verbose_name='fecha')),
                ('notas', models.CharField(blank=True, max_length=500, verbose_name='notas')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 6',
                'verbose_name_plural': 'Campos del Modelo 6',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo5',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_curso', models.CharField(blank=True, max_length=500, verbose_name='Nombre del Curso')),
                ('periodo_numeral', models.CharField(blank=True, max_length=500, verbose_name='Periodo del numeral')),
                ('notas', models.CharField(blank=True, max_length=500, verbose_name='Notas')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 5',
                'verbose_name_plural': 'Campos del Modelo 5',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo4',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(blank=True, max_length=500, verbose_name='Nombre completo')),
                ('titulo_de_tesis', models.CharField(blank=True, max_length=500, verbose_name='Titulo de tesis')),
                ('fecha', models.CharField(blank=True, max_length=500, verbose_name='fecha')),
                ('url', models.CharField(blank=True, max_length=500, verbose_name='link de la url')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 4',
                'verbose_name_plural': 'Campos del Modelo 4',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=500, verbose_name='Titulo de la presentacion')),
                ('autores', models.TextField(blank=True, max_length=15000, verbose_name='Nombre de los autores')),
                ('nombre_de_conferencia', models.CharField(blank=True, max_length=500, verbose_name='Nombre de la conferencia')),
                ('fecha', models.CharField(blank=True, max_length=500, verbose_name='fecha')),
                ('tipo', models.CharField(blank=True, choices=[('presentacion oral', 'presentacion oral'), ('poster', 'poster')], max_length=500, verbose_name='Presentacion oral o poster')),
                ('estudiantes', models.CharField(blank=True, max_length=10000, verbose_name='Nombre de los estudiantes')),
                ('doi', models.CharField(blank=True, max_length=500, verbose_name='DOI/ISBN')),
                ('url', models.CharField(blank=True, max_length=500, verbose_name='Nombre de la url')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 3',
                'verbose_name_plural': 'Campos del Modelo 3',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_proyecto', models.CharField(blank=True, max_length=500, verbose_name='Nombre del proyecto')),
                ('descripcion', models.TextField(blank=True, max_length=15000, verbose_name='descripcion')),
                ('participantes', models.TextField(blank=True, max_length=500, verbose_name='participantes')),
                ('estudiantes', models.CharField(blank=True, max_length=10000, verbose_name='estudiantes')),
                ('rol', models.CharField(blank=True, choices=[('Responsable', 'Responsable'), ('Técnico', 'Tecnico'), ('Participante', 'Participante')], max_length=500, verbose_name='Rol')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 2',
                'verbose_name_plural': 'Campos del Modelo 2',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo16',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_estudiante', models.CharField(blank=True, max_length=500, verbose_name='Nombre de estudiantes')),
                ('coordinacion', models.CharField(blank=True, max_length=500, verbose_name='Coordinacion')),
                ('grado', models.CharField(blank=True, max_length=500, verbose_name='grado')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 16',
                'verbose_name_plural': 'Campos del Modelo 16',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo15',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, max_length=15000, verbose_name='descripcion')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='anexo')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 15',
                'verbose_name_plural': 'Campos del Modelo 15',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo14',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, max_length=15000, verbose_name='Descripcion')),
                ('telescopio_instrumento_infra', models.CharField(blank=True, choices=[('Telescopio', 'Telescopio'), ('Instrumento', 'Instrumento'), ('Infraestructura', 'Infraestructura')], max_length=500, verbose_name='Telescopio, instrumento, infraestructura')),
                ('url', models.CharField(blank=True, max_length=100, verbose_name='url')),
                ('conferencia_proyecto', models.CharField(blank=True, max_length=500, verbose_name='Conferencia o proyecto')),
                ('rol', models.CharField(blank=True, max_length=500, verbose_name='rol')),
                ('fecha', models.CharField(blank=True, max_length=200, verbose_name='fecha')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='anexo')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 14',
                'verbose_name_plural': 'Campos del Modelo 14',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo13',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, max_length=15000, verbose_name='Descripcion')),
                ('agencias_financieras', models.CharField(blank=True, max_length=500, verbose_name='Agencias Financieras')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 13',
                'verbose_name_plural': 'Campos del Modelo 13',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo12',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('laboratorio_taller', models.CharField(blank=True, max_length=500, verbose_name='Laboratorio o taller')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 12',
                'verbose_name_plural': 'Campos del Modelo 12',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo11',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_del_estudiante', models.CharField(blank=True, max_length=500, verbose_name='Nombre del estudiante')),
                ('descripcion', models.TextField(blank=True, max_length=15000, verbose_name='Descripcion')),
                ('fecha', models.CharField(blank=True, max_length=500, verbose_name='Fecha')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 11',
                'verbose_name_plural': 'Campos del Modelo 11',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo10',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, max_length=15000, verbose_name='descripcion')),
                ('fecha', models.CharField(blank=True, max_length=500, verbose_name='fecha')),
                ('url', models.CharField(blank=True, max_length=500, verbose_name='url')),
                ('periodo_numeral', models.CharField(blank=True, max_length=500, verbose_name='periodo')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'campo Modelo 10',
                'verbose_name_plural': 'Campos del Modelo 10',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Modelo1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('autores', models.TextField(blank=True, max_length=15000, verbose_name='Nombre de los autores')),
                ('fecha', models.CharField(blank=True, max_length=100, verbose_name='Fecha del articulo')),
                ('titulo', models.TextField(blank=True, max_length=15000, verbose_name='Nombre del titulo')),
                ('revista_publicacion', models.CharField(blank=True, max_length=250, verbose_name='Nombre de la revista o publicacion')),
                ('url', models.URLField(blank=True, max_length=100, verbose_name='url del articulo')),
                ('estudiantes_en_articulo', models.CharField(blank=True, max_length=250, verbose_name='Nombre de los estudiantes en el articulo')),
                ('doi', models.CharField(blank=True, max_length=150, verbose_name='Nombre de doi')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('periodo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Periodo')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Campo Modelo 1',
                'verbose_name_plural': 'Campos del Modelo 1',
                'ordering': ['fecha_de_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Citas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('citas', models.IntegerField(default=0, verbose_name='Citas')),
                ('citas_en_periodo', models.IntegerField(default=0, verbose_name='Citas durante periodo del reporte')),
                ('indiceH', models.IntegerField(default=0, verbose_name='Indice H')),
                ('anexos', models.FileField(blank=True, upload_to='anexos/', verbose_name='archivo PDF')),
                ('fecha_de_creacion', models.DateTimeField(auto_now_add=True, verbose_name='Fecha y Hora de creacion')),
                ('numeral', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reportes.Numeral')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'cita del periodo',
                'verbose_name_plural': 'Citas del periodo',
                'ordering': ['fecha_de_creacion'],
            },
        ),
    ]
