# Redirecciones
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.core import serializers
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
from apps.registration.models import User
from apps.biblioteca.models import Biblioteca
from .models import ReporteEnviado
from django.http import JsonResponse
#Forms
from .forms import num61
# Manejo Archivos
import os
from django.conf import settings
from django.core.files.base import ContentFile
#Zip
import zipfile
#PDF 
import pdfkit
#config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  #Linux
config =  pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe') #Windows
# Correo
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from email.mime.base import MIMEBase
from email import encoders
from sistema_reportes.settings import BASE_DIR
#Reporte final
from .generarReporteCoordinacion import generarPdf
#Time zone
import datetime
#serializer 
    
@method_decorator(login_required, name='dispatch')
class reporte_productividad(View):
    def get(self,request):
        periodoActual =  Periodo.objects.last()
        periodos = Periodo.objects.all()
        data = {
            'periodoActual': periodoActual,'periodos':periodos
        }
        return render(request, 'reportes/reportes_productividad.html',data)

@method_decorator(login_required, name='dispatch')
class investigacion_cientifica(View):

    def get(self,request):
        id1 = request.GET.get('periodoActual')
        id_usuario = request.user.id
        periodoActual = Periodo.objects.get(id = id1)
        periodos = Periodo.objects.all()
        yearPeriodo = periodoActual.fecha_inicio.year
        data = {
            "numeralName": Numeral.objects.filter(nombre_seccion="Investigacion Cientifica"),
            'numeral_1': Biblioteca.objects.reporteProductividad(id_usuario,1,yearPeriodo),
            'numeral_2': Biblioteca.objects.reporteProductividad(id_usuario,2,yearPeriodo), 
            'numeral_3': Biblioteca.objects.reporteProductividad(id_usuario,3,yearPeriodo),
            'numeral_4': Biblioteca.objects.reporteProductividad(id_usuario,4,yearPeriodo),
            'numeral_5': Biblioteca.objects.reporteProductividad(id_usuario,5,yearPeriodo), 
            'numeral_6': Modelo1.objects.reporteProductividad(id_usuario,6,yearPeriodo),
            'numeral_7': Biblioteca.objects.reporteProductividad(id_usuario,7,yearPeriodo), 
            'numeral_8': Modelo1.objects.reporteProductividad(id_usuario,8,yearPeriodo),
            'numeral_9': Biblioteca.objects.reporteProductividad(id_usuario,9,yearPeriodo),
            "numeral_10": Modelo1.objects.reporteProductividad(id_usuario,10,yearPeriodo),
            'numeral_11': Biblioteca.objects.reporteProductividad(id_usuario,11,yearPeriodo), 
            'numeral_12': Biblioteca.objects.reporteProductividad(id_usuario,12,yearPeriodo),
            'numeral_13': Biblioteca.objects.reporteProductividad(id_usuario,13,yearPeriodo), 
            'numeral_14': Biblioteca.objects.reporteProductividad(id_usuario,14,yearPeriodo), 
            'numeral_14a': Biblioteca.objects.reporteProductividad(id_usuario,15,yearPeriodo),
            'numeral_15':Modelo1.objects.reporteProductividad(id_usuario,16,yearPeriodo),
            'numeral_16':Modelo1.objects.reporteProductividad(id_usuario,17,yearPeriodo),
            'numeral_17':Modelo1.objects.reporteProductividad(id_usuario,18,yearPeriodo),
            'numeral_18':Modelo2.objects.reporteProductividad(id_usuario, 19,yearPeriodo),
            'numeral_19':Modelo2.objects.reporteProductividad(id_usuario, 20,yearPeriodo),
            'numeral_20':Modelo2.objects.reporteProductividad(id_usuario, 21,yearPeriodo),
            'numeral_21':Modelo2.objects.reporteProductividad(id_usuario, 22,yearPeriodo),
            'numeral_22':Modelo2.objects.reporteProductividad(id_usuario, 23,yearPeriodo),
            'numeral_23':Modelo14.objects.reporteProductividad(id_usuario,24,yearPeriodo),
            'numeral_24':Modelo3.objects.reporteProductividad(id_usuario, 25,yearPeriodo),
            'numeral_25':Modelo3.objects.reporteProductividad(id_usuario, 26,yearPeriodo),
            'numeral_26':Modelo3.objects.reporteProductividad(id_usuario, 27,yearPeriodo),
            'numeral_27':Modelo3.objects.reporteProductividad(id_usuario, 28,yearPeriodo),
            'numeral_28':Modelo3.objects.reporteProductividad(id_usuario, 29,yearPeriodo),
            'numeral_29':Modelo3.objects.reporteProductividad(id_usuario, 30,yearPeriodo),
            'citas': Citas.objects.reporteProductividad(id_usuario), #Id - 31
            'glosario': Glosario.objects.reporteProductividad("I. INVESTIGACIÓN CIENTÍFICA"),
            'periodoActual': periodoActual,'periodos':periodos
        }
        return render(request, "reportes/investigacionCientifica.html", data)

@method_decorator(login_required, name='dispatch')
class formacion_RH(View):
    
    def get(self,request):
        id1 = request.GET.get('periodoActual')
        id_usuario = request.user.id
        periodoActual = Periodo.objects.get(id = id1)
        periodos = Periodo.objects.all()
        yearPeriodo = periodoActual.fecha_inicio.year
        data = {
            'numeralName': Numeral.objects.filter(nombre_seccion="Formacion de Recursos Humanos"),
            'numeral_31': Modelo4.objects.reporteProductividad(id_usuario,32,yearPeriodo),
            'numeral_32': Modelo4.objects.reporteProductividad(id_usuario,33,yearPeriodo),
            'numeral_33': Modelo4.objects.reporteProductividad(id_usuario,34,yearPeriodo),
            'numeral_34': Modelo4.objects.reporteProductividad(id_usuario,35,yearPeriodo),
            'numeral_35': Modelo5.objects.reporteProductividad(id_usuario,36,yearPeriodo),
            'numeral_36': Modelo5.objects.reporteProductividad(id_usuario,37,yearPeriodo),
            'numeral_37': Modelo6.objects.reporteProductividad(id_usuario,38,yearPeriodo),
            'numeral_38': Modelo16.objects.reporteProductividad(id_usuario,39,yearPeriodo),
            'numeral_39': Modelo6.objects.reporteProductividad(id_usuario,40,yearPeriodo),
            "glosario": Glosario.objects.reporteProductividad("II. FORMACIÓN DE RECURSOS HUMANOS"),
            "periodoActual": periodoActual,'periodos':periodos
            }
        return render(request, "reportes/formacionRRHH.html", data)

@method_decorator(login_required, name='dispatch')
class desarrollo_tec_inovacion(View):
    
    def get(self,request):
        id1 = request.GET.get('periodoActual')
        id_usuario = request.user.id
        periodoActual = Periodo.objects.get(id = id1)
        periodos = Periodo.objects.all()
        yearPeriodo = periodoActual.fecha_inicio.year
        data = {
            "numeralName": Numeral.objects.filter(nombre_seccion="Desarrollo Tecnologico e Innovacion"), 
            'numeral_40': Modelo7.objects.reporteProductividad(id_usuario,41,yearPeriodo),
            'numeral_41': Modelo7.objects.reporteProductividad(id_usuario,42,yearPeriodo),
            'numeral_42': Modelo7.objects.reporteProductividad(id_usuario,43,yearPeriodo),
            'numeral_43': Modelo7.objects.reporteProductividad(id_usuario,44,yearPeriodo),
            'numeral_44': Modelo7.objects.reporteProductividad(id_usuario,45,yearPeriodo),
            'numeral_45': Modelo8.objects.reporteProductividad(id_usuario,46,yearPeriodo),
            'numeral_46': Modelo9.objects.reporteProductividad(id_usuario,47,yearPeriodo),
            'glosario':  Glosario.objects.reporteProductividad("III. DESARROLLO TECNOLÓGICO E INNOVACIÓN(agregar patentes en REGISTRO)"),
            'periodoActual': periodoActual,'periodos':periodos
            }
        return render(request, "reportes/desarrolloTecInnov.html", data)

@method_decorator(login_required, name='dispatch')
class apoyo_institucional(View):
    
    def get(self,request):
        id1 = request.GET.get('periodoActual')
        id_usuario = request.user.id
        periodoActual = Periodo.objects.get(id = id1)
        periodos = Periodo.objects.all()
        yearPeriodo = periodoActual.fecha_inicio.year
        data = {
            "numeralName": Numeral.objects.filter(nombre_seccion="Apoyo Institucional"),
            'numeral_47': Modelo15.objects.reporteProductividad(id_usuario,48,yearPeriodo),
            'numeral_48': Modelo9.objects.reporteProductividad(id_usuario ,49,yearPeriodo),
            'numeral_49': Modelo10.objects.reporteProductividad(id_usuario,50,yearPeriodo),
            'numeral_49a': Modelo10.objects.reporteProductividad(id_usuario,51,yearPeriodo),
            'numeral_49b': Modelo10.objects.reporteProductividad(id_usuario,52,yearPeriodo),
            'numeral_50': Modelo10.objects.reporteProductividad(id_usuario,53,yearPeriodo),
            'numeral_51': Modelo10.objects.reporteProductividad(id_usuario,54,yearPeriodo),
            'numeral_52': Modelo10.objects.reporteProductividad(id_usuario,55,yearPeriodo),
            'numeral_52a': Modelo10.objects.reporteProductividad(id_usuario,56,yearPeriodo),
            'numeral_53': Modelo11.objects.reporteProductividad(id_usuario,57,yearPeriodo),
            'numeral_54': Modelo11.objects.reporteProductividad(id_usuario,58,yearPeriodo),
            'numeral_55': Modelo11.objects.reporteProductividad(id_usuario,59,yearPeriodo),
            'numeral_56': Modelo11.objects.reporteProductividad(id_usuario,60,yearPeriodo),
            'numeral_57': Modelo15.objects.reporteProductividad(id_usuario,61,yearPeriodo),
            'numeral_58': Modelo12.objects.reporteProductividad(id_usuario,62,yearPeriodo),
            'numeral_59': Modelo13.objects.reporteProductividad(id_usuario,63,yearPeriodo),
            'numeral_60': Modelo15.objects.reporteProductividad(id_usuario,64,yearPeriodo),
            'glosario': Glosario.objects.reporteProductividad("IV. APOYO INSTITUCIONAL"), 
            'periodoActual': periodoActual,'periodos':periodos
            }
        return render(request, "reportes/apoyoInstitucional.html", data)

@method_decorator(login_required, name='dispatch')
class informacion_adicional(View):
    def get(self,request):
        id_usuario = request.user.id
        id1 = request.GET.get('periodoActual')
        periodoActual = Periodo.objects.get(id = id1)
        periodos = Periodo.objects.all()
        yearPeriodo = periodoActual.fecha_inicio.year
        data = {
            'numeralName': Numeral.objects.filter(nombre_seccion="Informacion Adicional"),
            'numeral_61': Modelo14.objects.reporteProductividad(id_usuario,65,yearPeriodo),
            'glosario': Glosario.objects.reporteProductividad("V. INFORMACIÖN ADICIONAL"), 
            'periodoActual': periodoActual,'periodos':periodos,
            'num61': num61
            }

        return render(request, "reportes/informacionAdicional.html", data)

# Investigacion Cientifica - CRUD
class prueba(View):
    def get(self,request):
        print(request.GET)
        telescopio = request.GET.get('id_telescopio')
        anexo = request.GET.get('anexo')
        print(anexo)
        print(type(anexo))
        print(telescopio)
        return JsonResponse({'a':'da'})

# Numerales Biblioteca
@method_decorator(login_required, name='dispatch')
class actualizarBiblioteca(View):
    def post(self, request):
        id1 = request.POST.get('id')
        autor = request.POST.get('autores','')
        titulo = request.POST.get('titulo','')
        revista = request.POST.get('revista','')
        estudiantes = request.POST.get('estudiantes','')
        url = request.POST.get('url','')
        doi = request.POST.get('doi','')
        fecha = request.POST.get('fecha','')
        bibcode = request.POST.get('bibcode','')
        temp = len(fecha)
        fecha_ano = fecha[:temp - 3 ]
        
        # Actualizamos biblioteca
        obj = Biblioteca.objects.get(id=id1)
        obj.autores = autor
        obj.titulo = titulo
        obj.revista_publicacion = revista
        obj.estudiantes_en_articulo = estudiantes
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
                'revista': obj.revista_publicacion, 'estudiantes': obj.estudiantes_en_articulo}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class BibliotecaCrearNumeral(View):
    def post(self, request):
        numeral1 = request.POST.get('numeral')
        
        obj = Biblioteca.objects.create(
            usuario_id=request.user.id,
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
        id1 = request.POST.get('id')
        autores = request.POST.get('autores','')
        titulo = request.POST.get('titulo','')
        revista = request.POST.get('revista','')
        url = request.POST.get('url','')
        doi = request.POST.get('doi','')
        fecha = request.POST.get('fecha','')
        estudiantes = request.POST.get('estudiantes','')

        # Actualizamos Modelo1
        obj = Modelo1.objects.get(id=id1)
        obj.autores = autores
        obj.titulo = titulo
        obj.revista_publicacion = revista
        obj.fecha = fecha
        obj.estudiantes_en_articulo = estudiantes
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
        id1 = request.POST.get('id')

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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo1.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        autores = []
        fecha = []
        titulo = []
        revista_publicacion = []
        url = []
        estudiantes_en_articulo = []
        doi = []
        ids = []

        for d in datos:
            data = Modelo1.objects.create(
                autores = d.autores,
                fecha = d.fecha,
                titulo = d.titulo,
                revista_publicacion = d.revista_publicacion,
                url = d.url,
                estudiantes_en_articulo = d.estudiantes_en_articulo,
                doi = d.doi,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            autores.append(data.autores)
            fecha.append(data.fecha)
            titulo.append(data.titulo)
            revista_publicacion.append(data.revista_publicacion)
            url.append(data.url)
            estudiantes_en_articulo.append(data.estudiantes_en_articulo)
            doi.append(data.doi)
            ids.append(data.id)

        data = {
            'autores':autores,
            'fecha': fecha,
            'titulo': titulo,
            'revista_publicacion': revista_publicacion,
            'url': url,
            'estudiantes_en_articulo': estudiantes_en_articulo,
            'doi': doi,
            'ids':ids,
        }
        return  JsonResponse(data)

# Operaciones Modelo2
@method_decorator(login_required, name='dispatch')
class actualizarModelo2(View):
    def post(self, request):
        # Actualizamos Modelo2
        obj = Modelo2.objects.get(id=request.POST.get('id'))

        obj.nombre_del_proyecto = request.POST.get('nombre_del_proyecto','')
        obj.descripcion = request.POST.get('descripcion','')
        obj.participantes = request.POST.get('participantes','')
        obj.estudiantes = request.POST.get('estudiantes','')
        obj.rol = request.POST.get('responsable','')

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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo2.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        nombre_del_proyecto = []
        descripcion = []
        participantes = []
        estudiantes = []
        rols = []
        ids = []

        for d in datos:
            data = Modelo2.objects.create(
                nombre_del_proyecto = d.nombre_del_proyecto,
                descripcion = d.descripcion,
                participantes = d.participantes,
                estudiantes = d.estudiantes,
                rol = d.rol,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            nombre_del_proyecto.append(data.nombre_del_proyecto)
            descripcion.append(data.descripcion)
            participantes.append(data.participantes)
            estudiantes.append(data.estudiantes)
            rols.append(data.rol)
            ids.append(data.id)

        data = {
            'nombre_del_proyecto':nombre_del_proyecto,
            'descripcion':descripcion,
            'participantes':participantes,
            'estudiantes':estudiantes,
            'rols':rols,
            'ids':ids
        }

        return  JsonResponse(data)

# Operaciones Modelo3
@method_decorator(login_required, name='dispatch')
class actualizarModelo3(View):
    def post(self, request):
        id1 = request.POST.get('id')
        titulo = request.POST.get('titulo','')
        autores = request.POST.get('autores','')
        nombre_de_conferencia = request.POST.get('nombre_de_conferencia','')
        fecha = request.POST.get('fecha','')
        estudiantes = request.POST.get('estudiantes','')
        doi = request.POST.get('doi','')
        tipo = request.POST.get('tipo','')
        url = request.POST.get('url','')

        # Actualizamos modelo3
        obj = Modelo3.objects.get(id=id1)
        obj.titulo = titulo
        obj.autores = autores
        obj.nombre_de_conferencia = nombre_de_conferencia
        obj.fecha = fecha
        obj.tipo = tipo
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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo3.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        titulo = []
        autores = []
        nombre_de_conferencia = []
        fecha = []
        tipo = []
        estudiantes = []
        doi = []
        url = []
        ids = []

        for d in datos:
            data = Modelo3.objects.create(
                titulo = d.titulo,
                autores = d.autores,
                nombre_de_conferencia = d.nombre_de_conferencia,
                fecha = d.fecha,
                tipo = d.tipo,
                estudiantes = d.estudiantes,
                doi = d.doi,
                url = d.url,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            titulo.append(data.titulo)
            autores.append(data.autores)
            nombre_de_conferencia.append(data.nombre_de_conferencia)
            fecha.append(data.fecha)
            tipo.append(data.tipo)
            estudiantes.append(data.estudiantes)
            doi.append(data.doi)
            url.append(data.url)
            ids.append(data.id)
        
        data = {
            'titulo':titulo,
            'autores':autores,
            'nombre_de_conferencia':nombre_de_conferencia,
            'fecha':fecha,
            'tipo':tipo,
            'estudiantes':estudiantes,
            'doi':doi,
            'url':url,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarCitas(View):
    def post(self, request):
        id1 = request.POST.get('id')
        citas = request.POST.get('citas')
        citas_en_periodo = request.POST.get('citas_en_periodo')
        indiceH = request.POST.get('indiceH')

        obj = Citas.objects.get(id=id1)
        obj.citas = citas
        obj.citas_en_periodo = citas_en_periodo
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
        numeral1 = request.GET.get('numeral')
        id = request.GET.get('periodo')
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
        id1 = request.POST.get('id')
        nombre_completo = request.POST.get('nombre_completo','')
        titulo_de_tesis = request.POST.get('titulo_de_tesis','')
        fecha = request.POST.get('fecha','')
        url = request.POST.get('url','')
       

        # Actualizamos modelo4
        obj = Modelo4.objects.get(id=id1)
        obj.nombre_completo = nombre_completo
        obj.titulo_de_tesis = titulo_de_tesis
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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo4.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        nombre_completo = []
        titulo_de_tesis = []
        fecha = []
        url = []
        ids = []

        for d in datos:
            data = Modelo4.objects.create(
                nombre_completo = d.nombre_completo,
                titulo_de_tesis = d.titulo_de_tesis,
                fecha = d.fecha,
                url = d.url,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
        
            nombre_completo.append(data.nombre_completo)
            titulo_de_tesis.append(data.titulo_de_tesis)
            fecha.append(data.fecha)
            url.append(data.url)
            ids.append(data.id)

        data = {
            'nombre_completo': nombre_completo,
            'titulo_de_tesis': titulo_de_tesis,
            'fecha': fecha,
            'url': url,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo5(View):
    def post(self, request):
        id1 = request.POST.get('id')
        nombre_del_curso = request.POST.get('nombre_del_curso','')
        periodo = request.POST.get('periodo','')
        notas = request.POST.get('notas','')

        # Actualizamos biblioteca
        obj = Modelo5.objects.get(id=id1)
        obj.nombre_del_curso = nombre_del_curso
        obj.periodo_numeral = periodo
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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo5.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        nombre_del_curso = []
        periodo_numeral = []
        notas = []
        ids = []

        for d in datos:
            data = Modelo5.objects.create(
                nombre_del_curso = d.nombre_del_curso,
                periodo_numeral = d.periodo_numeral,
                notas = d.notas,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
        
            nombre_del_curso.append(data.nombre_del_curso)
            periodo_numeral.append(data.periodo_numeral)
            notas.append(data.notas)
            ids.append(data.id)

        data = {
            'nombre_del_curso':nombre_del_curso,
            'periodo_numeral':periodo_numeral,
            'notas':notas,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo6(View):
    def post(self, request):
        id1 = request.POST.get('id')
        nombre = request.POST.get('nombre','')
        titulo = request.POST.get('titulo_de_tesis','')
        grado = request.POST.get('grado','')
        institucion = request.POST.get('institucion','')
        fecha = request.POST.get('fecha','')
        notas = request.POST.get('notas','')

        # Actualizamos modelo
        obj = Modelo6.objects.get(id=id1)
        obj.nombre = nombre
        obj.titulo_de_tesis = titulo
        obj.grado = grado
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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo6.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id,numeral_id=numeral_id)
        nombre = []
        titulo_de_tesis = []
        grado = []
        institucion = []
        fecha = []
        notas = []
        ids = []

        for d in datos:
            data = Modelo6.objects.create(
                nombre = d.nombre,
                titulo_de_tesis = d.titulo_de_tesis,
                grado = d.grado,
                institucion = d.institucion,
                fecha = d.fecha,
                notas = d.notas,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            nombre.append(data.nombre)
            titulo_de_tesis.append(data.titulo_de_tesis)
            grado.append(data.grado)
            institucion.append(data.institucion)
            fecha.append(data.fecha)
            notas.append(data.notas)
            ids.append(data.id)

        data = {
            'nombre':nombre,
            'titulo_de_tesis':titulo_de_tesis,
            'grado':grado,
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
        id1 = request.POST.get('id')
        autores = request.POST.get('autores','')
        descripcion = request.POST.get('descripcion','')
        url = request.POST.get('url','')

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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
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
        id1 = request.POST.get('id')
        nombre = request.POST.get('nombre','')
        descripcion = request.POST.get('descripcion','')
        participantes = request.POST.get('participantes','')
        financiamiento = request.POST.get('financiamiento','')

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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
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
        id1 = request.POST.get('id')
        titulo = request.POST.get('titulo','')
        autores = request.POST.get('autores','')
        Nreporte = request.POST.get('Nreportes','')
        fecha = request.POST.get('fecha','')
        url = request.POST.get('url','')
        revista = request.POST.get('revista_publicacion','')
        doi = request.POST.get('doi','')

        obj = Modelo9.objects.get(id=id1)
        obj.titulo = titulo
        obj.autores = autores
        obj.numero_reportes = Nreporte
        obj.fecha = fecha
        obj.url = url
        obj.revista_publicacion = revista
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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        numeral_id = request.GET.get('numeral')
        periodo_id = int(periodo) - 1
        datos = Modelo9.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id = numeral_id)
        titulo = []
        autores = []
        numero_reportes = []
        fecha = []
        url = []
        revista_publicacion = []
        doi = []
        ids = []

        for d in datos:
            data = Modelo9.objects.create(
                titulo = d.titulo,
                autores = d.autores,
                numero_reportes = d.numero_reportes,
                fecha = d.fecha,
                url = d.url,
                revista_publicacion = d.revista_publicacion,
                doi = d.doi,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id

            )
            titulo.append(data.titulo)
            autores.append(data.autores)
            numero_reportes.append(data.numero_reportes)
            fecha.append(data.fecha)
            url.append(data.url)
            revista_publicacion.append(data.revista_publicacion)
            doi.append(data.doi)
            ids.append(data.id)

        data = {
            'titulo':titulo,
            'autores':autores,
            'numero_reportes':numero_reportes,
            'fecha':fecha,
            'url':url,
            'revista_publicacion':revista_publicacion,
            'doi':doi,
            'ids':ids
        }
        return  JsonResponse(data)

# Apoyo institucional
@method_decorator(login_required, name='dispatch')
class actualizarModelo10(View):
    def post(self, request):
        id1 = request.POST.get('id')
        descripcion = request.POST.get('descripcion','')
        fecha = request.POST.get('fecha','')
        url = request.POST.get('url','')
        periodo = request.POST.get('periodo','')

        obj = Modelo10.objects.get(id=id1)
        obj.descripcion = descripcion
        obj.fecha = fecha
        obj.url = url
        obj.periodo_numeral = periodo
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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo10.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id = numeral_id)
        descripcion = []
        fecha = []
        url = []
        periodo_numeral = []
        ids = []

        for d in datos:
            data = Modelo10.objects.create(
                descripcion = d.descripcion,
                fecha = d.fecha,
                url = d.url,
                periodo_numeral = d.periodo_numeral,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            descripcion.append(data.descripcion)
            fecha.append(data.fecha)
            url.append(data.url)
            periodo_numeral.append(data.periodo_numeral)
            ids.append(data.id)

        data = {
            'descripcion':descripcion,
            'fecha':fecha,
            'url':url,
            'periodo_numeral':periodo_numeral,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo11(View):
    def post(self, request):
        id1 = request.POST.get('id')
        nombre = request.POST.get('nombre_del_estudiante','')
        descripcion = request.POST.get('descripcion','')
        fecha = request.POST.get('fecha','')
        fechaPeriodo = request.POST.get('fechaPeriodo','')

        obj = Modelo11.objects.get(id=id1)
        obj.nombre_del_estudiante = nombre
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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo11.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id = numeral_id)
        descripcion = []
        nombre_del_estudiante = []
        fecha = []
        ids =  []

        for d in datos:
            data = Modelo11.objects.create(
                descripcion = d.descripcion,
                nombre_del_estudiante = d.nombre_del_estudiante,
                fecha = d.fecha,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            descripcion.append(data.descripcion)
            nombre_del_estudiante.append(data.nombre_del_estudiante)
            fecha.append(data.fecha)
            ids.append(data.id)

        data = {
            'descripcion':descripcion,
            'nombre_del_estudiante':nombre_del_estudiante,
            'fecha':fecha,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo12(View):
    def post(self, request):
        id1 = request.POST.get('id')
        laboratorio = request.POST.get('laboratorio_taller','')

        obj = Modelo12.objects.get(id=id1)

        obj.laboratorio_taller = laboratorio
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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo12.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        laboratorio_taller = []
        ids  = []
        for d in datos:
            data = Modelo12.objects.create(
                laboratorio_taller = d.laboratorio_taller,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            laboratorio_taller.append(data.laboratorio_taller)
            ids.append(data.id)

        data = {
            'laboratorio_taller':laboratorio_taller,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo13(View):
    def post(self, request):
        id1 = request.POST.get('id')
        descripcion = request.POST.get('descripcion','')
        agencia = request.POST.get('agencias_financieras','')

        obj = Modelo13.objects.get(id=id1)
        obj.descripcion = descripcion
        obj.agencias_financieras = agencia
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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo13.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        descripcion = []
        agencias_financieras = []
        ids = []

        for d in datos:
            data = Modelo13.objects.create(
                descripcion = d.descripcion,
                agencias_financieras = d.agencias_financieras,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            descripcion.append(data.descripcion)
            agencias_financieras.append(data.agencias_financieras)
            ids.append(data.id)

        data = {
            'descripcion':descripcion,
            'agencias':agencias_financieras,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo14(View):

    def post(self, request):
        id1 = request.POST.get('id')
        telescopio = request.POST.get('telescopio','')
        descripcion = request.POST.get('descripcion','')
        url = request.POST.get('url','')
        conferencia_proyecto = request.POST.get('conferencia_proyecto','')
        rol = request.POST.get('rol','')
        fecha = request.POST.get('fecha','')

        obj = Modelo14.objects.get(id=id1)
        obj.telescopio_instrumento_infra = telescopio
        obj.descripcion = descripcion
        obj.url = url
        obj.conferencia_proyecto = conferencia_proyecto
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
        id1 = request.POST.get('id')
        Modelo14.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class crearModelo14(View):
    def get(self, request):

        #Create
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')     
        #Validate update or create
        
        obj = Modelo14.objects.create(
            usuario_id=request.user.id,
            numeral_id=numeral,
            periodo_id=periodo_id,
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
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
                telescopio_instrumento_infra = d.telescopio_instrumento_infra,
                url = d.url,
                rol = d.rol,
                fecha = d.fecha,
                conferencia_proyecto = d.conferencia_proyecto,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )
            telescopio.append(data.telescopio_instrumento_infra)
            descripcion.append(data.descripcion)
            rol.append(data.rol)
            conferencia.append(data.conferencia_proyecto)
            fecha.append(data.fecha)
            urls.append(data.url)
            ids.append(data.id)
            
        
        data = {
            'telescopio':telescopio,
            'descripcion':descripcion,
            'urls':urls,
            'conferencia_proyecto':conferencia,
            'rol':rol,
            'fecha':fecha,
            'ids':ids
        }
        
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class actualizarModelo15(View):
    def post(self, request):
        id1 = request.POST.get('id')
        descripcion = request.POST.get('descripcion','')

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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
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
        id1 = request.POST.get('id')
        estudiantes = request.POST.get('nombre_del_estudiante','')
        coordinacion = request.POST.get('coordinacion','')
        grado = request.POST.get('grado','')
        
        obj = Modelo16.objects.get(id=id1)
        obj.nombre_del_estudiante = estudiantes
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
        id1 = request.POST.get('id')
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
        numeral = request.GET.get('numeral')
        periodo_id = request.GET.get('periodo')
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
        periodo = request.GET.get('periodo')
        periodo_id = int(periodo) - 1
        numeral_id = request.GET.get('numeral')
        datos = Modelo16.objects.filter(periodo_id = periodo_id, usuario_id = request.user.id, numeral_id=numeral_id)
        nombre_del_estudiante = []
        coordinacion = []
        grado = []
        ids = []

        for d in datos:
            data = Modelo16.objects.create(
                nombre_del_estudiante = d.nombre_del_estudiante,
                coordinacion = d.coordinacion,
                grado = d.grado,
                numeral_id = numeral_id,
                periodo_id = periodo,
                usuario_id = request.user.id
            )

            nombre_del_estudiante.append(data.nombre_del_estudiante)
            coordinacion.append(data.coordinacion)
            grado.append(data.grado)
            ids.append(data.id)


        data = {
            'nombre_del_estudiante':nombre_del_estudiante,
            'coordinacion':coordinacion,
            'grado':grado,
            'ids':ids
        }
        return  JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class enviarReporte(View): 
    def get(self, request, *args, **kwargs):
        #Declaramos variables para filtos y nombres
        periodo_id = request.GET.get('periodoActual')
        periodo = Periodo.objects.get(id=periodo_id)
        usuario = request.user.id
        yearPeriodo = periodo.fecha_inicio.year

        #Hacemos conexion conn la BD para obtener los anexos de cada nuemral del usuario y del periodo(año)
        anexoModelo1 = Modelo1.objects.anexosModelo1(usuario,yearPeriodo)
        anexoModelo2 = Modelo2.objects.anexosModelo2(usuario,yearPeriodo)
        anexoModelo3 = Modelo3.objects.anexosModelo3(usuario,yearPeriodo)
        anexoModelo4 = Modelo4.objects.anexosModelo4(usuario,yearPeriodo)
        anexoModelo5 = Modelo5.objects.anexosModelo5(usuario,yearPeriodo)
        anexoModelo6 = Modelo6.objects.anexosModelo6(usuario,yearPeriodo)
        anexoModelo7 = Modelo7.objects.anexosModelo7(usuario,yearPeriodo)
        anexoModelo8 = Modelo8.objects.anexosModelo8(usuario,yearPeriodo)
        anexoModelo9 = Modelo9.objects.anexosModelo9(usuario,yearPeriodo)
        anexoModelo10 = Modelo10.objects.anexosModelo10(usuario,yearPeriodo)
        anexoModelo11 = Modelo11.objects.anexosModelo11(usuario,yearPeriodo)
        anexoModelo12 = Modelo12.objects.anexosModelo12(usuario,yearPeriodo)
        anexoModelo13 = Modelo13.objects.anexosModelo13(usuario,yearPeriodo)
        anexoModelo14 = Modelo14.objects.anexosModelo14(usuario,yearPeriodo)
        anexoModelo15 = Modelo15.objects.anexosModelo15(usuario,yearPeriodo)
        anexoModelo16 = Modelo16.objects.anexosModelo16(usuario,yearPeriodo)
        anexoBiblioteca = Biblioteca.objects.anexosBiblioteca(usuario,yearPeriodo)
        anexoCitas = Citas.objects.anexosCitas(usuario)

        #Mandamos a llamar a la funcion que genera el PDF.
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
        data = {'periodo':periodo.nombre_periodo,}
        
        """
        #Email para investigador
        body = render_to_string(
            'reportes/templateReportesFinalizadoUsuario.html', {
                'nombre': request.user.nombre,
                'apellido': request.user.apellido,
                'periodo':periodo.nombre_periodo,
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
        adjunto.add_header('Content-Disposition', "attachment; filename= Reporte "+periodo.nombre_periodo+'.pdf')
        email_message.attach(adjunto)
        #Enviamos email
        email_message.send()


        #Email para la coordinacionP
        bodyAdmin = render_to_string(
         'reportes/templateReporteFinalizado.html',{
             'nombre':request.user.nombre,
             'apellido': request.user.apellido,
             'periodo': periodo.nombre_periodo,
         }   
        )

        mensajeCordinacion = EmailMessage(
            subject='Reporte enviado a la Coordinación',
            body=bodyAdmin,
            from_email='reportes-astro@inaoep.mx',
            to=['reportes-astro@inaoep.mx'], #agregar a  'astrofi@inaoep.mx',
        )
        mensajeCordinacion.content_subtype = 'html'
        mensajeCordinacion.attach(adjunto)
        #Enviamos email
        mensajeCordinacion.send()
        """
        #creamos o actualizamos reporte en BD
        obj,creado = ReporteEnviado.objects.get_or_create(periodo_id = periodo_id, usuario_id = request.user.id)
        
        if creado:
            data['actualizado'] = False

        else:
            data['actualizado'] = True
            if obj.reporte:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.reporte.name))
            if obj.anexo:
                os.remove(os.path.join(BASE_DIR + '/media/'+obj.anexo.name))
            
        obj.reporte.save('Reporte '+periodo.nombre_periodo+' '+str(obj.id)+'.pdf', ContentFile(pdf), save=False)

        #Genera Zip con anexos
        with zipfile.ZipFile(BASE_DIR + '/media/'+'anexos_zip/anexo.zip', mode='w', compression=zipfile.ZIP_DEFLATED) as anexoZip:
            
            for anexo in anexoModelo1:
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)
            
            for anexo in anexoModelo2:
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo3:
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo4:        
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo5:        
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo6:
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
        
            for anexo in anexoModelo7:
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo8:
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo9:   
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo10:    
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo11:
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo12:        
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo13:        
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo14:        
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)            
            
            for anexo in anexoModelo15:
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)
            
            for anexo in anexoModelo16:        
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)
            
            for anexo in anexoCitas:        
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)
            
            for anexo in anexoBiblioteca:        
                anexoZip.write(BASE_DIR + '/media/'+ anexo.anexos.name, anexo.anexos.name)
        
        anexoZip.close()

        anexoZip = open(BASE_DIR + '/media/'+'anexos_zip/anexo.zip','rb') #Corregir este error
        obj.anexo.save("Anexo "+periodo.nombre_periodo+' '+str(obj.id)+".zip", ContentFile(anexoZip.read()), save=False)
        obj.save()
        
        return  JsonResponse(data)


# Generar PDF
@method_decorator(login_required, name='dispatch')
class generarReporte(View):
    def post(self,request):
        periodo_id = request.POST.get('periodo')
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
        pdf  = pdfkit.from_string(html,False,configuration=config,options=options)
        return HttpResponse(pdf,content_type='application/pdf')
        
    
@method_decorator(login_required, name='dispatch')
class reportesEnviados(View):
    def get(self,request):
        queryset = ReporteEnviado.objects.filter(usuario_id= request.user.id)
        return render(request,'reportes/reportesEnviados.html',{'reportes':queryset})

@method_decorator(login_required, name='dispatch')
class home(TemplateView):
    template_name = 'reportes/home.html'


@method_decorator(login_required, name='dispatch')
class perfil(TemplateView):
    template_name = 'registration/profile_form.html'


@method_decorator(login_required, name='dispatch')
class ampliarSesion(View):
    def get(self, request):
        request.session.set_expiry(600)
        request.session.get_expiry_date()

        timeNow = datetime.datetime.now() + datetime.timedelta(minutes=10)
        hora = timeNow.hour
        minutos = timeNow.minute
        nuevaSesion = str(hora) + ":" + str(minutos)
    
        data = {
            'nuevaSesion': nuevaSesion
        }
        return JsonResponse(data)
