from django.urls import path
from . import views


metricaspatterns = ([ 
    #Rutas biblioteca
    path('metricasForm/', views.metricasForm.as_view(), name="metricasForm"),
    path('obtenerGrafico/', views.obtenerGrafico.as_view(), name="obtenerGrafico"),
],'metricas')
