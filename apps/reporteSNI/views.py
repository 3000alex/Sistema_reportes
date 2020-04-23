from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView
from django.views.generic import View, ListView
# Librerias para validar el login
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from apps.biblioteca.models import Biblioteca
from SNIads import SNIads
import os
from sistema_reportes.settings import BASE_DIR
token = "71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7"
# Create your views here.

class instruccionesSNI(View):
    def get(self,request):
        return render(request, 'reporteSNI/instrucciones.html')


class reporteSNI(View):
    def get(self,request):
        biblioteca = ""
        try:
            biblioteca = Biblioteca.objects.filter(user_id = request.user.id).exclude(numeral_id = 9)
        except:
            biblioteca = ""
    
        return render(request, 'reporteSNI/reporteSNI.html',{'biblioteca':biblioteca})


class metodo1ReporteSNI(View):
    def get(self,request):
        
        author = request.GET.get('autor','None')
        articulos = SNIads.get_papers(author, token=token)
        citas = SNIads.get_citations(articulos, token=token)
        f = open(BASE_DIR + '/media/reporteSNI/refs_{}.tex'.format(SNIads.clean_author(author)), 'w')
        SNIads.print_results(author,articulos,citas,f)
        f.close()

        f = open(BASE_DIR + '/media/reporteSNI/refs_{}.tex'.format(SNIads.clean_author(author)), 'r')
        response = HttpResponse(f, content_type="application/octet-stream" )
        filename = 'refs_{}.tex'.format(SNIads.clean_author(author))
        content = "attachment; filename= %s" %(filename)
        response['content-Disposition'] = content
        f.close()
        return response

@method_decorator(login_required, name='dispatch')
class metodo2ReporteSNI(View):
    def get(self,request):
        
        author = request.GET.get('autor','None')
        #Obtenemos lista de bibcodes
        biblioteca = Biblioteca.objects.filter(user_id = request.user.id)

        bibcodes = open(BASE_DIR + '/media/reporteSNI/bibcodes_{}.dat'.format(author), 'w')
        for b in biblioteca:
            bibcodes.writelines('['+b.bibcode+']'+'\n')
        bibcodes.close()
        
        #Usamos la libreria SNI para generar el reporte con el archivo bibcodes_{}.dat
        articulos = SNIads.get_papers(author, token=token, in_file=BASE_DIR + '/media/reporteSNI/bibcodes_{}.dat'.format(author))
        citas = SNIads.get_citations(articulos, token=token)
        sniFile = open(BASE_DIR + '/media/reporteSNI/refs_{}.tex'.format(SNIads.clean_author(author)), 'w')
        SNIads.print_results(author,articulos,citas,sniFile)
        sniFile.close()


        #Generamos archivo y lo servimos
        sniFile = open(BASE_DIR + '/media/reporteSNI/refs_{}.tex'.format(SNIads.clean_author(author)), 'r')
        response = HttpResponse(sniFile, content_type="application/octet-stream" )
        filename = 'refs_{}.tex'.format(SNIads.clean_author(author))
        content = "attachment; filename='%s'" %(filename)
        response['content-Disposition'] = content
        sniFile.close()
        return response
