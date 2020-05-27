from django.db import models
from apps.registration.models import User
from apps.reportes.models import Periodo,Numeral
#Managers
from .managers import BibliotecaManager
# Create your models here.
class Biblioteca(models.Model):
    cuartil_select = (
        ('No aplica','No aplica'),
        ('Primero','Primero'),
        ('Segundo','Segundo'),
        ('Tercero','Tercero'),
        ('Cuarto','Cuarto'),
    )

    usuario = models.ForeignKey(User,blank=True, on_delete=models.CASCADE)
    numeral = models.ForeignKey(Numeral, blank=True, on_delete=models.CASCADE, null=True)
    fecha  = models.CharField(max_length=50,verbose_name="Fecha", blank=True,default='')
    fecha_ano = models.CharField(max_length=50,verbose_name="Fecha", blank=True,default='')
    doi = models.CharField(max_length=100,verbose_name="doi", blank=True,default='')
    bibcode = models.CharField(max_length=80, verbose_name="bibcode",blank=True,default='')
    titulo = models.TextField(max_length=15000, verbose_name="titulo", blank=True,default='')
    autores = models.TextField(max_length=15000, verbose_name="autores", blank=True,default='')
    estudiantes_en_articulo = models.CharField(max_length=150,verbose_name="Estudiantes en el articulo", blank=True,default='')
    revista_publicacion = models.CharField(max_length=150,blank=True,default='')
    paginas = models.CharField(max_length=150, blank=True,default='')
    volumen = models.CharField(max_length=150, blank=True,default='')
    url = models.CharField(max_length=550, blank=True,default='')
    anexos = models.FileField(verbose_name="archivo PDF",  upload_to='anexos/', blank=True)
    
    objects = BibliotecaManager()
    class Meta:
        verbose_name = "biblioteca"
        verbose_name_plural = "bibliotecas"
        ordering = ['-fecha']
    
    def __str__(self):
        return self.usuario.nombre