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
        
        citasTotales = metricas['citation stats refereed']['total number of citations']
        citasNormalizadas = metricas['citation stats refereed']['normalized number of citations']
        citasReferenciadas = metricas['citation stats refereed']['total number of refereed citations']
        citasReferenciadasNormalizadas = metricas['citation stats refereed']['normalized number of refereed citations']
        citasLabels = metricas['histograms']['citations']['nonrefereed to refereed']
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
            'citasLabels':citasLabels,
            'titulo': titulo,
        }
        
        return JsonResponse(datos)