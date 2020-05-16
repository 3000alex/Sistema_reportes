# Vistas
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
# mensajes
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.mail import send_mail
# Modelos y forms
from apps.registration.models import User
from apps.reportes.models import Modelo1, Modelo2, Modelo3, Modelo4, Modelo5, Modelo6, Modelo7, Modelo8, Modelo9, Modelo10, Modelo11, Modelo12, Modelo13, Modelo14, Modelo15
from apps.reportes.models import ReporteEnviado,Periodo,Numeral
from apps.reportes.models import Citas
from apps.biblioteca.models import Biblioteca
# Diversos
from django.http import JsonResponse
from django.urls import reverse, reverse_lazy
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
# Correo
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
from django.contrib.auth.hashers import check_password #Comprobar password
from django.core import serializers
#Archivo zip
import os
import zipfile
from io import StringIO
import json
#Reporte maestro
from apps.administradores.reporteMaestro import Reporte
#Reportes adms


class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('reportes:home'))
        return super(StaffRequiredMixin, self).dispatch(request, *args, **kwargs)


class UsuariosListado(StaffRequiredMixin, ListView):
    model = User  # Llamamos a la clase Users que es la que contiene nuestros usuarios
    template_name = "administradores/investigadores.html"
    context_object_name = 'users'


class UsuariosEditar(StaffRequiredMixin, View):
    def get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)  # Nombre(s) investigador
        apellido1 = request.GET.get('lastName', None)
        nombreCorto1 = request.GET.get('nombreCorto',None)
        email1 = request.GET.get('email', None)  # Email Investigador

        obj = User.objects.get(id=id1)
        obj.nombre = name1
        obj.apellido = apellido1
        obj.nombreCorto = nombreCorto1
        obj.email = email1  # correo y usuario es el mismo
        obj.save()
        user = {'id': obj.id, 'nombreCorto': obj.nombreCorto,
                'name': obj.nombre, 'apellido': obj.apellido, 'email': obj.email}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)


class UsuarioAgregar(StaffRequiredMixin, View):
    def post(self, request):
        email1 = request.POST.get('email', None)
        nombre1 = request.POST.get('nombre', None)
        lastName1 = request.POST.get('apellido', None)
        password1 =  get_random_string(length=20)
        nombreCorto1 = request.POST.get('nombreCorto',None)
        periodos = Periodo.objects.all()
        # Crear objeto
        userNew = User.objects.create_user(email=email1, password=password1, nombre=nombre1, apellido=lastName1, nombreCorto=nombreCorto1)
        
        Citas.objects.create(
            numeral_id = 31,  usuario_id = userNew.id
        )

        body = render_to_string(
            'administradores/templateBienvenida.html', {
                'nombre': userNew.nombre,
                'apellido': userNew.apellido,
                'password': password1,
                'correo': userNew.email,
            },
        )

        email_message = EmailMessage(
            subject='Bienvenido(a) al Sistema de Reportes de Astrofísica',
            body=body,
            from_email='reportes-astro@inaoep.mx',
            to=[userNew.email],
        )
        email_message.content_subtype = 'html'
        email_message.send()

        user = {'id': userNew.id, 'nombreCorto':userNew.nombreCorto,
                'nombre': userNew.nombre, 'apellido': userNew.apellido, 'email': userNew.email}

        data = { 'user': user}
        return JsonResponse(data)


class UsuariosEliminar(StaffRequiredMixin, View):

    def post(self, request):
        id1 = request.POST.get('id', None)
        User.objects.get(id=id1).delete()
        data = {
            'deleted': True,
        }

        return JsonResponse(data)

class correoBienvenida(StaffRequiredMixin, View):
    def post(self, request):
        id1 = request.POST.get('id',None)
        obj = User.objects.get(id=id1)
        password = get_random_string(length=20)
        obj.set_password(password)
        obj.save()
        
        body = render_to_string(
            'administradores/templateBienvenida.html', {
                'nombre': obj.nombre,
                'apellido': obj.apellido,
                'password': password,
                'correo': obj.email,
            },
        )

        email_message = EmailMessage(
            subject='Bienvenido(a) al Sistema de Reportes de Astrofísica',
            body=body,
            from_email='reportes-astro@inaoep.mx',
            to=[obj.email],
        )
        email_message.content_subtype = 'html'
        email_message.send()

        data = {
            'nombre':obj.nombre,
            'apellido':obj.apellido,
        }

        return JsonResponse(data)


class home_adm(StaffRequiredMixin, TemplateView):
    template_name = 'administradores/home_adm.html'


class perfil_adm(StaffRequiredMixin, View):
    
    def get(self,request):
        perfil = User.objects.get(id=request.user.id)
        data = {'perfil':perfil}
        return render(request,'administradores/perfil_adm.html',data)
    
    def post(self,request):
        correoAlternativo = request.POST.get('correoAlternativo',None)
        obj = User.objects.get(id = request.user.id)
        obj.correoAlternativo = correoAlternativo
        obj.save()
        data = {'cambio':True}
        return JsonResponse(data)


class reportes_adm(StaffRequiredMixin,View):
    def get(self, request):

        periodos = Periodo.objects.all()
        periodoActual = Periodo.objects.last()

        reportes = ReporteEnviado.objects.filter(periodo_id=periodoActual)
        data = {
            'periodos':periodos,
            'periodoActual':periodoActual,
            'reportes':reportes,
        }
        return render(request,'administradores/reportes_adm.html', data)
    
    def post(self,request):
        periodos = Periodo.objects.all()
        periodo_id = request.POST.get('periodo_id',None)
        periodoActual = Periodo.objects.get(id=periodo_id)

        reportes = ReporteEnviado.objects.filter(periodo_id=periodoActual)
        data = {
            'periodos':periodos,
            'periodoActual':periodoActual,
            'reportes':reportes,
        }
        return render(request,'administradores/reportes_adm.html', data)

    
class reporteMaestro(View):

    def post(self, request):
        periodo_id = request.POST.get('periodoActual',None)
        periodoActual = Periodo.objects.get(id=periodo_id)
        #Reporte maestro:
        reporte = Reporte(request,periodo_id)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=Reporte Maestro %s.docx' %(periodoActual.nombre_periodo)
        reporte.save(response)
        
        return response