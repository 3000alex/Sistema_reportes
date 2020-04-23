from django.shortcuts import render
import django.http.request
import ads
#Librerias para validar el login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
##
from .models import Biblioteca
from django.views.generic.base import TemplateView
from django.views.generic import ListView, View
from django.http import JsonResponse
from django.urls import reverse
from django.http import HttpResponse
from django.shortcuts import redirect
from django.template import loader, Context
from apps.registration.models import User
from datetime import date
from datetime import datetime
from django.contrib import messages
# Create your views here.

@method_decorator(login_required, name='dispatch')
class biblioteca_personal(ListView):
    def get(self,request):

        biblioteca = Biblioteca.objects.filter(user_id=request.user.id)
        return render(request, "biblioteca/biblioteca_personal.html", {"biblioteca": biblioteca})

@method_decorator(login_required, name='dispatch')
class busqueda_biblioteca(ListView):

    def get(self,request):
        user = User.objects.get(id=request.user.id)   
        return render(request,"biblioteca/busqueda_biblioteca.html",{"user":user})

@method_decorator(login_required, name='dispatch')
class editar_biblioteca(View):

    def post(self, request):    
        id1 = request.POST.get('id')
        obj = Biblioteca.objects.get(id=id1)
        estudiantesEnArticulo1 = request.POST.get('estudiantesEnArticulo', obj.estudiantesEnArticulo)  # Contador (Front - end)
        numeral1 = request.POST.get('numeral',obj.numeral_id) #Numeral relacionado con articulo
        
        if numeral1 == "":
            
            obj.estudiantesEnArticulo = estudiantesEnArticulo1
            numeral = ""
            obj.save()
        else:
            obj.estudiantesEnArticulo = estudiantesEnArticulo1
            obj.numeral_id = numeral1
            obj.save()
            numeral = str(obj.numeral)

          
        data = {'id': obj.id, 'estudiantesEnArticulo':obj.estudiantesEnArticulo,'numeral':numeral}

        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminar_biblioteca(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        
        Biblioteca.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class publicaciones_generales(View):
    def post(self,request):
        # Obtenemos valores de busqueda
        query = request.POST.get('author')

         # determinamos nuestro token de busqueda
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7'
        # traemoes el modelo de biblioteca para validar si esta en biblioteca o no.j
        articulos = Biblioteca.objects.filter(user_id=request.user.id)

        data =  list(ads.SearchQuery(q=query,fl='title,year,bibcode,author',rows=1000))  # Buscar por autor

        return render(request, 'biblioteca/publicaciones.html', {'data': data, 'articulos': articulos})

@method_decorator(login_required, name='dispatch')       
class publicaciones_bidcode(View):
    def post(self,request):
        query_bidcode = request.POST.get('bibcode')
        # determinamos nuestro token de busqueda
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7'
        data = list(ads.SearchQuery(bibcode=query_bidcode,fl='title,year,bibcode,author',rows=1000))  # Buscar por bidcode
        articulos = Biblioteca.objects.filter(user_id=request.user.id) # Filtramos articulos para validar si existen en la biblioteca
        # Pasamos como 3 parametro un diccionario (json) con el contenido
        return render(request, 'biblioteca/publicaciones.html', {'data': data, 'articulos': articulos})

@method_decorator(login_required, name='dispatch')
class publicaciones_orcid(View):
    def post(self,request):
        query_orcid = request.POST.get('orcid')
        # determinamos nuestro token de busqueda
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7'
        data = list(ads.SearchQuery(orcid=query_orcid,fl='title,year,bibcode,author',rows=1000))  # Buscar por orcid
        articulos = Biblioteca.objects.filter(user_id=request.user.id)

        # Pasamos como 3 parametro un diccionario (json) con el contenido
        return render(request, 'biblioteca/publicaciones.html', {'data': data, 'articulos': articulos})

@method_decorator(login_required, name='dispatch')
class agregar_biblioteca(View):
    def post(self,request):
        #Obtenemos valores de bidcodes a buscar
        bibcodes = request.POST.getlist("seleccion[]") #Obtenemos bibcodes seleccionados en el template publicacones
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7' #Configuramos el token de ADS para las consultas
        articulos = Biblioteca.objects.filter(user_id = request.user.id)  #Obtenemos articulos guardados en base de datos
        consulta = [] #Se almacenan los bibcodes que no estan duplicados en la BD y que se agregaran a biblioteca
        bibcodesBD = []

        for a in articulos:
            bibcodesBD.append(a.bibcode)

        for b in bibcodes:
            if b not in bibcodesBD:
                consulta.append(b)
        
        for bibcode in consulta:
            data = ads.SearchQuery(bibcode=bibcode,fl='title,pubdate,author,doi,page,volume,pub',rows=1000)

            for dato in data:
                #Iteramos el titulo y lo agregamos al arreglo que tiene los titulos
                
                titulo = dato.title[0]
                bibcode = bibcode  # Agregamos al arreglo el bibcode correspondiente al articulo
                revista = dato.pub  # Agregamos al arreglo la revista donde fue publicada correspondiente al articulo
                volumen = dato.volume  # Agregamos al arreglo el volumen  correspondiente al articulo
                autores = '; '.join(dato.author)
                
                if dato.doi:
                    doi = dato.doi[0]  # Si el articulo tiene un doi relacionado se itera y se agrega al arreglo si no se rellena con un campo vacio
                else:
                    doi = ""
                
                if dato.page:
                    paginas = dato.page[0]
                else:
                    paginas = ""

                #Guardamos en la variable fechaBD la fecha que nos devuelve la API en formato YYYY-MM-DD (Donde solo nos devuelve YYYY-MM y DD por default es 00)
                fechaBD = dato.pubdate
                temp = len(fechaBD)  # Determinamos la longitud de la fecha recibida | 2019-00-00

                try:
                    fecha = fechaBD[:temp - 3 ] 
                    datetime.strptime(fecha, "%Y-%m") #Damos formato correcto a la fecha
                    fecha = fecha.replace('-','/')
                    fecha_ano = fecha[:temp - 6 ]
                except:
                    fecha = fechaBD[:temp - 6 ]
                    fecha_ano = fecha
                
                    
                url = 'https://ui.adsabs.harvard.edu/abs/' + bibcode + '/abstract'
                

                obj = Biblioteca.objects.create(
                    fecha = fecha,
                    bibcode = bibcode,
                    titulo = titulo,
                    autores = autores,
                    revistaPublicacion = revista,
                    paginas = paginas,
                    volumen = volumen,
                    doi = doi,
                    url = url,
                    fecha_ano = fecha_ano,
                    user_id = request.user.id
                )
                obj.save()  
                    
            
        messages.success(request,'<strong>Publicaciones importadas correctamente.<br> Favor de editar la información de sus publicaciones: cuartil, estudiantes, congresos, etc.</strong>')
        return redirect("biblioteca:biblioteca_personal")