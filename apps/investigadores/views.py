# Redirecciones
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
# Vistas genericas
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic import View, ListView
from django.views.generic import FormView
# Librerias para validar el login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Modelos y forms
from .models import Numeral, Citas, ReporteEnviado, Modelo1, Modelo2, Modelo3, Modelo4, Modelo5, Modelo6, Modelo7, Modelo8, Modelo9, Modelo10, Glosario
from .models import Modelo11, Modelo12, Modelo13, Modelo14, Modelo15,Modelo16, Periodo
from apps.registration.models import User
from apps.biblioteca.models import Biblioteca
from .models import ReporteEnviado
from datetime import date
from datetime import datetime
from django.http import JsonResponse

# Manejo Archivos
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from django.core.files.base import ContentFile
from django.core.files.base import File as contenidoFile
#Zip
import zipfile
import zlib
from io import StringIO
#PDF 
import pdfkit
from io import BytesIO
from django.core.files import File
#config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  #Linux
config =  pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe') #Windows
# Correo
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.core.files import File
from email.mime.base import MIMEBase
from email import encoders
from sistema_reportes.settings import BASE_DIR
#Reporte final
from .generarReporteCoordinacion import generarPdf
#Time zone
import datetime

@method_decorator(login_required, name='dispatch')
class reporte_productividad(View):
    def get(self,request):
        periodoActual =  Periodo.objects.last()
        periodos = Periodo.objects.all()
        data = {
            'periodoActual': periodoActual,'periodos':periodos
        }
        return render(request, 'investigadores/reportes_productividad.html',data)

@method_decorator(login_required, name='dispatch')
class investigacion_cientifica(View):

    def get(self,request):
        id1 = request.GET.get('periodoActual')
        periodoActual = Periodo.objects.get(id = id1)
        periodos = Periodo.objects.all()
        yearPeriodo = periodoActual.fechaInicio.year
        data = {
            "numeralName": Numeral.objects.filter(nombreDeSeccion="Investigacion Cientifica"),
            'numeral_1': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=1, fecha_ano=yearPeriodo),
            'numeral_2': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=2, fecha_ano=yearPeriodo), 
            'numeral_3': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=3, fecha_ano=yearPeriodo),
            'numeral_4': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=4, fecha_ano=yearPeriodo),
            'numeral_5': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=5, fecha_ano=yearPeriodo), 
            'numeral_6': Modelo1.objects.filter(usuario_id=request.user.id, numeral_id=6, periodo__fechaInicio__year = yearPeriodo),
            'numeral_7': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=7, fecha_ano=yearPeriodo), 
            'numeral_8': Modelo1.objects.filter(usuario_id=request.user.id, numeral_id=8, periodo__fechaInicio__year = yearPeriodo),
            'numeral_9': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=9, fecha_ano=yearPeriodo),
            "numeral_10": Modelo1.objects.filter(usuario_id=request.user.id, numeral_id=10, periodo__fechaInicio__year = yearPeriodo),
            'numeral_11': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=11, fecha_ano=yearPeriodo), 
            'numeral_12': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=12, fecha_ano=yearPeriodo),
            'numeral_13': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=13, fecha_ano=yearPeriodo), 
            'numeral_14': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=14, fecha_ano=yearPeriodo), 
            'numeral_14a': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=15, fecha_ano=yearPeriodo),
            'numeral_15': Modelo1.objects.filter(usuario_id=request.user.id, numeral_id=16, periodo__fechaInicio__year = yearPeriodo),
            'numeral_16':Modelo1.objects.filter(usuario_id=request.user.id, numeral_id=17, periodo__fechaInicio__year = yearPeriodo),
            'numeral_17':Modelo1.objects.filter(usuario_id=request.user.id, numeral_id=18, periodo__fechaInicio__year = yearPeriodo),
            'numeral_18':Modelo2.objects.filter(usuario_id=request.user.id, numeral_id=19, periodo__fechaInicio__year = yearPeriodo),
            'numeral_19':Modelo2.objects.filter(usuario_id=request.user.id, numeral_id=20, periodo__fechaInicio__year = yearPeriodo),
            'numeral_20':Modelo2.objects.filter(usuario_id=request.user.id, numeral_id=21, periodo__fechaInicio__year = yearPeriodo),
            'numeral_21':Modelo2.objects.filter(usuario_id=request.user.id, numeral_id=22, periodo__fechaInicio__year = yearPeriodo),
            'numeral_22':Modelo2.objects.filter(usuario_id=request.user.id, numeral_id=23, periodo__fechaInicio__year = yearPeriodo),
            'numeral_23':Modelo14.objects.filter(usuario_id=request.user.id, numeral_id=24, periodo__fechaInicio__year = yearPeriodo),
            'numeral_24':Modelo3.objects.filter(usuario_id=request.user.id, numeral_id=25, periodo__fechaInicio__year = yearPeriodo),
            'numeral_25':Modelo3.objects.filter(usuario_id=request.user.id, numeral_id=26, periodo__fechaInicio__year = yearPeriodo),
            'numeral_26':Modelo3.objects.filter(usuario_id=request.user.id, numeral_id=27, periodo__fechaInicio__year = yearPeriodo),
            'numeral_27':Modelo3.objects.filter(usuario_id=request.user.id, numeral_id=28, periodo__fechaInicio__year = yearPeriodo),
            'numeral_28':Modelo3.objects.filter(usuario_id=request.user.id, numeral_id=29, periodo__fechaInicio__year = yearPeriodo),
            'numeral_29':Modelo3.objects.filter(usuario_id=request.user.id, numeral_id=30, periodo__fechaInicio__year = yearPeriodo),
            'citas': Citas.objects.filter(usuario_id=request.user.id), #Id - 31
            'glosario': Glosario.objects.filter(seccion="I. INVESTIGACIÓN CIENTÍFICA"),
            'periodoActual': periodoActual,'periodos':periodos
        }
        return render(request, "investigadores/investigacionCientifica.html", data)

@method_decorator(login_required, name='dispatch')
class formacion_RH(View):
    
    def get(self,request):
        id1 = request.GET.get('periodoActual')
        periodoActual = Periodo.objects.get(id = id1)
        periodos = Periodo.objects.all()
        yearPeriodo = periodoActual.fechaInicio.year
        data = {
            'numeralName': Numeral.objects.filter(nombreDeSeccion="Formacion de Recursos Humanos"),
            'numeral_31': Modelo4.objects.filter(usuario_id=request.user.id, numeral_id=32, periodo__fechaInicio__year = yearPeriodo),
            'numeral_32': Modelo4.objects.filter(usuario_id=request.user.id, numeral_id=33, periodo__fechaInicio__year = yearPeriodo),
            'numeral_33': Modelo4.objects.filter(usuario_id=request.user.id, numeral_id=34, periodo__fechaInicio__year = yearPeriodo),
            'numeral_34': Modelo4.objects.filter(usuario_id=request.user.id, numeral_id=35, periodo__fechaInicio__year = yearPeriodo),
            'numeral_35': Modelo5.objects.filter(usuario_id=request.user.id, numeral_id=36, periodo__fechaInicio__year = yearPeriodo),
            'numeral_36': Modelo5.objects.filter(usuario_id=request.user.id, numeral_id=37, periodo__fechaInicio__year = yearPeriodo),
            'numeral_37': Modelo6.objects.filter(usuario_id=request.user.id, numeral_id=38, periodo__fechaInicio__year = yearPeriodo),
            'numeral_38': Modelo16.objects.filter(usuario_id=request.user.id,numeral_id=39, periodo__fechaInicio__year = yearPeriodo),
            'numeral_39': Modelo6.objects.filter(usuario_id=request.user.id, numeral_id=40, periodo__fechaInicio__year = yearPeriodo),
            "glosario": Glosario.objects.filter(seccion="II. FORMACIÓN DE RECURSOS HUMANOS"),
            "periodoActual": periodoActual,'periodos':periodos
            }
        return render(request, "investigadores/formacionRRHH.html", data)

@method_decorator(login_required, name='dispatch')
class desarrollo_tec_inovacion(View):
    
    def get(self,request):
        id1 = request.GET.get('periodoActual')
        periodoActual = Periodo.objects.get(id = id1)
        periodos = Periodo.objects.all()
        yearPeriodo = periodoActual.fechaInicio.year
        data = {
            "numeralName": Numeral.objects.filter(nombreDeSeccion="Desarrollo Tecnologico e Innovacion"), 
            'numeral_40': Modelo7.objects.filter(usuario_id=request.user.id,numeral_id=41, periodo__fechaInicio__year = yearPeriodo),
            'numeral_41': Modelo7.objects.filter(usuario_id=request.user.id,numeral_id=42, periodo__fechaInicio__year = yearPeriodo),
            'numeral_42': Modelo7.objects.filter(usuario_id=request.user.id,numeral_id=43, periodo__fechaInicio__year = yearPeriodo),
            'numeral_43': Modelo7.objects.filter(usuario_id=request.user.id,numeral_id=44, periodo__fechaInicio__year = yearPeriodo),
            'numeral_44': Modelo7.objects.filter(usuario_id=request.user.id,numeral_id=45, periodo__fechaInicio__year = yearPeriodo),
            'numeral_45': Modelo8.objects.filter(usuario_id=request.user.id,numeral_id=46, periodo__fechaInicio__year = yearPeriodo),
            'numeral_46': Modelo9.objects.filter(usuario_id=request.user.id,numeral_id=47, periodo__fechaInicio__year = yearPeriodo),
            'glosario':  Glosario.objects.filter(seccion="III. DESARROLLO TECNOLÓGICO E INNOVACIÓN(agregar patentes en REGISTRO)"),
            'periodoActual': periodoActual,'periodos':periodos
            }
        return render(request, "investigadores/desarrolloTecInnov.html", data)

@method_decorator(login_required, name='dispatch')
class apoyo_institucional(View):
    
    def get(self,request):
        id1 = request.GET.get('periodoActual')
        periodoActual = Periodo.objects.get(id = id1)
        periodos = Periodo.objects.all()
        yearPeriodo = periodoActual.fechaInicio.year
        data = {
            "numeralName": Numeral.objects.filter(nombreDeSeccion="Apoyo Institucional"),
            'numeral_47': Modelo15.objects.filter(usuario_id=request.user.id, numeral_id=48, periodo__fechaInicio__year = yearPeriodo),
            'numeral_48': Modelo9.objects.filter(usuario_id=request.user.id ,numeral_id=49, periodo__fechaInicio__year = yearPeriodo),
            'numeral_49': Modelo10.objects.filter(usuario_id=request.user.id, numeral_id=50, periodo__fechaInicio__year = yearPeriodo),
            'numeral_49a': Modelo10.objects.filter(usuario_id=request.user.id, numeral_id=51, periodo__fechaInicio__year = yearPeriodo),
            'numeral_49b': Modelo10.objects.filter(usuario_id=request.user.id, numeral_id=52, periodo__fechaInicio__year = yearPeriodo),
            'numeral_50': Modelo10.objects.filter(usuario_id=request.user.id, numeral_id=53, periodo__fechaInicio__year = yearPeriodo),
            'numeral_51': Modelo10.objects.filter(usuario_id=request.user.id, numeral_id=54, periodo__fechaInicio__year = yearPeriodo),
            'numeral_52': Modelo10.objects.filter(usuario_id=request.user.id, numeral_id=55, periodo__fechaInicio__year = yearPeriodo),
            'numeral_52a': Modelo10.objects.filter(usuario_id=request.user.id, numeral_id=56, periodo__fechaInicio__year = yearPeriodo),
            'numeral_53': Modelo11.objects.filter(usuario_id=request.user.id, numeral_id=57, periodo__fechaInicio__year = yearPeriodo),
            'numeral_54': Modelo11.objects.filter(usuario_id=request.user.id, numeral_id=58, periodo__fechaInicio__year = yearPeriodo),
            'numeral_55': Modelo11.objects.filter(usuario_id=request.user.id, numeral_id=59, periodo__fechaInicio__year = yearPeriodo),
            'numeral_56': Modelo11.objects.filter(usuario_id=request.user.id, numeral_id=60, periodo__fechaInicio__year = yearPeriodo),
            'numeral_57': Modelo15.objects.filter(usuario_id=request.user.id, numeral_id=61, periodo__fechaInicio__year = yearPeriodo),
            'numeral_58': Modelo12.objects.filter(usuario_id=request.user.id, numeral_id=62, periodo__fechaInicio__year = yearPeriodo),
            'numeral_59': Modelo13.objects.filter(usuario_id=request.user.id, numeral_id=63, periodo__fechaInicio__year = yearPeriodo),
            'numeral_60': Modelo15.objects.filter(usuario_id=request.user.id, numeral_id=64, periodo__fechaInicio__year = yearPeriodo),
            'glosario': Glosario.objects.filter(seccion="IV. APOYO INSTITUCIONAL"), 
            'periodoActual': periodoActual,'periodos':periodos
            }
        return render(request, "investigadores/apoyoInstitucional.html", data)

@method_decorator(login_required, name='dispatch')
class informacion_adicional(FormView):

    def get(self,request):
        id1 = request.GET.get('periodoActual')
        periodoActual = Periodo.objects.get(id = id1)
        periodos = Periodo.objects.all()
        yearPeriodo = periodoActual.fechaInicio.year
        data = {
            'numeralName': Numeral.objects.filter(nombreDeSeccion="Informacion Adicional"),
            'numeral_61': Modelo14.objects.filter(usuario_id=request.user.id,numeral_id=65, periodo__fechaInicio__year = yearPeriodo),
            'glosario': Glosario.objects.filter(seccion="V. INFORMACIÖN ADICIONAL"), 
            'periodoActual': periodoActual,'periodos':periodos
            }
        return render(request, "investigadores/informacionAdicional.html", data)

# Investigacion Cientifica - CRUD

# Numerales Biblioteca
@method_decorator(login_required, name='dispatch')
class actualizarBiblioteca(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        autor = request.POST.get('autores', None)
        titulo = request.POST.get('titulo', None)
        revista = request.POST.get('revista', None)
        estudiantes = request.POST.get('estudiantes', None)
        url = request.POST.get('url', None)
        doi = request.POST.get('doi', None)
        fecha = request.POST.get('fecha', None)
        bibcode = request.POST.get('bibcode', None)
        temp = len(fecha)
        fecha_ano = fecha[:temp - 3 ]
        
        # Actualizamos biblioteca
        obj = Biblioteca.objects.get(id=id1)
        obj.autores = autor
        obj.titulo = titulo
        obj.revistaPublicacion = revista
        obj.estudiantesEnArticulo = estudiantes
        obj.doi = doi
        obj.fecha = fecha
        obj.url = url
        obj.fecha_ano = fecha_ano
        obj.bibcode = bibcode
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id, 'autores': obj.autores, 'titulo': obj.titulo,
                'revista': obj.revistaPublicacion, 'estudiantes': obj.estudiantesEnArticulo}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class BibliotecaCrearNumeral(View):
    def post(self, request):
        numeral1 = request.POST.get('numeral', None)
        
        obj = Biblioteca.objects.create(
            user_id=request.user.id,
            numeral_id=numeral1
        )
        
        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorBiblioteca(View):
    def get(self,request):
        periodo_id = request.GET.get('periodo',None)
        periodo_id = int(periodo_id) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo14.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id)

        data = {
            'descripcion':datos.descripcion,
        }
        return  JsonResponse(data)
# Fin Numerales Biblioteca

# Operaciones Modelo1
@method_decorator(login_required, name='dispatch')
class actualizarModelo1(View):

    def post(self, request):
        id1 = request.POST.get('id', None)
        autores = request.POST.get('autores', None)
        titulo = request.POST.get('titulo', None)
        revista = request.POST.get('revista', None)
        url = request.POST.get('url', None)
        doi = request.POST.get('doi', None)
        fecha = request.POST.get('fecha',None)
        estudiantes = request.POST.get('estudiantes', None)

        # Actualizamos Modelo1
        obj = Modelo1.objects.get(id=id1)
        obj.autores = autores
        obj.titulo = titulo
        obj.revistaPublicacion = revista
        obj.fecha = fecha
        obj.estudiantesEnArticulo = estudiantes
        obj.doi = doi
        obj.url = url

        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        data = {'id': obj.id}  # Json que se enviara a Data

        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo1(View):
    def post(self, request):
        id1 = request.POST.get('id', None)

        obj = Modelo1.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo1.objects.get(id=id1).delete()

        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo1(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)
        
        obj = Modelo1.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )
        
        
        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo1(View):
    def get(self,request):
        periodo_id = request.GET.get('periodo',None)
        periodo_id = int(periodo_id) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo1.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id).last()

        data = {
            'descripcion':datos.descripcion,
        }
        return  JsonResponse(data)

# Operaciones Modelo2
@method_decorator(login_required, name='dispatch')
class actualizarModelo2(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        nombreProyecto = request.POST.get('nombreProyecto', None)
        descripcion = request.POST.get('descripcion', None)
        participantes = request.POST.get('participantes', None)
        responsable = request.POST.get('responsable', None)
        estudiantes = request.POST.get('estudiantes', None)

        # Actualizamos Modelo2
        obj = Modelo2.objects.get(id=id1)
        obj.nombreProyecto = nombreProyecto
        obj.descripcion = descripcion
        obj.participantes = participantes
        obj.estudiantes = estudiantes
        obj.responsableTecParticipante = responsable

        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo2(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        print(id1)

        obj = Modelo2.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo2.objects.get(id=id1).delete()

        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo2(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)
        
        obj = Modelo2.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )
        

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo2(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo2.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        nombreProyecto = []
        descripcion = []
        participantes = []
        estudiantes = []
        responsableTecParticipantes = []
        ids = []

        for d in datos:
            data = Modelo2.objects.create(
                nombreProyecto = d.nombreProyecto,
                descripcion = d.descripcion,
                participantes = d.participantes,
                estudiantes = d.estudiantes,
                responsableTecParticipante = d.responsableTecParticipante,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            nombreProyecto.append(data.nombreProyecto)
            descripcion.append(data.descripcion)
            participantes.append(data.participantes)
            estudiantes.append(data.estudiantes)
            responsableTecParticipantes.append(data.responsableTecParticipante)
            ids.append(data.id)

        data = {
            'nombreProyecto':nombreProyecto,
            'descripcion':descripcion,
            'participantes':participantes,
            'estudiantes':estudiantes,
            'responsableTecParticipantes':responsableTecParticipantes,
            'ids':ids
        }

        return  JsonResponse(data)

# Operaciones Modelo3
@method_decorator(login_required, name='dispatch')
class actualizarModelo3(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        tituloPresentacion = request.POST.get('tituloPresentacion', None)
        autores = request.POST.get('autores', None)
        nombreConferencia = request.POST.get('nombreConferencia', None)
        fecha = request.POST.get('fecha', None)
        estudiantes = request.POST.get('estudiantes', None)
        doi = request.POST.get('doi', None)
        presentacionPoster = request.POST.get('presentacionPoster', None)
        url = request.POST.get('url', None)

        # Actualizamos modelo3
        obj = Modelo3.objects.get(id=id1)
        obj.tituloPresentacion = tituloPresentacion
        obj.autores = autores
        obj.nombreConferencia = nombreConferencia
        obj.fecha = fecha
        obj.presentacionPoster = presentacionPoster
        obj.estudiantes = estudiantes
        obj.doi = doi
        obj.url = url
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo3(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo3.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo3.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo3(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)
        
        obj = Modelo3.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )
        

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo3(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo3.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        tituloPresentacion = []
        autores = []
        nombreConferencia = []
        fecha = []
        presentacionPoster = []
        estudiantes = []
        doi = []
        url = []
        ids = []

        for d in datos:
            data = Modelo3.objects.create(
                tituloPresentacion = d.tituloPresentacion,
                autores = d.autores,
                nombreConferencia = d.nombreConferencia,
                fecha = d.fecha,
                presentacionPoster = d.presentacionPoster,
                estudiantes = d.estudiantes,
                doi = d.doi,
                url = d.url,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            tituloPresentacion.append(data.tituloPresentacion)
            autores.append(data.autores)
            nombreConferencia.append(data.nombreConferencia)
            fecha.append(data.fecha)
            presentacionPoster.append(data.presentacionPoster)
            estudiantes.append(data.estudiantes)
            doi.append(data.doi)
            url.append(data.url)
            ids.append(data.id)
        
        data = {
            'tituloPresentacion':tituloPresentacion,
            'autores':autores,
            'nombreConferencia':nombreConferencia,
            'fecha':fecha,
            'presentacionPoster':presentacionPoster,
            'estudiantes':estudiantes,
            'doi':doi,
            'url':url,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarCitas(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        citas = request.POST.get('citas', None)
        citasPeriodo = request.POST.get('citasPeriodo', None)
        indiceH = request.POST.get('indiceH', None)

        obj = Citas.objects.get(id=id1)
        obj.citas = citas
        obj.citasObtenidasEnPeriodo = citasPeriodo
        obj.indiceH = indiceH
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()
        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearCitas(View):
    def get(self,request):
        numeral1 = request.GET.get('numeral', None)
        id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=id)
        
        obj = Citas.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id':obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

# Formacion RRHH - CRUD
@method_decorator(login_required, name='dispatch')
class actualizarModelo4(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        nombreCompleto = request.POST.get('nombreCompleto', None)
        tituloTesis = request.POST.get('tituloTesis', None)
        fecha = request.POST.get('fecha', None)
        url = request.POST.get('url', None)
       

        # Actualizamos modelo4
        obj = Modelo4.objects.get(id=id1)
        obj.nombreCompleto = nombreCompleto
        obj.tituloTesis = tituloTesis
        obj.fecha = fecha
        obj.url = url


        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo4(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo4.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo4.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo4(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo4.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo4(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo4.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        nombreCompleto = []
        tituloTesis = []
        fecha = []
        url = []
        ids = []

        for d in datos:
            data = Modelo4.objects.create(
                nombreCompleto = d.nombreCompleto,
                tituloTesis = d.tituloTesis,
                fecha = d.fecha,
                url = d.url,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
        
            nombreCompleto.append(data.nombreCompleto)
            tituloTesis.append(data.tituloTesis)
            fecha.append(data.fecha)
            url.append(data.url)
            ids.append(data.id)

        data = {
            'nombreCompleto': nombreCompleto,
            'tituloTesis': tituloTesis,
            'fecha': fecha,
            'url': url,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo5(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        nombreCurso = request.POST.get('nombreCurso', None)
        periodo = request.POST.get('periodo', None)
        notas = request.POST.get('notas', None)

        # Actualizamos biblioteca
        obj = Modelo5.objects.get(id=id1)
        obj.nombreCurso = nombreCurso
        obj.periodoNumeral = periodo
        obj.notas = notas

        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo5(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo5.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo5.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo5(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo5.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo5(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo5.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        nombreCurso = []
        periodoNumeral = []
        notas = []
        ids = []

        for d in datos:
            data = Modelo5.objects.create(
                nombreCurso = d.nombreCurso,
                periodoNumeral = d.periodoNumeral,
                notas = d.notas,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
        
            nombreCurso.append(data.nombreCurso)
            periodoNumeral.append(data.periodoNumeral)
            notas.append(data.notas)
            ids.append(data.id)

        data = {
            'nombreCurso':nombreCurso,
            'periodoNumeral':periodoNumeral,
            'notas':notas,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo6(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        nombre = request.POST.get('nombre', None)
        titulo = request.POST.get('tituloTesis', None)
        grado = request.POST.get('grado', None)
        institucion = request.POST.get('institucion', None)
        fecha = request.POST.get('fecha', None)
        notas = request.POST.get('notas', None)

        # Actualizamos modelo
        obj = Modelo6.objects.get(id=id1)
        obj.nombre = nombre
        obj.tituloTesis = titulo
        obj.Grado = grado
        obj.institucion = institucion
        obj.fecha = fecha
        obj.notas = notas
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo6(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo6.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo6.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo6(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)
       
        obj = Modelo6.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo6(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo6.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        nombre = []
        tituloTesis = []
        Grado = []
        institucion = []
        fecha = []
        notas = []
        ids = []

        for d in datos:
            data = Modelo6.objects.create(
                nombre = d.nombre,
                tituloTesis = d.tituloTesis,
                Grado = d.Grado,
                institucion = d.institucion,
                fecha = d.fecha,
                notas = d.notas,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            nombre.append(data.nombre)
            tituloTesis.append(data.tituloTesis)
            Grado.append(data.Grado)
            institucion.append(data.institucion)
            fecha.append(data.fecha)
            notas.append(data.notas)
            ids.append(data.id)

        data = {
            'nombre':nombre,
            'tituloTesis':tituloTesis,
            'Grado':Grado,
            'institucion':institucion,
            'fecha':fecha,
            'notas':notas,
            'ids':ids
        }
        return  JsonResponse(data)

# Desarrollo Tec. Innov. - CRUD
@method_decorator(login_required, name='dispatch')
class actualizarModelo7(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        autores = request.POST.get('autores', None)
        descripcion = request.POST.get('descripcion', None)
        url = request.POST.get('url', None)

        obj = Modelo7.objects.get(id=id1)
        obj.autores = autores
        obj.descripcion = descripcion
        obj.url = url
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo7(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo7.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo7.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo7(View):
    def get(self, request):        
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo7.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo7(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo7.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        descripcion = []
        autores = []
        url = []
        ids = []
        for d in datos:
            data = Modelo7.objects.create(
                descripcion = d.descripcion,
                autores = d.autores,
                url = d.url,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            descripcion.append(data.descripcion)
            autores.append(data.autores)
            url.append(data.url)
            ids.append(data.id)

        data = {
            'descripcion':descripcion,
            'autores':autores,
            'url':url,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo8(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        nombre = request.POST.get('nombre', None)
        descripcion = request.POST.get('descripcion', None)
        participantes = request.POST.get('participantes', None)
        financiamiento = request.POST.get('financiamiento', None)

        obj = Modelo8.objects.get(id=id1)
        obj.nombre = nombre
        obj.descripcion = descripcion
        obj.participantes = participantes
        obj.financiamiento = financiamiento
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo8(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo8.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo8.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo8(View):
    def get(self, request):        
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo8.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo8(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo8.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        nombre = []
        descripcion = []
        participantes = []
        financiamiento = []
        ids = []

        for d in datos:
            data = Modelo8.objects.create(
                nombre = d.nombre,
                descripcion = d.descripcion,
                participantes = d.participantes,
                financiamiento = d.financiamiento,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            nombre.append(data.nombre)
            descripcion.append(data.descripcion)
            participantes.append(data.participantes)
            financiamiento.append(data.financiamiento)
            ids.append(data.id)

        data = {
            'nombre':nombre,
            'descripcion':descripcion,
            'participantes':participantes,
            'financiamiento':financiamiento,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo9(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        titulo = request.POST.get('titulo', None)
        autores = request.POST.get('autores', None)
        Nreporte = request.POST.get('Nreportes', None)
        fecha = request.POST.get('fecha', None)
        url = request.POST.get('url', None)
        revista = request.POST.get('revistaPublicacion', None)
        doi = request.POST.get('doi',None)

        obj = Modelo9.objects.get(id=id1)
        obj.titulo = titulo
        obj.autores = autores
        obj.numeroReportes = Nreporte
        obj.fecha = fecha
        obj.url = url
        obj.revistaPublicacion = revista
        obj.doi = doi
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo9(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo9.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo9.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo9(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo9.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo9(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        numeral_id = request.GET.get('numeral',None)
        periodo_id = int(periodo) - 1
        datos = Modelo9.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id = numeral_id)
        titulo = []
        autores = []
        numeroReportes = []
        fecha = []
        url = []
        revistaPublicacion = []
        doi = []
        ids = []

        for d in datos:
            data = Modelo9.objects.create(
                titulo = d.titulo,
                autores = d.autores,
                numeroReportes = d.numeroReportes,
                fecha = d.fecha,
                url = d.url,
                revistaPublicacion = d.revistaPublicacion,
                doi = d.doi,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id

            )
            titulo.append(data.titulo)
            autores.append(data.autores)
            numeroReportes.append(data.numeroReportes)
            fecha.append(data.fecha)
            url.append(data.url)
            revistaPublicacion.append(data.revistaPublicacion)
            doi.append(data.doi)
            ids.append(data.id)

        data = {
            'titulo':titulo,
            'autores':autores,
            'numeroReportes':numeroReportes,
            'fecha':fecha,
            'url':url,
            'revistaPublicacion':revistaPublicacion,
            'doi':doi,
            'ids':ids
        }
        return  JsonResponse(data)

# Apoyo institucional
@method_decorator(login_required, name='dispatch')
class actualizarModelo10(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        descripcion = request.POST.get('descripcion', None)
        fecha = request.POST.get('fecha', None)
        url = request.POST.get('url', None)
        periodo = request.POST.get('periodo', None)

        obj = Modelo10.objects.get(id=id1)
        obj.descripcion = descripcion
        obj.fecha = fecha
        obj.url = url
        obj.periodoNumeral = periodo
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo10(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo10.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo10.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo10(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo10.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo10(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo10.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id = numeral_id)
        descripcion = []
        fecha = []
        url = []
        periodoNumeral = []
        ids = []

        for d in datos:
            data = Modelo10.objects.create(
                descripcion = d.descripcion,
                fecha = d.fecha,
                url = d.url,
                periodoNumeral = d.periodoNumeral,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            descripcion.append(data.descripcion)
            fecha.append(data.fecha)
            url.append(data.url)
            periodoNumeral.append(data.periodoNumeral)
            ids.append(data.id)

        data = {
            'descripcion':descripcion,
            'fecha':fecha,
            'url':url,
            'periodoNumeral':periodoNumeral,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo11(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        nombre = request.POST.get('nombreEstudiante', None)
        descripcion = request.POST.get('descripcion', None)
        fecha = request.POST.get('fecha', None)
        fechaPeriodo = request.POST.get('fechaPeriodo', None)

        obj = Modelo11.objects.get(id=id1)
        obj.nombreEstudiante = nombre
        obj.descripcion = descripcion
        obj.fecha = fecha
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo11(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo11.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo11.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo11(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo11.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo11(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo11.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id = numeral_id)
        descripcion = []
        nombreEstudiante = []
        fecha = []
        ids =  []

        for d in datos:
            data = Modelo11.objects.create(
                descripcion = d.descripcion,
                nombreEstudiante = d.nombreEstudiante,
                fecha = d.fecha,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            descripcion.append(data.descripcion)
            nombreEstudiante.append(data.nombreEstudiante)
            fecha.append(data.fecha)
            ids.append(data.id)

        data = {
            'descripcion':descripcion,
            'nombreEstudiante':nombreEstudiante,
            'fecha':fecha,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo12(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        laboratorio = request.POST.get('laboratorioTaller', None)

        obj = Modelo12.objects.get(id=id1)

        obj.laboratorioTaller = laboratorio
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo12(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo12.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo12.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo12(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)
    
        obj = Modelo12.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo12(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo12.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        laboratorioTaller = []
        ids  = []
        for d in datos:
            data = Modelo12.objects.create(
                laboratorioTaller = d.laboratorioTaller,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            laboratorioTaller.append(data.laboratorioTaller)
            ids.append(data.id)

        data = {
            'laboratorioTaller':laboratorioTaller,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo13(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        descripcion = request.POST.get('descripcion', None)
        agencia = request.POST.get('agenciasFinancieras', None)

        obj = Modelo13.objects.get(id=id1)
        obj.descripcion = descripcion
        obj.agenciasFinancieras = agencia
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo13(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo13.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo13.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo13(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo13.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo13(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo13.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        descripcion = []
        agenciasFinancieras = []
        ids = []

        for d in datos:
            data = Modelo13.objects.create(
                descripcion = d.descripcion,
                agenciasFinancieras = d.agenciasFinancieras,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            descripcion.append(data.descripcion)
            agenciasFinancieras.append(data.agenciasFinancieras)
            ids.append(data.id)

        data = {
            'descripcion':descripcion,
            'agencias':agenciasFinancieras,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo14(View):

    def post(self, request):
        id1 = request.POST.get('id', None)
        telescopio = request.POST.get('telescopio', None)
        descripcion = request.POST.get('descripcion', None)
        url = request.POST.get('url', None)
        conferenciaProyecto = request.POST.get('conferenciaProyecto',None)
        rol = request.POST.get('rol',None)
        fecha = request.POST.get('fecha',None)

        obj = Modelo14.objects.get(id=id1)
        obj.TelescopioInstrumentoInfra = telescopio
        obj.descripcion = descripcion
        obj.url = url
        obj.conferenciaProyecto = conferenciaProyecto
        obj.rol = rol
        obj.fecha = fecha
        
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + obj.anexos.url))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo14(View):
    def post(self, request):
        print("Entre a la funcion")
        id1 = request.POST.get('id', None)
        print(id1)
        Modelo14.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo14(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo14.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo14(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo14.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        telescopio = []
        descripcion = []
        rol = []
        conferencia = []
        fecha = []
        ids = []
        urls = []

        for d in datos:
            data = Modelo14.objects.create(
                descripcion = d.descripcion,
                TelescopioInstrumentoInfra = d.TelescopioInstrumentoInfra,
                url = d.url,
                rol = d.rol,
                fecha = d.fecha,
                conferenciaProyecto = d.conferenciaProyecto,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            telescopio.append(data.TelescopioInstrumentoInfra)
            descripcion.append(data.descripcion)
            rol.append(data.rol)
            conferencia.append(data.conferenciaProyecto)
            fecha.append(data.fecha)
            urls.append(data.url)
            ids.append(data.id)
            
        
        data = {
            'telescopio':telescopio,
            'descripcion':descripcion,
            'urls':urls,
            'conferenciaProyecto':conferencia,
            'rol':rol,
            'fecha':fecha,
            'ids':ids
        }
        
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo15(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        descripcion = request.POST.get('descripcion', None)

        obj = Modelo15.objects.get(id=id1)
        obj.descripcion = descripcion
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo15(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo15.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo15.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo15(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo15.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo15(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo15.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        descripcion = []
        ids = []

        for d in datos:
            data = Modelo15.objects.create(
                descripcion = d.descripcion,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            descripcion.append(data.descripcion)
            ids.append(data.id)
        data = {
            'descripcion':descripcion,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo16(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        estudiantes = request.POST.get('nombreEstudiante', None)
        coordinacion = request.POST.get('coordinacion',None)
        grado = request.POST.get('grado',None)
        
        obj = Modelo16.objects.get(id=id1)
        obj.nombreEstudiante = estudiantes
        obj.coordinacion = coordinacion
        obj.grado = grado
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexos:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
                obj.anexos = archivo
            else:
                obj.anexos = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo16(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        obj = Modelo16.objects.get(id=id1)
        if obj.anexos:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexos.name))
        Modelo16.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo16(View):
    def get(self, request):
        numeral = request.GET.get('numeral', None)
        periodo_id = request.GET.get('periodo',None)
        periodo = Periodo.objects.get(id=periodo_id)

        obj = Modelo16.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral,
            'periodo':periodo_id,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class infoAnteriorModelo16(View):
    def get(self,request):
        periodo = request.GET.get('periodo',None)
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral',None)
        datos = Modelo16.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        nombreEstudiante = []
        coordinacion = []
        grado = []
        ids = []

        for d in datos:
            data = Modelo16.objects.create(
                nombreEstudiante = d.nombreEstudiante,
                coordinacion = d.coordinacion,
                grado = d.grado,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            nombreEstudiante.append(data.nombreEstudiante)
            coordinacion.append(data.coordinacion)
            grado.append(data.grado)
            ids.append(data.id)


        data = {
            'nombreEstudiante':nombreEstudiante,
            'coordinacion':coordinacion,
            'grado':grado,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class enviarReporte(View): 
    def get(self, request, *args, **kwargs):
        periodo_id = request.GET.get('periodoActual',None)
        periodo = Periodo.objects.get(id=periodo_id)
        yearPeriodo = periodo.fechaInicio.year
        anexoModelo1 = Modelo1.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo2 = Modelo2.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo3 = Modelo3.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo4 = Modelo4.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo5 = Modelo5.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo6 = Modelo6.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo7 = Modelo7.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo8 = Modelo8.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo9 = Modelo9.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo10 = Modelo10.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo11 = Modelo11.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo12 = Modelo12.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo13 = Modelo13.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo14 = Modelo14.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo15 = Modelo15.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoModelo16 = Modelo16.objects.exclude(anexos = "").filter(usuario_id = request.user.id, periodo__fechaInicio__year = yearPeriodo)
        anexoBiblioteca = Biblioteca.objects.exclude(anexos = "").filter(user_id = request.user.id, fecha_ano=yearPeriodo)
        anexoCitas = Citas.objects.exclude(anexos = "").filter(usuario_id = request.user.id,periodo__fechaInicio__year = yearPeriodo)

        html = generarPdf(request,periodo_id)
        
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        pdf = pdfkit.from_string(html,False,configuration=config,options=options)
        periodo = Periodo.objects.get(id=periodo_id)
        periodo = periodo.nombrePeriodo
        
        data = {
            'periodo':periodo,
        }
        
        """
        #Email para investigador
        body = render_to_string(
            'investigadores/templateReportesFinalizadoUsuario.html', {
                'nombre': request.user.first_name,
                'apellido': request.user.last_name,
                'periodo':periodo,
            },
        )

        email_message = EmailMessage(
            subject='Reporte enviado a la Coordinación',
            body=body,
            from_email='reportes-astro@inaoep.mx',
            to=[request.user.email],
        )

        email_message.content_subtype = 'html'
        #Convertimos la instancia PDF en un tipo MIME para enviarlo
        adjunto = MIMEBase('application', 'octet-stream')
        adjunto.set_payload(pdf)
        encoders.encode_base64(adjunto)
        adjunto.add_header('Content-Disposition', "attachment; filename= Reporte "+periodo+'.pdf')
        email_message.attach(adjunto)
        #Enviamos email
        email_message.send()


        #Email para la coordinacion
        bodyAdmin = render_to_string(
         'investigadores/templateReporteFinalizado.html',{
             'nombre':request.user.first_name,
             'apellido': request.user.last_name,
             'periodo': periodo,
         }   
        )

        mensajeCordinacion = EmailMessage(
            subject='Reporte enviado a la Coordinación',
            body=bodyAdmin,
            from_email='reportes-astro@inaoep.mx',
            to=['alexXarellan@hotmail.com'], #Cambiar a astrofi@inaoep.mx
        )
        mensajeCordinacion.content_subtype = 'html'
        mensajeCordinacion.attach(adjunto)
        #Enviamos email
        mensajeCordinacion.send()
        """
        #Guardamos reporte en BD
        reporte,creado = ReporteEnviado.objects.get_or_create(periodo_id = periodo_id, usuario_id = request.user.id)
        
        if creado:
            data['actualizado'] = False

        else:
            data['actualizado'] = True
            if reporte.reporte:
                os.remove(os.path.join(BASE_DIR + '/media/'+reporte.reporte.name))
            if reporte.anexo:
                os.remove(os.path.join(BASE_DIR + '/media/'+reporte.anexo.name))
            
        reporte.reporte.save('Reporte '+periodo+' '+str(reporte.id)+'.pdf', ContentFile(pdf), save=False)
        print(BASE_DIR + '/media/'+'anexos_zip/anexo.zip')
        #Genera Zip con anexos
        with zipfile.ZipFile(BASE_DIR + '/media/'+'anexos_zip/anexo.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as anexoZip:
            
            for anexo in anexoModelo1:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)
            for anexo in anexoModelo2:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo3:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo4:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo5:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo6:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo7:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo8:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo9:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo10:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo11:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo12:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo13:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo14:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            for anexo in anexoModelo15:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)
            for anexo in anexoModelo16:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)
            for anexo in anexoCitas:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)
            for anexo in anexoBiblioteca:
                if anexo:
                    anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)
        anexoZip.close()

        anexoZip = open(BASE_DIR + '/media/'+'anexos_zip/anexo.zip','rb') #Corregir este error
        reporte.anexo.save("Anexo "+periodo+' '+str(reporte.id)+".zip", ContentFile(anexoZip.read()), save=False)
        reporte.save()
        #os.remove('media/anexos_zip/anexo.zip')
        
        return  JsonResponse(data)


# Generar PDF
@method_decorator(login_required, name='dispatch')
class generarReporte(View):
    def get(self,request):
        periodo_id = request.GET.get('periodo',None)

        html = generarPdf(request,periodo_id)
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        pdf = pdfkit.from_string(html,False,configuration=config,options=options)
        return HttpResponse(pdf,content_type='application/pdf')
        
    
@method_decorator(login_required, name='dispatch')
class reportesEnviados(View):
    def get(self,request):
        queryset = ReporteEnviado.objects.filter(usuario_id= request.user.id)
        return render(request,'investigadores/reportesEnviados.html',{'reportes':queryset})


@method_decorator(login_required, name='dispatch')
class descargarReporteEnviado(View):
    def get(self, request, pdf):
        #Reporte maestro:
        reporte = Reporte(request)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=reporte %s.docx' %(self.periodo.nombrePeriodo)
        reporte.save(response)


@method_decorator(login_required, name='dispatch')
class home(TemplateView):
    template_name = 'investigadores/home.html'


@method_decorator(login_required, name='dispatch')
class perfil(TemplateView):
    template_name = 'registration/profile_form.html'


@method_decorator(login_required, name='dispatch')
class ampliarSesion(View):
    def get(self, request):
        sesion_expiry = request.session.set_expiry(600)
        sesion = request.session.get_expiry_date()

        timeNow = datetime.datetime.now() + datetime.timedelta(minutes=10)
        hora = timeNow.hour
        minutos = timeNow.minute
        nuevaSesion = str(hora) + ":" + str(minutos)
    
        data = {
            'nuevaSesion': nuevaSesion
        }
        return JsonResponse(data)