from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from .managers import UserManager
class User(AbstractBaseUser,PermissionsMixin):
    categoria_select = (
        ('Investigador posdoctoral','Investigador posdoctoral'),
        ('Cátedra CONACyT',"Cátedra CONACyT"),
        ('Investigador Asociado C','Investigador Asociado C'),
        ('Investigador Titular A','Investigador Titular A'),
        ('Investigador Titular B','Investigador Titular B'),
        ('Investigador Titular C','Investigador Titular C'),
        ('Investigador Titular D','Investigador Titular D'),
    )
    nivelSni_select = (
        ('Candidato','Candidato'),
        ('Nivel 1','Nivel 1'),
        ('Nivel 2','Nivel 2'),
        ('Nivel 3','Nivel 3'),
        ('Emérito','Emérito'),
    )
    
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellido = models.CharField(max_length=50, verbose_name="Apellido", blank=True)
    nombreCorto = models.CharField(max_length=50, verbose_name="Nombre corto", blank=True)
    correoAlternativo = models.EmailField(max_length=50, verbose_name="Correo alternativo", blank=True)
    categoria = models.CharField(max_length=50, blank=True, verbose_name="Categoria", default="Sin especificar", choices= categoria_select)
    nivelSni = models.CharField(max_length=50, blank=True, verbose_name="Nivel de SNI", default="Sin especificar", choices= nivelSni_select)
    orcId = models.CharField(max_length=50, blank=True, verbose_name="Orc ID")
    arxivId = models.CharField(max_length=50, blank=True, verbose_name="Arxiv ID")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name ="Investigador"
        verbose_name_plural = "Investigadores"
        ordering = ['apellido']

    USERNAME_FIELD = 'email'
    objects = UserManager()

    def get_short_name(self):
        return self.email
    
    def get_full_name(self):
        return self.nombre + ' ' + self.apellido
