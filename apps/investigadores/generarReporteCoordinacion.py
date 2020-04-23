from .models import Numeral, Citas, Modelo1, Modelo2, Modelo3, Modelo4, Modelo5, Modelo6, Modelo7, Modelo8, Modelo9, Modelo10
from .models import Modelo11, Modelo12, Modelo13, Modelo14, Modelo15, Modelo16, Periodo
from apps.registration.models import User
from apps.biblioteca.models import Biblioteca
from datetime import date
from datetime import datetime
from django.http import HttpResponse
from django.template.loader import get_template

def generarPdf(request,periodo_id):
    template = get_template('investigadores/templateReporte.html')
    #periodo = Periodo.objects.last()
    periodo = Periodo.objects.get(id=periodo_id) #Para obtener valores del 2019
    yearPeriodo = periodo.fechaInicio.year
    mesFin = ""
    if periodo.fechaInicio.month == 1:
        mesFin = "JUNIO"
    elif periodo.fechaInicio.month == 6:
        mesFin = "DICIEMBRE"
    
    dataReporte = {
        'fechaInicioP': periodo.fechaInicio,
        'mesFin':mesFin,
        'datosInvestigador': User.objects.get(id=request.user.id),
        'numeral': Numeral.objects.all(),
        'citas': Citas.objects.filter(usuario_id=request.user.id,periodo__fechaInicio__year = yearPeriodo),
        'biblioteca': Biblioteca.objects.filter( user_id=request.user.id, fecha_ano=yearPeriodo),
        'modelo1': Modelo1.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo2': Modelo2.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo3': Modelo3.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
            
        #Formacion_RH
        'modelo4': Modelo4.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo5': Modelo5.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo6':Modelo6.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        #Desarrollo Tec. Inn.
        'modelo7': Modelo7.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo8': Modelo8.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo9': Modelo9.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
            
        #Apoyo Institucional
        'modelo10': Modelo10.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo11': Modelo11.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo12': Modelo12.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo13': Modelo13.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        #Informacion Adicional
        'modelo14': Modelo14.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo15': Modelo15.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
        'modelo16': Modelo16.objects.filter(usuario_id=request.user.id, periodo__fechaInicio__year = yearPeriodo),
    }
    html = template.render(dataReporte)

    return html