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
from registration.models import User
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

        try:
            user = User.objects.get(id=request.user.id)            
        except:
            if not orcid:
                user = "No se ha asignado un Orcid"

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
class publicaciones_author(ListView):
    def get(self,request):
        # Obtenemos valores de busqueda
        query = request.GET['author']

         # determinamos nuestro token de busqueda
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7'
        # traemoes el modelo de biblioteca para validar si esta en biblioteca o no.j
        articulos = Biblioteca.objects.filter(user_id=request.user.id)

        data =  list(ads.SearchQuery(q=query,rows=1000))  # Buscar por autor

        return render(request, 'biblioteca/publicaciones.html', {'data': data, 'articulos': articulos})

@method_decorator(login_required, name='dispatch')       
class publicaciones_bidcode(ListView):
    def get(self,request):
        query_bidcode = request.GET['bibcode']
        # determinamos nuestro token de busqueda
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7'
        data = list(ads.SearchQuery(q=query_bidcode,rows=1000))  # Buscar por bidcode
        articulos = Biblioteca.objects.filter(user_id=request.user.id) # Filtramos articulos para validar si existen en la biblioteca
        # Pasamos como 3 parametro un diccionario (json) con el contenido
        return render(request, 'biblioteca/publicaciones.html', {'data': data, 'articulos': articulos})

@method_decorator(login_required, name='dispatch')
class publicaciones_orcid(ListView):
    def get(self,request):
        query_orcid = request.GET['orcid']
        # determinamos nuestro token de busqueda
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7'
        data = list(ads.SearchQuery(orcid=query_orcid,rows=1000))  # Buscar por orcid
        articulos = Biblioteca.objects.filter(user_id=request.user.id)

        # Pasamos como 3 parametro un diccionario (json) con el contenido
        return render(request, 'biblioteca/publicaciones.html', {'data': data, 'articulos': articulos})


class agregar_biblioteca(View):
    def get(self,request):
        #Obtenemos valores de bidcodes a buscar
        bibcodes = request.GET.getlist("seleccion[]") #Obtenemos bibcodes seleccionados en el template publicacones
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7' #Configuramos el token de ADS para las consultas
        id1 = request.user.id #Obtenemos el ID del usuario para fitrar los articulos que se encuentran en la base y para despues guardarlos en la biblioteca personal
        articulo = Biblioteca.objects.filter(user_id = request.user.id)  #Obtenemos articulos guardados en base de datos
        
        bibcodeBD = [] #Bibcodes que se encuentran en la base de datos
        consulta = [] #Se almacenan los bibcodes que no estan duplicados en la BD y que se agregaran a biblioteca
        titulo = [] #
        fecha = [] 
        autores = []
        bibcode = []
        doi = []
        revista = []
        paginas = []
        volumen = []
        url = []
        autorAux = "" #variable concatenadora de autores de los articulos

        #Se guarda en un array los bibcodes que estan en la BD.
        for a in articulo:
            bibcodeBD.append(a.bibcode)

        #Se recorren los bibcodes que el usuario quiere agregar a la BD y se compara que no se encuentre en la BD para evitar entradas dobles, a su vez se guardan en
        # 'consulta' los bibcodes que se buscaran y agregaran a la BD
        for b in bibcodes:
            if b not in bibcodeBD:
                consulta.append(b)
        
        #Recorremos los bibcodes que se almacenaran y buscamos los atributos correspondientes
        for b in consulta:
            data = ads.SearchQuery(q=b,rows=1000)
                
            for dato in data:
                #Iteramos el titulo y lo agregamos al arreglo que tiene los titulos
                for t in dato.title:
                    titulo.append(t)

                bibcode.append(dato.bibcode)#Agregamos al arreglo el bibcode correspondiente al articulo
                revista.append(dato.pub) #Agregamos al arreglo la revista donde fue publicada correspondiente al articulo

                if dato.page: #Evaluamos si el articulo tiene paginas 
                    p = ''.join(dato.page)   # Si el articulo tiene paginas se itera y se agrega al arreglo si no se rellena con un campo vacio
                    paginas.append(p) 
                else:
                    paginas.append('')
               
                if dato.volume:
                    volumen.append(dato.volume) #Agregamos al arreglo el volumen  correspondiente al articulo
                else:
                    volumen.append('')
                #Guardamos en la variable fechaBD la fecha que nos devuelve la API en formato YYYY-MM-DD (Donde solo nos devuelve YYYY-MM y DD por default es 00)
                fechaBD = dato.pubdate
                temp = len(fechaBD) #Determinamos la longitud de la fecha recibida
                fechaBD = fechaBD[:temp -3 ] 
                f = datetime.strptime(fechaBD,"%Y-%m") #Damos formato correcto a la fecha 
                fecha.append(f) #Procedemos a agregar la fecha al arreglo correspondiente al articulo

                #Iteramos el los autores 
                for d in dato.author:
                    autorAux = autorAux + d + '; ' #Cambiamos el formato que nos regresa la API/NASA para que los autores sean separados por ;
                temp = len(autorAux) #Comprobamos la longitud de la cadena de autores generada
                autorAux = autorAux[:temp -2] #Eliminamos los ultimos caracteres de la cadena correspondientes a un ; y un " "
                autores.append(autorAux) #Procedemos a agregar los autores al arreglo correspondiente al articulo
                autorAux = "" #Limpiamos la variable concatenadora

                
                if dato.doi: #Evaluamos si el articulo tiene un doi relacionado
                    for d in dato.doi: # Si el articulo tiene un doi relacionado se itera y se agrega al arreglo si no se rellena con un campo vacio
                        doi.append(d)
                else:
                    doi.append("")
                
                url.append('https://ui.adsabs.harvard.edu/abs/' +dato.bibcode+ '/abstract')
                
        #Agregamos los articulos a la base de datos iterando un range en len(titulo) el cual nos regresara cuantos titulos hay que agregar e iterar.
        for i in range(len(titulo)):

            obj = Biblioteca.objects.create(
                fecha = fecha[i],
                bibcode = bibcode[i],
                titulo = titulo[i],
                autores = autores[i],
                revistaPublicacion = revista[i],
                paginas = paginas[i],
                volumen = volumen[i],
                doi = doi[i],
                url = url[i],
                user_id = id1
            )
            obj.save()    
        messages.success(request,'<strong>Publicaciones importadas correctamente.<br> Favor de editar la información de sus publicaciones: cuartil, estudiantes, congresos, etc.</strong>')
        return redirect("biblioteca:biblioteca_personal") 
