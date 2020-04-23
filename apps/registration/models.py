from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    
    categoria_select = (
        ('select','sin especificar'),
        ('Investigador posdoctoral','Investigador posdoctoral'),
        ('Cátedra CONACyT',"Cátedra CONACyT"),
        ('Investigador Asociado C','Investigador Asociado C'),
        ('Investigador Titular A','Investigador Titular A'),
        ('Investigador Titular B','Investigador Titular B'),
        ('Investigador Titular C','Investigador Titular C'),
        ('Investigador Titular D','Investigador Titular D'),
    )
    nivelSni_select = (
        ('Sin Nombramiento','Sin Nombramiento'),
        ('Candidato','Candidato'),
        ('Nivel 1','Nivel 1'),
        ('Nivel 2','Nivel 2'),
        ('Nivel 3','Nivel 3'),
        ('Emérito','Emérito'),
    )
    
    nombreCorto = models.CharField(max_length=50, verbose_name="Nombre corto", null=True, blank=True)
    correoAlternativo = models.EmailField(max_length=50, verbose_name="Correo alternativo", blank=True)
    categoria = models.CharField(max_length=50, blank=True, verbose_name="Nombramiento", choices= categoria_select)
    nivelSni = models.CharField(max_length=50, blank=True, verbose_name="Nivel de SNI",  choices= nivelSni_select)
    orcId = models.CharField(max_length=50, blank=True, verbose_name="Orc ID")
    arxivId = models.CharField(max_length=50, blank=True, verbose_name="Arxiv ID")

    class Meta:
        verbose_name="Usuario"
        verbose_name_plural = "Usuarios"
        ordering = ['nombreCorto']
    
    def __str__(self):
        return self.first_name +" "+ self.last_name
    