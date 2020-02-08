from django.db import models
from registration.models import User
from investigadores.models import Periodo,Numeral

# Create your models here.
class Biblioteca(models.Model):
    cuartil_select = (
        ('No aplica','No aplica'),
        ('Primero','Primero'),
        ('Segundo','Segundo'),
        ('Tercero','Tercero'),
        ('Cuarto','Cuarto'),
    )

    user = models.ForeignKey(User,null=True,blank=True, on_delete=models.CASCADE)
    fecha  = models.DateField(verbose_name="Fecha", null=True, blank=True)
    numeral = models.ForeignKey(Numeral, null=True, blank=True, on_delete=models.CASCADE)
    doi = models.CharField(max_length=100,verbose_name="doi", null=True,blank=True)
    bibcode = models.CharField(max_length=80, verbose_name="bibcode", null=True, blank=True)
    titulo = models.TextField(max_length=15000, verbose_name="titulo", null=True, blank=True)
    autores = models.TextField(max_length=15000, verbose_name="autores", null=True, blank=True)
    estudiantesEnArticulo = models.CharField(max_length=150,verbose_name="Estudiantes en el articulo", null=True, blank=True)
    revistaPublicacion = models.CharField(max_length=150,blank=True,null=True)
    paginas = models.CharField(max_length=150, blank=True,null=True)
    volumen = models.CharField(max_length=150, blank=True,null=True)
    url = models.CharField(max_length=550, blank=True,null=True)
    anexoPdf = models.FileField(verbose_name="archivo PDF",  upload_to='anexos/pdfs/',  blank=True)
    

    class Meta:
        verbose_name = "biblioteca"
        verbose_name_plural = "bibliotecas"
        ordering = ['-fecha']
    
    def __str__(self):
        return self.user.first_name