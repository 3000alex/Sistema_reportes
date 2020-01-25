from django.shortcuts import render
from django.contrib.auth import authenticate,login
from django.urls import reverse
from django.contrib.messages.views import SuccessMessageMixin 
from registration.models import User
from django.views.generic import View
from django.http import JsonResponse
from django.http import HttpResponseRedirect
# Create your views here.
def login_view(request):
    if request.user.is_authenticated:
            if request.user.email == 'astrofi@inaoep.mx':#if para redirigir a perfil administrador
                return render(request,"administradores/home_adm.html")
            else:#else para redirigir a perfil investigador
                return render(request,"investigadores/home.html")
    else:#else para redirigir a loguearse
        context = {}
        if request.method == "POST":
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request, username=username, password=password)
                if user:
                   #user.is_authenticated
                   login(request,user)
                   
                   if user.email == 'astrofi@inaoep.mx':
                        return HttpResponseRedirect(reverse('administradores:home-adm'))
                   else:
                       return HttpResponseRedirect(reverse('investigadores:home'))
                else:
                    context["error"] = '<div class="alert alert-danger" role="alert"><ul><li>Por favor, introduzca un nombre de usuario y clave correctos. Observe que ambos campos pueden ser sensibles a mayúsculas.</li></ul></div>'
                    return render(request,"registration/login.html",context)
        else:
            return render(request,"registration/login.html",context)

class ProfileUpdate(View):
   
    def get(self,request):
        perfil = User.objects.get(id=request.user.id)
        data = {'perfil':perfil}
        return render(request,'registration/perfil.html',data)

    def post(self,request):
        obj = User.objects.get(id=request.user.id)
        nombre = request.POST.get('nombres',obj.first_name)
        apellidos = request.POST.get('apellidos',obj.last_name)
        correo = request.POST.get('correo',obj.email)
        categoria = request.POST.get('categoria',obj.categoria)
        nivel_sni = request.POST.get('nivel_sni',obj.nivelSni)
        orcid = request.POST.get('orc_id',obj.orcId)
        arxiv_id = request.POST.get('arxiv_id',obj.arxivId)
        
        
        obj.first_name = nombre
        obj.last_name = apellidos
        obj.email = correo
        obj.categoria = categoria
        obj.nivelSni = nivel_sni
        obj.orcId = orcid
        obj.arxivId = arxiv_id
        obj.save()


        data= {
            'id':obj.id   
        }
        return JsonResponse(data)