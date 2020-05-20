from django.db import models

class BibliotecaManager(models.Manager):
    """Managers para el modelo biblioteca"""

    def listarBiblioteca(self,user):
        response = self.filter(usuario_id = user)
        return response

    def bibliotecaId(self,pk):
        response = self.filter(id = pk)
        return response
    
    def reporteProductividad(self,user,numeral,fecha_ano):
        response = self.filter(usuario_id=user,numeral_id=numeral,fecha_ano=fecha_ano)
        return response
    
    def reporteProductividad2(self,user,fecha_ano):
        response = self.filter(usuario_id=user,fecha_ano=fecha_ano)
        return response

    def entradasContador(self,year,numeral):
        response = str(self.filter(fecha_ano=year,numeral_id=numeral).count())
        return  response