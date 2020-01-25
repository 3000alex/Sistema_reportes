# Vistas
from django.views.generic import ListView
from django.views.generic import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
# mensajes
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.mail import send_mail
# Modelos y forms
from registration.models import User
from .forms import RegisterForm, CorreoAlternativo
from investigadores.models import Modelo1, Modelo2, Modelo3, Modelo4, Modelo5, Modelo6, Modelo7, Modelo8, Modelo9, Modelo10, Modelo11, Modelo12, Modelo13, Modelo14, Modelo15
from investigadores.models import ReporteEnviado,Periodo,Numeral
from investigadores.models import Citas
from biblioteca.models import Biblioteca
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
from administradores.reporteMaestro import Reporte


class StaffRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            return redirect(reverse_lazy('investigadores:home'))
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
        obj.first_name = name1
        obj.last_name = apellido1
        obj.username = email1
        obj.nombreCorto = nombreCorto1
        obj.email = email1  # correo y usuario es el mismo
        obj.save()
        user = {'id': obj.id, 'username': obj.username, 'nombreCorto': obj.nombreCorto,
                'name': obj.first_name, 'last_name': obj.last_name, 'email': obj.email}  # Json que se enviara a Data

        data = {
            'user': user  # Objeto de Json con los datos actualizados.
        }
        return JsonResponse(data)


class UsuarioAgregar(StaffRequiredMixin, View):
    def post(self, request):
        email1 = request.POST.get('email', None)
        username1 = request.POST.get('email', None)
        first_name1 = request.POST.get('nombre', None)
        lastName1 = request.POST.get('apellido', None)
        password1 = get_random_string(length=20)
        nombreCorto1 = request.POST.get('nombreCorto',None)
        correoInstitucional = 'reportes-astro@inaoep.mx'
        # Crear objeto
        userNew = User.objects.create_user(
            username=username1, email=email1, password=password1, first_name=first_name1, last_name=lastName1, nombreCorto=nombreCorto1)


        user = {'id': userNew.id, 'name': userNew.username, 'nombreCorto':userNew.nombreCorto,
                'first_name': userNew.first_name, 'last_name': userNew.last_name, 'email': userNew.email}

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
        print()
        
        body = render_to_string(
            'administradores/templateBienvenida.html', {
                'nombre': obj.first_name,
                'apellido': obj.last_name,
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
            'nombre':obj.first_name,
            'apellido':obj.last_name,
        }

        return JsonResponse(data)


class home_adm(StaffRequiredMixin, TemplateView):
    template_name = 'administradores/home_adm.html'


class perfil_adm(StaffRequiredMixin, SuccessMessageMixin, UpdateView):
    
    form_class = CorreoAlternativo
    template_name = 'administradores/perfil_adm.html'
    success_url = reverse_lazy('administradores:home-adm')
    success_message = '<div class="alert alert-success" role="alert"><strong>Perfil actualizado correctamente</strong></div>'

    def get_object(self):
        user, created = User.objects.get_or_create(
            id=self.request.user.id)
        return user


class reportes_adm(StaffRequiredMixin, View):
    
    def get(self,request):
        periodo = Periodo.objects.all()
        
        ultimoPeriodo = Periodo.objects.last()
        reporte = ReporteEnviado.objects.filter(periodo_id=ultimoPeriodo)
        usuarios = User.objects.all()
        data = {
            'periodo':periodo,
            'ultimoPeriodo':ultimoPeriodo,
            'reportes':reporte,
            'usuarios':usuarios,
        }
        return render(request,'administradores/reportes_adm.html', data)
    
    def post(self,request):
        periodo = request.POST.get('periodo',None)
        reporteSerialize = serializers.serialize('json',ReporteEnviado.objects.filter(periodo_id=periodo), fields=('reporte','anexo','fechaCreacion','periodo_id','usuario_id'))
        usuariosSerialize = serializers.serialize('json',User.objects.all(), fields=('first_name','last_name'))

        data = {
            periodo,
            reporteSerialize,
            usuariosSerialize
        }

        return HttpResponse(data, content_type='application/json')

class reporteMaestro(View):

    periodo = Periodo.objects.last()

    def get(self, request):

        #Reporte maestro:
        reporte = Reporte(request)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=Reporte Maestro %s.docx' %(self.periodo.nombrePeriodo)
        reporte.save(response)
        
        return response
