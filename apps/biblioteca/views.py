from django.shortcuts import render
import ads
#Librerias para validar el login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import Biblioteca
from django.views.generic.base import TemplateView
from django.views.generic import ListView, View
from django.http import JsonResponse
from django.contrib import messages
import json
from django.http import HttpResponse
ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7' #Configuramos el token de ADS para las consultas
# Create your views here.

@method_decorator(login_required, name='dispatch')
class biblioteca_personal(ListView):
    template_name = 'biblioteca/biblioteca_personal.html'
    context_object_name = 'biblioteca'
    
    def get_queryset(self):
        return Biblioteca.objects.listarBiblioteca(self.request.user)

@method_decorator(login_required, name='dispatch')
class busqueda_ads(TemplateView):
    template_name = 'biblioteca/busqueda_ads.html'

@method_decorator(login_required, name='dispatch')
class editar_biblioteca(View):

    def post(self, request):      
        id1 = request.POST.get('id')
        obj = Biblioteca.objects.get(id=id1)
        estudiantes_en_articulo1 = request.POST.get('estudiantes_en_articulo', obj.estudiantes_en_articulo)  # Contador (Front - end)
        numeral1 = request.POST.get('numeral',obj.numeral_id) #Numeral relacionado con articulo    
        if numeral1 == "":
            obj.estudiantes_en_articulo = estudiantes_en_articulo1
            numeral = ""
            obj.save()
        else:
            obj.estudiantes_en_articulo = estudiantes_en_articulo1
            obj.numeral_id = numeral1
            obj.save()
            numeral = str(obj.numeral)      
        data = {'id': obj.id, 'estudiantes_en_articulo':obj.estudiantes_en_articulo,'numeral':numeral}

        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class eliminar_biblioteca(View):
    def post(self, request):
        id1 = request.POST.get('id', None)
        
        Biblioteca.objects.get(id=id1).delete()
        data = {'deleted': True}
        return JsonResponse(data)

@method_decorator(login_required, name='dispatch')
class publicaciones_generales(View):
    def get(self,request):
        # Obtenemos valores de busqueda
        query = request.GET.get('author')
        # traemoes el modelo de biblioteca para validar si esta en biblioteca o no.j
        articulos = Biblioteca.objects.filter(usuario_id=request.user.id)

        data =  list(ads.SearchQuery(q=query,fl='title,pubdate,author,doi,page,volume,pub,bibcode',rows=1000))  # Buscar por autor

        return render(request, 'biblioteca/publicaciones.html', {'data': data, 'articulos': articulos})
      
class publicaciones_bidcode(View):
    def get(self,request):
        query_bidcode = '2018MNRAS.479..917G'
        articulo = []
        data = ads.SearchQuery(bibcode=query_bidcode,fl='title,pubdate,author,doi,page,volume,pub,bibcode',rows=1000)  # Buscar por bidcode
        articulos = Biblioteca.objects.filter(usuario_id=request.user.id) # Filtramos articulos para validar si existen en la biblioteca
        # Pasamos como 3 parametro un diccionario (json) con el contenido
        for d in data:
            articulo.append({
            'title': d.title,
            'pubdate': d.pubdate,
            'author': d.author,
            'doi': d.doi,
            'page': d.page,
            'volume': d.volume,
            'pub': d.pub
        })
        print(articulo)
        
        return HttpResponse(articulo)

@method_decorator(login_required, name='dispatch')
class publicaciones_orcid(View):
    def get(self,request):
        query_orcid = request.GET.get('orcid')

        data = list(ads.SearchQuery(orcid=query_orcid,fl='title,pubdate,author,doi,page,volume,pub,bibcode',rows=1000))  # Buscar por orcid
        articulos = Biblioteca.objects.filter(usuario_id=request.user.id)

        # Pasamos como 3 parametro un diccionario (json) con el contenido
        return render(request, 'biblioteca/publicaciones.html', {'data': data, 'articulos': articulos})

@method_decorator(login_required, name='dispatch')
class agregar_biblioteca(View):
    def post(self,request):
        #Obtenemos valores de bidcodes a buscar
        #bibcodes = request.POST.getlist("seleccion[]") #Obtenemos bibcodes seleccionados en el template publicacones
        datos = request.POST.getlist('articulos[]')  
        articulosDB = [] 
        lista = json.loads(datos[0])
        for l in lista:
            obj = Biblioteca(
                    fecha = l['fecha'],
                    bibcode = l['bibcode'],
                    titulo = l['titulo'],
                    autores = l['autores'],
                    revista_publicacion = l['pub'],
                    paginas = l['page'],
                    volumen = l['volume'],
                    doi = l['doi'],
                    url = 'https://ui.adsabs.harvard.edu/abs/' + l['bibcode'] + '/abstract',
                    fecha_ano = l['fecha'][0:4],
                    usuario_id = request.user.id
                )
            articulosDB.append(obj)
        
        Biblioteca.objects.bulk_create(articulosDB)  #creamos todos los objetos de tipo biblioteca en la BD.
        messages.success(request,'<strong>Publicaciones importadas correctamente.<br> Favor de editar la información de sus publicaciones: cuartil, estudiantes, congresos, etc.</strong>')
        return JsonResponse({'ok':'ok'})#redirect("biblioteca:biblioteca_personal")