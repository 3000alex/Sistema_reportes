import ads
from django.shortcuts import render
from django.http import JsonResponse
#Vistas genericas
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic import View,ListView
from django.core import serializers
# Create your views here.
class metricasForm(TemplateView):
    template_name = "metricas.html"

class obtenerGrafico(View):

    def get(self,request):

        query = request.GET.get('query', None) 

        # determinamos nuestro token de busqueda
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7'

        data = ads.SearchQuery(q=query,rows=1000)  # Buscar por orcid
        
        for m in data:
            metrica = m.metrics
            print(metrica['basic stats'])
            metrica = metrica['basic stats']
            metrica = metrica['normalized paper count']
            
                
            

        data = {
            'query': metrica  # Objeto de Json con los datos actualizados.
        }

        return JsonResponse(data)