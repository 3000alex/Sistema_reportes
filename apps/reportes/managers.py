from django.db import models

class modelo1Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo1(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo2Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response

    def anexosModelo2(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo3Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo3(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo4Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response

    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo4(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo5Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo5(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo6Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo6(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo7Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo7(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo8Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo8(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo9Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo9(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo10Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response

    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo10(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo11Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo11(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo12Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo12(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo13Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo13(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo14Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo14(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo15Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo15(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class modelo16Manager(models.Manager):
    """Managers para el modelo biblioteca"""
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,periodo__fecha_inicio__year=fecha_ano)
        return response
    
    def entradasContador(self,year,numeral):
        response = str(self.filter(periodo__fecha_inicio__year=year, numeral_id=numeral).count())
        return response
    
    def anexosModelo16(self,user,year):
        response = self.exclude(anexos= "").filter(usuario_id = user, periodo__fecha_inicio__year= year)
        return response

class citasManager(models.Manager):
    def reporteProductividad(self,user_id):
        response = self.filter(usuario_id=user_id)
        return response
    
    def anexosCitas(self,user):
        response = self.exclude(anexos= "").filter(usuario_id = user)
        return response

class glosarioManager(models.Manager):
    def reporteProductividad(self,seccion):
        response = self.filter(seccion=seccion)
        return response



