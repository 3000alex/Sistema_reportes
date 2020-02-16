import ads
from django.shortcuts import render
from django.http import JsonResponse
#Vistas genericas
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic import View,ListView
from django.core import serializers
from django_pandas.io import read_frame
from django.http import HttpResponse
# Create your views here.
class metricasForm(TemplateView):
    template_name = "metricas/metricas.html"

class obtenerGrafico(View):

    def post(self,request):
        # determinamos nuestro token de busqueda
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7'
        query = request.POST.get('query', None) 
        data = []
        data.append(1)
        data.append(100)
        
        metricas = ads.MetricsQuery(query).execute()  # Buscar por orcid            
        
        citasTotales = metricas['citation stats refereed']['total number of citations']
        citasNormalizadas = metricas['citation stats refereed']['normalized number of citations']
        citasReferenciadas = metricas['citation stats refereed']['total number of refereed citations']
        citasReferenciadasNormalizadas = metricas['citation stats refereed']['normalized number of refereed citations']
        #Reads
        numTotalLecturas = metricas['basic stats refereed']['total number of reads']
        numTotalDescargas = metricas['basic stats refereed']['total number of downloads']
        
        datos ={
            'citasTotales': citasTotales,
            'citasNormalizadas':citasNormalizadas,
            'citasReferenciadas':citasReferenciadas,
            'citasReferenciadasNormalizadas':citasReferenciadasNormalizadas,
            'numTotalLecturas':numTotalLecturas,
            'numTotalDescargas':numTotalDescargas,
            'arreglo':data
        }
        
        return JsonResponse(datos)