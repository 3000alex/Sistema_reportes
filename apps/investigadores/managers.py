from django.db import models

class modelo1Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo2Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo3Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo4Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo5Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo6Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo7Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo8Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo9Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo10Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo11Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo12Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo13Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo14Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo15Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class modelo16Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fechaInicio__year=fecha_ano)
        return response

class citasManager(models.Manager):
    def reporteProductividad(self,user_id):
        response = self.filter(usuario_id=user_id)
        return response

class glosarioManager(models.Manager):
    def reporteProductividad(self,seccion):
        response = self.filter(seccion=seccion)
        return response



