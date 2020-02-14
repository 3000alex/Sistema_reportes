from django.urls import path
from . import views as vista

reporteSNIpatterns = ([
    path('Instrucciones-ReporteSNI/', vista.instruccionesSNI.as_view(), name="instruccionesSNI"),
    path('ReporteSNI/', vista.reporteSNI.as_view(), name="reporteSNI"),
    path('metodo1SNI/', vista.metodo1ReporteSNI.as_view(), name="metodo1SNI"),
    path('metodo2SNI/', vista.metodo2ReporteSNI.as_view(), name="metodo2SNI"),
],'reporteSNI')