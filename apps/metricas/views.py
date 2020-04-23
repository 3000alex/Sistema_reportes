import ads
from django.shortcuts import render
from django.http import JsonResponse
#Vistas genericas
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic import View,ListView
from django.core import serializers
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

# Create your views here.
@method_decorator(login_required, name='dispatch')
class metricasForm(TemplateView):
    template_name = "metricas/metricas.html"

@method_decorator(login_required, name='dispatch')
class obtenerGrafico(View):

    def post(self,request):
        # determinamos nuestro token de busqueda
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7'
        query = request.POST.get('query', None)
        query = list(ads.SearchQuery(q=query, fl='bibcode,title'))
        bibcode = ""
       
        for q in query:
            bibcode = q.bibcode
            titulo = q.title[0]

        metricas = ads.MetricsQuery(bibcode).execute()  # Buscar por orcid            
        #Citas tabla
        citasTotales = metricas['citation stats refereed']['total number of citations']
        citasNormalizadas = metricas['citation stats refereed']['normalized number of citations']
        citasReferenciadas = metricas['citation stats refereed']['total number of refereed citations']
        citasReferenciadasNormalizadas = metricas['citation stats refereed']['normalized number of refereed citations']
        #Reads tabla
        numTotalLecturas = metricas['basic stats refereed']['total number of reads']
        numTotalDescargas = metricas['basic stats refereed']['total number of downloads']
        
        #grafics
        #Citas Totales
        refereed_to_refereed = metricas['histograms']['citations']['refereed to refereed']
        nonrefereed_to_refereed = metricas['histograms']['citations']['nonrefereed to refereed']
        #citas Totales Normalizadas
        refereed_to_refereed_normalized = metricas['histograms']['citations']['refereed to refereed normalized']
        nonrefereed_to_refereed_normalized = metricas['histograms']['citations']['nonrefereed to refereed normalized']
        #Reads Totales
        refereed_reads = metricas['histograms']['reads']['refereed reads']
        refereed_reads_normalized = metricas['histograms']['reads']['refereed reads normalized']
        
        datos ={
            'citasTotales': citasTotales,
            'citasNormalizadas':citasNormalizadas,
            'citasReferenciadas':citasReferenciadas,
            'citasReferenciadasNormalizadas':citasReferenciadasNormalizadas,
            'numTotalLecturas':numTotalLecturas,
            'numTotalDescargas':numTotalDescargas,
            'titulo': titulo,
            'refereed_to_refereed':refereed_to_refereed,
            'nonrefereed_to_refereed':nonrefereed_to_refereed,
            'refereed_to_refereed_normalized':refereed_to_refereed_normalized,
            'nonrefereed_to_refereed_normalized':nonrefereed_to_refereed_normalized,
            'refereed_reads':refereed_reads,
            'refereed_reads_normalized':refereed_reads_normalized
        }
        
        return JsonResponse(datos)