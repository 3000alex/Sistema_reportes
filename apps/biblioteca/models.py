from django.db import models
from apps.registration.models import User
from apps.investigadores.models import Periodo,Numeral
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

    usuario = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    fecha  = models.CharField(max_length=50,verbose_name="Fecha", null=True, blank=True)
    fecha_ano = models.CharField(max_length=50,verbose_name="Fecha", null=True, blank=True)
    numeral = models.ForeignKey(Numeral, null=True, blank=True, on_delete=models.CASCADE)
    doi = models.CharField(max_length=100,verbose_name="doi", null=True,blank=True)
    bibcode = models.CharField(max_length=80, verbose_name="bibcode", null=True, blank=True,unique=True)
    titulo = models.TextField(max_length=15000, verbose_name="titulo", null=True, blank=True)
    autores = models.TextField(max_length=15000, verbose_name="autores", null=True, blank=True)
    estudiantesEnArticulo = models.CharField(max_length=150,verbose_name="Estudiantes en el articulo", null=True, blank=True)
    revistaPublicacion = models.CharField(max_length=150,blank=True,null=True)
    paginas = models.CharField(max_length=150, blank=True,null=True)
    volumen = models.CharField(max_length=150, blank=True,null=True)
    url = models.CharField(max_length=550, blank=True,null=True)
    anexos = models.FileField(verbose_name="archivo PDF",  upload_to='anexos/',  blank=True)
    
    objects = BibliotecaManager()
    class Meta:
        verbose_name = "biblioteca"
        verbose_name_plural = "bibliotecas"
        ordering = ['-fecha']
    
    def __str__(self):
        return self.usuario.first_name