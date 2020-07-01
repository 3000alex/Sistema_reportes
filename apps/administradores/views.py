# Vistas
from django.views.generic import View,TemplateView,ListView
# Modelos y forms
from apps.registration.models import User
from apps.reportes.models import ReporteEnviado,Periodo,Numeral,Citas
# Diversos
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils.crypto import get_random_string
# Correo
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.shortcuts import render
#Reporte maestro
from apps.administradores.reporteMaestro import Reporte


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
       
        data = {'id': obj.id, 'nombreCorto': obj.nombreCorto,
                'name': obj.nombre, 'apellido': obj.apellido, 'email': obj.email}  # Json que se enviara a Data

        return JsonResponse(data)

class UsuarioAgregar(StaffRequiredMixin, View):
    def post(self, request):
        email1 = request.POST.get('email')
        nombre1 = request.POST.get('nombre')
        lastName1 = request.POST.get('apellido')
        password1 =  get_random_string(length=20)
        nombreCorto1 = request.POST.get('nombreCorto')
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
            to=[userNew.email],#,'reportes-astro@inaoep.mx'],
        )
        email_message.content_subtype = 'html'
        email_message.send()

        data = {'id': userNew.id, 'nombreCorto':userNew.nombreCorto,
                'nombre': userNew.nombre, 'apellido': userNew.apellido, 'email': userNew.email}

        return JsonResponse(data)

class UsuariosEliminar(StaffRequiredMixin, View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        print(id1)
        User.objects.get(id=id1).delete()
        data = {'deleted': True,}

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
            to=[obj.email,'reportes-astro@inaoep.mx'],
        )
        email_message.content_subtype = 'html'
        email_message.send()

        data = {
            'nombre':obj.nombre,
            'apellido':obj.apellido,
        }

        return JsonResponse(data)

class home_adm(StaffRequiredMixin, TemplateView):
    template_name = 'administradores/home.html'

class perfil_adm(StaffRequiredMixin, View):
    
    def get(self,request):
        perfil = User.objects.get(id=request.user.id)
        data = {'perfil':perfil}
        return render(request,'administradores/perfil.html',data)
    
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
        periodoActual =  periodos.last()
        periodos = periodos.order_by("-fecha_inicio")[:2]

        reportes = ReporteEnviado.objects.filter(periodo_id=periodoActual)
        data = {
            'periodos':periodos,
            'periodoActual':periodoActual,
            'reportes':reportes,
        }
        return render(request,'administradores/reportes_adm.html', data)
    
class tabla_reportes(StaffRequiredMixin, View):
    def post(self,request):
        id1 = request.POST.get('periodoActual')
        periodoActual = Periodo.objects.get(id = id1)

        reportes = ReporteEnviado.objects.filter(periodo_id=periodoActual)
        data = {
            'periodoActual':periodoActual,
            'reportes':reportes,
        }
        return render(request,'administradores/tablaReportes.html', data)

class reporteMaestro(StaffRequiredMixin,View):

    def post(self, request):
        periodo_id = request.POST.get('periodoActual',None)
        periodoActual = Periodo.objects.get(id=periodo_id)
        #Reporte maestro:
        reporte = Reporte(request,periodo_id)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        response['Content-Disposition'] = 'attachment; filename=Reporte Maestro %s.docx' %(periodoActual.nombre_periodo)
        reporte.save(response)
        
        return response