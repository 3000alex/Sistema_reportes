# Redirecciones
from django.urls import reverse
from django.shortcuts import render
from django.http import HttpResponse
# Vistas genericas
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic import View, ListView
# Librerias para validar el login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# Modelos y forms
from .models import Numeral, Citas, ReporteEnviado, Modelo1, Modelo2, Modelo3, Modelo4, Modelo5, Modelo6, Modelo7, Modelo8, Modelo9, Modelo10, Glosario
from .models import Modelo11, Modelo12, Modelo13, Modelo14, Modelo15,Modelo16, Periodo
from registration.models import User
from biblioteca.models import Biblioteca
from .models import ReporteEnviado
from datetime import date
from datetime import datetime
from django.http import JsonResponse
# Manejo Archivos
from django.shortcuts import redirect
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
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
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#Reporte final
from .generarReporteCoordinacion import generarPdf
periodo = Periodo.objects.last()
periodo = Periodo.objects.get(id=1)

@method_decorator(login_required, name='dispatch')
class investigacion_cientifica(View):
    def get(self, request):
        
        periodoActual = Periodo.objects.last()
        periodoActual = Periodo.objects.get(id=1)
        yearPeriodo = periodoActual.fechaInicio.year
        monthPeriodoInicio = periodoActual.fechaInicio.month
        monthPeriodoFin = periodoActual.fechaFin.month
        data = {
            "numeralName": Numeral.objects.filter(nombreDeSeccion="Investigacion Cientifica"),
            'numeral_1': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=1, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]),
            'numeral_2': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=2, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]), 
            'numeral_3': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=3, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]),
            'numeral_4': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=4, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]),
            'numeral_5': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=5, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]), 
            'numeral_6': Modelo1.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=6),
            'numeral_7': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=7, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]), 
            'numeral_8': Modelo1.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=8),
            'numeral_9': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=9, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]),
            "numeral_10": Modelo1.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=10),
            'numeral_11': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=11, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]), 
            'numeral_12': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=12, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]),
            'numeral_13': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=13, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]), 
            'numeral_14': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=14, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]), 
            'numeral_14a': Biblioteca.objects.filter(user_id=request.user.id, numeral_id=15, fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]),
            'numeral_15': Modelo1.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=16),
            'numeral_16':Modelo1.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=17),
            'numeral_17':Modelo1.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=18),
            'numeral_18':Modelo2.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=19),
            'numeral_19':Modelo2.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=20),
            'numeral_20':Modelo2.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=21),
            'numeral_21':Modelo2.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=22),
            'numeral_22':Modelo2.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=23),
            'numeral_23':Modelo1.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=24),
            'numeral_24':Modelo3.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=25),
            'numeral_25':Modelo3.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=26),
            'numeral_26':Modelo3.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=27),
            'numeral_27':Modelo3.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=28),
            'numeral_28':Modelo3.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=29),
            'numeral_29':Modelo3.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=30),
            'citas': Citas.objects.filter(usuario_id=request.user.id, periodo=periodoActual), #Id - 31
            'glosario': Glosario.objects.filter(seccion="I. INVESTIGACIÓN CIENTÍFICA"),
            'periodoActual': periodoActual
        }
        return render(request, "investigadores/investigacionCientifica.html", data)


@method_decorator(login_required, name='dispatch')
class formacion_RH(View):
    def get(self, request):
        periodoActual = Periodo.objects.last()
        periodoActual = Periodo.objects.get(id=1)
        data = {
            'numeralName': Numeral.objects.filter(nombreDeSeccion="Formacion de Recursos Humanos"),
            'numeral_31': Modelo4.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=32),
            'numeral_32': Modelo4.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=33),
            'numeral_33': Modelo4.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=34),
            'numeral_34': Modelo4.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=35),
            'numeral_35': Modelo5.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=36),
            'numeral_36': Modelo5.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=37),
            'numeral_37': Modelo6.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=38),
            'numeral_38': Modelo16.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=39),
            'numeral_39': Modelo6.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=40),
            "glosario": Glosario.objects.filter(seccion="II. FORMACIÓN DE RECURSOS HUMANOS"),
            "periodoActual": periodoActual
            }
        return render(request, "investigadores/formacionRRHH.html", data)


@method_decorator(login_required, name='dispatch')
class desarrollo_tec_inovacion(View):
    def get(self, request):
        periodoActual = Periodo.objects.last()
        periodoActual = Periodo.objects.get(id=1)
        data = {
            "numeralName": Numeral.objects.filter(nombreDeSeccion="Desarrollo Tecnologico e Innovacion"), 
            'numeral_40': Modelo7.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=41),
            'numeral_41': Modelo7.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=42),
            'numeral_42': Modelo7.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=43),
            'numeral_43': Modelo7.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=44),
            'numeral_44': Modelo7.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=45),
            'numeral_45': Modelo8.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=46),
            'numeral_46': Modelo9.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=47),
            'glosario':  Glosario.objects.filter(seccion="III. DESARROLLO TECNOLÓGICO E INNOVACIÓN(agregar patentes en REGISTRO)"),
            'periodoActual': periodoActual
            }
        return render(request, "investigadores/desarrolloTecInnov.html", data)

@method_decorator(login_required, name='dispatch')
class apoyo_institucional(View):
    def get(self, request):
        periodoActual = Periodo.objects.last()
        periodoActual = Periodo.objects.get(id=1)
        data = {
            "numeralName": Numeral.objects.filter(nombreDeSeccion="Apoyo Institucional"),
            'numeral_47': Modelo15.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=48),
            'numeral_48': Modelo9.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=49),
            'numeral_49': Modelo10.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=50),
            'numeral_49a': Modelo10.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=51),
            'numeral_49b': Modelo10.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=52),
            'numeral_50': Modelo10.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=53),
            'numeral_51': Modelo10.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=54),
            'numeral_52': Modelo10.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=55),
            'numeral_52a': Modelo10.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=56),
            'numeral_53': Modelo11.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=57),
            'numeral_54': Modelo11.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=58),
            'numeral_55': Modelo11.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=59),
            'numeral_56': Modelo11.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=60),
            'numeral_57': Modelo15.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=61),
            'numeral_58': Modelo12.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=62),
            'numeral_59': Modelo13.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=63),
            'numeral_60': Modelo15.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=64),
            'glosario': Glosario.objects.filter(seccion="IV. APOYO INSTITUCIONAL"), 
            'periodoActual': periodoActual
            }
        return render(request, "investigadores/apoyoInstitucional.html", data)


@method_decorator(login_required, name='dispatch')
class informacion_adicional(View):
    def get(self, request):
        periodoActual = Periodo.objects.last()
        periodoActual = Periodo.objects.get(id=1)
        data = {
            'numeralName': Numeral.objects.filter(nombreDeSeccion="Informacion Adicional"),
            'numeral_61': Modelo14.objects.filter(usuario_id=request.user.id, periodo=periodoActual,numeral_id=65),
            'glosario': Glosario.objects.filter(seccion="V. INFORMACIÖN ADICIONAL"), 
            'periodoActual': periodoActual
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

        # Actualizamos biblioteca
        obj = Biblioteca.objects.get(id=id1)
        obj.autores = autor
        obj.titulo = titulo
        obj.revista_Publicacion = revista
        obj.estudiantesEnArticulo = estudiantes
        obj.doi = doi
        obj.fecha = datetime.strptime(fecha, "%Y/%m")
        obj.url = url
        obj.bibcode = bibcode
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
        obj.save()

        user = {'id': obj.id, 'autores': obj.autores, 'titulo': obj.titulo,
                'revista': obj.revista_Publicacion, 'estudiantes': obj.estudiantesEnArticulo}  # Json que se enviara a Data

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
        estudiantes = request.POST.get('estudiantes', None)

        # Actualizamos Modelo1
        obj = Modelo1.objects.get(id=id1)
        obj.autores = autores
        obj.titulo = titulo
        obj.revistaPublicacion = revista
        obj.estudiantesEnArticulo = estudiantes
        obj.doi = doi
        obj.url = url

        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
        obj.save()

        data = {'id': obj.id}  # Json que se enviara a Data

        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo1(View):
    def post(self, request):
        id1 = request.POST.get('id', None)

        obj = Modelo1.objects.get(id=id1)
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo1.objects.get(id=id1).delete()

        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo1(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)
        obj = Modelo1.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )
        
        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo2.objects.get(id=id1).delete()

        data = {
            'deleted': True
        }
        return JsonResponse(data)


@method_decorator(login_required, name='dispatch')
class crearModelo2(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo2.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo3.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo3(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo3.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
        obj.save()
        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo4.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo4(View):
    def get(self, request):

        numeral1 = request.GET.get('numeral', None)

        obj = Modelo4.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo5.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo5(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo5.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo6.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo6(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)
       
        obj = Modelo6.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo7.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo7(View):
    def get(self, request):        
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo7.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo8(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        nombre = request.POST.get('nombre', None)
        descripcion = request.POST.get('descripcion', None)
        participantes = request.POST.get('participantes', None)
        url = request.POST.get('url', None)

        obj = Modelo8.objects.get(id=id1)
        obj.nombre = nombre
        obj.descripcion = descripcion
        obj.participantes = participantes
        obj.url = url
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo8.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo8(View):
    def get(self, request):        
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo8.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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

        obj = Modelo9.objects.get(id=id1)
        obj.titulo = titulo
        obj.autores = autores
        obj.numeroReportes = Nreporte
        obj.fecha = fecha
        obj.url = url
        obj.revistaPublicacion = revista
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo9.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo9(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo9.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo10.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo10(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo10.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo11.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo11(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo11.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo12.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo12(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)
    
        obj = Modelo12.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo13.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo13(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo13.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo14(View):

    def post(self, request):
        id1 = request.POST.get('id', None)
        telescopio = request.POST.get('telescopio', None)
        descripcion = request.POST.get('descripcion', None)
        participantes = request.POST.get('participantes', None)

        obj = Modelo14.objects.get(id=id1)
        obj.TelescopioInstrumentoInfra = telescopio
        obj.descripcion = descripcion
        obj.participantes = participantes
        #obj.anexoPdf = archivo
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + obj.anexoPdf.url))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
        obj.save()

        user = {'id': obj.id}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminarModelo14(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        Modelo14.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo14(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo14.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

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
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo15.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo15(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo15.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo16(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        estudiantes = request.POST.get('nombreEstudiante', None)

        obj = Modelo16.objects.get(id=id1)
        obj.nombreEstudiante = estudiantes
        # Subir archivos
        if request.FILES:
            archivo = request.FILES['anexo']
            if obj.anexoPdf:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
                obj.anexoPdf = archivo
            else:
                obj.anexoPdf = archivo
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
        if obj.anexoPdf:
            os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexoPdf.name))
        Modelo16.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo16(View):
    def get(self, request):
        numeral1 = request.GET.get('numeral', None)

        obj = Modelo16.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral1,
            periodo_id=periodo.id,
        )

        data = {
            'id': obj.id,
            'numeral': numeral1,
        }
        return JsonResponse(data)

class enviarReporte(View):
    def get(self, request, *args, **kwargs):
        periodo = Periodo.objects.last()

        html = generarPdf(request)
        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'no-outline': None
        }
        pdf = pdfkit.from_string(html,'reporte.pdf',configuration=config,options=options)
        with open('reporte.pdf', 'r', encoding="utf8") as archivo:
            reportePDF = archivo

        reporteFinal = ReporteEnviado.objects.create( periodo_id=periodo.id, usuario_id=request.user.id)
        
        
        archivo = reportesEnviados.objects.get(id = reporteFinal.id)
        archivo.reporte = archivo 
        #reporteFinal.save()
        archivo.save()

        return HttpResponse(pdf,content_type='application/pdf')

# Generar PDF
@method_decorator(login_required, name='dispatch')
class generarReporte(View):
    def get(self,request):
        html = generarPdf(request)
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
class reportesEnviados(ListView):
    model = ReporteEnviado
    template_name = 'investigadores/reportesEnviados.html'
    context_object_name = 'reportes'


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

        data = {
            'sesion': sesion
        }
        return JsonResponse(data)
