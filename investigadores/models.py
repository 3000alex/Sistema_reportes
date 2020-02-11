from django.db import models
from registration.models import User
from datetime import *
# Create your models here.
Seccionselect = (
        ('Investigacion Cientifica','Investigacion Cientifica'),
        ('Formacion de Recursos Humanos','Formacion de Recursos Humanos'),
        ('Desarrollo Tecnologico e Innovacion','Desarrollo Tecnologico e Innovacion'),
        ('Apoyo Institucional','Apoyo Institucional'),
        ('Informacion Adicional','Informacion Adicional'),

    )

Presentacionselect = (
    ('presentacion oral','presentacion oral'),
    ('poster','poster'),
)

Gradoselect = (
    ('licenciatura','licenciatura'),
    ('maestría','maestría'),
    ('doctorado','doctorado'),
)

ResponsableSelect = (
    ('Responsable','Responsable'),
    ('Técnico','Tecnico'),
    ('Participante','Participante'),
)

GlosarioSelect = (
    ('I. INVESTIGACIÓN CIENTÍFICA', 'I. INVESTIGACIÓN CIENTÍFICA'),
    ('II. FORMACIÓN DE RECURSOS HUMANOS', 'II. FORMACIÓN DE RECURSOS HUMANOS'),
    ('III. DESARROLLO TECNOLÓGICO E INNOVACIÓN(agregar patentes en REGISTRO)', 'III. DESARROLLO TECNOLÓGICO E INNOVACIÓN(agregar patentes en REGISTRO)'),
    ('IV. APOYO INSTITUCIONAL', 'IV. APOYO INSTITUCIONAL'),
    ('V. INFORMACIÖN ADICIONAL', 'V. INFORMACIÖN ADICIONAL' ),
)

class Numeral(models.Model):
    nombre = models.CharField(max_length=190,verbose_name="Nombre del numeral",blank=True)
    nombreDeSeccion = models.CharField(max_length=150,verbose_name="Nombre de la seccion",choices=Seccionselect)
    orden = models.FloatField(verbose_name="Ordenamiento",null=True)

    class Meta:
        verbose_name="Numeral"
        verbose_name_plural = "Numerales"
        ordering = ['orden']
    
    def __str__(self):
        return self.nombre

class Glosario(models.Model):
    seccion = models.CharField(max_length=200, verbose_name="Seccion perteneciente", choices=GlosarioSelect)
    numerales = models.TextField(max_length=5000, verbose_name="Nombre del numeral")
    explicacion = models.TextField(max_length=5000, verbose_name="Explicación")
    
    class Meta:
        verbose_name = "glosario"
        verbose_name_plural = "Glosarios"
        ordering = ['numerales']
    
    def __str__(self):
        return self.seccion

class Periodo(models.Model):
    nombrePeriodo = models.CharField(max_length=150, verbose_name="Nombre del periodo")
    fechaInicio = models.DateTimeField(verbose_name="Fecha del inicio de periodo",auto_now_add=True)
    class Meta:
        verbose_name="Periodo del reporte"
        verbose_name_plural = "Periodos de los reportes"
        ordering = ['fechaInicio']
    
    def __str__(self):
        return self.nombrePeriodo

#Modelo 1 comprende los numerales 1-14, 15-17(A excepcion del campo estudiantes), y el numeral 23
class Modelo1(models.Model):
    usuario =  models.ForeignKey(User,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    autores = models.TextField(max_length=15000,verbose_name="Nombre de los autores", blank=True)
    titulo = models.TextField(max_length=15000,verbose_name="Nombre del titulo", blank=True)
    revistaPublicacion = models.CharField(max_length=250,verbose_name="Nombre de la revista o publicacion", blank=True)
    url = models.CharField(max_length=100,verbose_name="url del articulo", blank=True)
    estudiantesEnArticulo = models.CharField(max_length=250,verbose_name="Nombre de los estudiantes en el articulo", blank=True)
    doi = models.CharField(max_length=150,verbose_name="Nombre de doi", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF",  upload_to='anexos/', null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    

    class Meta:
        verbose_name="Campo Modelo 1"
        verbose_name_plural = "Campos del Modelo 1"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 2 comprende los numerales 18-22
class Modelo2(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nombreProyecto = models.CharField(max_length=500,verbose_name="Nombre del proyecto",blank=True)
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion",blank=True)
    participantes = models.TextField(max_length=500,verbose_name="participantes",blank=True)
    estudiantes = models.CharField(max_length=10000,verbose_name="estudiantes",blank=True)
    responsableTecParticipante = models.CharField(max_length=500,verbose_name="responsable,tecnico o participante", blank=True,choices=ResponsableSelect)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    

    class Meta:
        verbose_name="campo Modelo 2"
        verbose_name_plural = "Campos del Modelo 2"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 3 comprende los numerales 24-25, 26-27(Sin el campo presentacion Oral o Poster), 28-29
class Modelo3(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    tituloPresentacion = models.CharField(max_length=500,verbose_name="Titulo de la presentacion", blank=True)
    autores = models.TextField(max_length=15000,verbose_name="Nombre de los autores", blank=True,)
    nombreConferencia = models.CharField(max_length=500,verbose_name="Nombre de la conferencia", blank=True)
    fecha = models.CharField(max_length=500,verbose_name="fecha", blank=True)
    presentacionPoster = models.CharField(max_length=500,verbose_name="Presentacion oral o poster",choices=Presentacionselect, blank=True)
    estudiantes = models.CharField(max_length=10000,verbose_name="Nombre de los estudiantes", blank=True)
    doi = models.CharField(max_length=500,verbose_name="DOI/ISBN", blank=True)
    url = models.CharField(max_length=500,verbose_name="Nombre de la url", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name="campo Modelo 3"
        verbose_name_plural = "Campos del Modelo 3"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 4 comprende los numerales 31-34
class Modelo4(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nombreCompleto = models.CharField(max_length=500,verbose_name="Nombre completo", blank=True)
    tituloTesis = models.CharField(max_length=500,verbose_name="Titulo de tesis", blank=True)
    fecha = models.CharField(max_length=500,verbose_name="fecha", blank=True)
    url = models.CharField(max_length=500,verbose_name="link de la url", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name="campo Modelo 4"
        verbose_name_plural = "Campos del Modelo 4"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 5 comprende los numerales 35-36
class Modelo5(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nombreCurso = models.CharField(max_length=500,verbose_name="Nombre del Curso", blank=True)
    periodoNumeral = models.CharField(max_length=500,verbose_name="Periodo del numeral", blank=True)
    notas = models.CharField(max_length=500,verbose_name="Notas", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', blank=True,)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name="campo Modelo 5"
        verbose_name_plural = "Campos del Modelo 5"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 6 comprende a los numerales 37(Sin el atributo de fecha),39
class Modelo6(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=500,verbose_name="Nombre", blank=True)
    tituloTesis = models.CharField(max_length=500,verbose_name="titulo de la tesis", blank=True)
    Grado = models.CharField(max_length=500,verbose_name="Tipo de grado", blank=True,choices=Gradoselect)
    institucion = models.CharField(max_length=500,verbose_name="Institucion", blank=True)
    fecha = models.CharField(max_length=500,verbose_name="fecha", blank=True)
    notas = models.CharField(max_length=500,verbose_name="notas", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/',null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    

    class Meta:
        verbose_name="campo Modelo 6"
        verbose_name_plural = "Campos del Modelo 6"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 7 comprende numerales 40-44
class Modelo7(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    autores = models.TextField(max_length=15000,verbose_name="autores", blank=True)
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion", blank=True)
    url = models.CharField(max_length=500,verbose_name="url", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name="campo Modelo 7"
        verbose_name_plural = "Campos del Modelo 7"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 8 comprende numeral 45
class Modelo8(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=500,verbose_name="nombre", blank=True)
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion", blank=True)
    participantes = models.TextField(max_length=500,verbose_name="participantes", blank=True)
    url = models.CharField(max_length=500,verbose_name="url", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/',null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name="campo Modelo 8"
        verbose_name_plural = "Campos del Modelo 8"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo9 comprende los numerales 46 (Sin revista o publcacion) y el 48
class Modelo9(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    titulo = models.TextField(max_length=15000,verbose_name="titulo", blank=True)
    autores = models.TextField(max_length=15000,verbose_name="autores", blank=True)
    numeroReportes = models.CharField(max_length=500,verbose_name="numero de reportes", blank=True,)
    fecha = models.CharField(max_length=500,verbose_name="fecha", blank=True)
    url = models.CharField(max_length=500,verbose_name="url", blank=True)
    revistaPublicacion = models.CharField(max_length=500,verbose_name="revista o publicacion", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name="campo Modelo 9"
        verbose_name_plural = "Campos del Modelo 9"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#El modelo 10 comprende del numeral 49 al 52 con los subnumerales 49a,49b. 52a(Con sus campos CursosCortos-Descripcion y periodo)
class Modelo10(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion", blank=True)
    fecha = models.CharField(max_length=500,verbose_name="fecha", blank=True)
    url = models.CharField(max_length=500,verbose_name="url", blank=True)
    periodoNumeral = models.CharField(max_length=500,verbose_name="periodo", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/',null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name="campo Modelo 10"
        verbose_name_plural = "Campos del Modelo 10"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#El modelo 11 comprende los numerales 53(Sin el atributo fecha), 54(Solo el atributo fecha), 55-56 (Fecha o periodo)
class Modelo11(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nombreEstudiante = models.CharField(max_length=500,verbose_name="Nombre del estudiante", blank=True)
    descripcion = models.TextField(max_length=15000,verbose_name="Descripcion", blank=True)
    fecha = models.CharField(max_length=500,verbose_name="Fecha", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name="campo Modelo 11"
        verbose_name_plural = "Campos del Modelo 11"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 12 comprende el numeral 58
class Modelo12(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    laboratorioTaller = models.CharField(max_length=500,verbose_name="Laboratorio o taller", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/',null=True, )
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion", blank=True)
    
    class Meta:
        verbose_name="campo Modelo 12"
        verbose_name_plural = "Campos del Modelo 12"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 13 comprende el numeral 59
class Modelo13(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=15000,verbose_name="Descripcion", blank=True)
    agenciasFinancieras = models.CharField(max_length=500,verbose_name="Agencias Financieras", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name="campo Modelo 13"
        verbose_name_plural = "Campos del Modelo 13"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Modelo 14 Comprende el numeral 61
class Modelo14(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=15000,verbose_name="Descripcion", blank=True)
    TelescopioInstrumentoInfra = models.CharField(max_length=500,verbose_name="Opciones", blank=True)
    participantes = models.CharField(max_length=500,verbose_name="Participaciones", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name="campo Modelo 14"
        verbose_name_plural = "Campos del Modelo 14"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

# Modelo 15 comprende los nuumerales 38,47,57,60
class Modelo15(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    descripcion = models.TextField(max_length=15000,verbose_name="descripcion", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', null=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion", blank=True)
    
    class Meta:
        verbose_name="campo Modelo 15"
        verbose_name_plural = "Campos del Modelo 15"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

#Numeral 
class Modelo16(models.Model):
    usuario =  models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    nombreEstudiante = models.CharField(max_length=500,  verbose_name="Nombre de estudiantes", blank=True)
    anexos = models.FileField(verbose_name="archivo PDF", upload_to='anexos/', null=True, blank=True)
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion", blank=True)

    class Meta:
        verbose_name="campo Modelo 16"
        verbose_name_plural = "Campos del Modelo 16"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

class Citas(models.Model):
    usuario = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, null=True,blank=True, on_delete=models.CASCADE)
    periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    citas = models.CharField(verbose_name="Citas", max_length=10, blank=True)
    citasObtenidasEnPeriodo = models.CharField(verbose_name="Citas durante periodo del reporte", blank=True,max_length=10)
    indiceH = models.CharField(verbose_name="Indice H",  blank=True, max_length=3)
    anexos = models.FileField(verbose_name="archivo PDF",  null=True, upload_to='anexos/')
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha y Hora de creacion")
    
    class Meta:
        verbose_name ="cita del periodo"
        verbose_name_plural = "Citas del periodo"
        ordering = ['fechaCreacion']

    def __str__(self):
        return self.numeral.nombre

class ReporteEnviado(models.Model):
    usuario = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    reporte = models.FileField(verbose_name="reporte", null=True, blank=True, upload_to='reportes/pdfs/')
    anexo = models.FileField(verbose_name="anexos", null=True, blank=True, upload_to='reportes/anexos/')
    periodo = models.ForeignKey(Periodo, null=True,blank=True, on_delete=models.CASCADE, verbose_name="periodo")
    fechaCreacion = models.DateTimeField(auto_now_add=True, verbose_name="fecha")

    class Meta:
        verbose_name = "Reporte Enviado"
        verbose_name_plural = "Reportes Enviados"
        ordering = ['usuario']

    def __str__(self):
        return self.periodo.nombrePeriodo
    