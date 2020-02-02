from .models import Numeral, Citas, Modelo1, Modelo2, Modelo3, Modelo4, Modelo5, Modelo6, Modelo7, Modelo8, Modelo9, Modelo10
from .models import Modelo11, Modelo12, Modelo13, Modelo14, Modelo15, Modelo16, Periodo
from registration.models import User
from biblioteca.models import Biblioteca
from datetime import date
from datetime import datetime
from django.http import HttpResponse
from django.template.loader import get_template

def generarPdf(request,periodo_id):
    template = get_template('investigadores/templateReporte.html')
    #periodo = Periodo.objects.last()
    periodo = Periodo.objects.get(id=periodo_id) #Para obtener valores del 2019

    yearPeriodo = periodo.fechaInicio.year
    monthPeriodoInicio = periodo.fechaInicio.month
    monthPeriodoFin = periodo.fechaFin.month
 
    
    dataReporte = {
        'fechaInicioP': periodo.fechaInicio,
        'fechaFinP':periodo.fechaFin,
        'datosInvestigador': User.objects.get(id=request.user.id),
        'numeral': Numeral.objects.all(),
        'citas': Citas.objects.filter(usuario_id=request.user.id,periodo_id = periodo.id),
        'biblioteca': Biblioteca.objects.filter( user_id=request.user.id, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]),
        'modelo1': Modelo1.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo2': Modelo2.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo3': Modelo3.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
            
        #Formacion_RH
        'modelo4': Modelo4.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo5': Modelo5.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo6':Modelo6.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        #Desarrollo Tec. Inn.
        'modelo7': Modelo7.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo8': Modelo8.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo9': Modelo9.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
            
        #Apoyo Institucional
        'modelo10': Modelo10.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo11': Modelo11.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo12': Modelo12.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo13': Modelo13.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        #Informacion Adicional
        'modelo14': Modelo14.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo15': Modelo15.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
        'modelo16': Modelo16.objects.filter(usuario_id=request.user.id, periodo_id = periodo.id),
    }
    html = template.render(dataReporte)

    return html