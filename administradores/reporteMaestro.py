from django.http import HttpResponse
# Manejo Word
import docx
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.style import WD_STYLE
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.table import WD_TABLE_DIRECTION
from docx.enum.table import WD_ALIGN_VERTICAL
from docx.enum.table import WD_ROW_HEIGHT_RULE
#Modelos 
from investigadores.models import Numeral, Citas, ReporteEnviado, Modelo1, Modelo2, Modelo3, Modelo4, Modelo5, Modelo6, Modelo7, Modelo8, Modelo9, Modelo10
from investigadores.models import Modelo11, Modelo12, Modelo13, Modelo14, Modelo15, Periodo
from registration.models import User
from biblioteca.models import Biblioteca
from docx.shared import RGBColor

def obtenerDuplicados(request):
    DatosNumeral = []
    #periodo = Periodo.objects.last()
    periodo = Periodo.objects.get(id=1)
    yearPeriodo = periodo.fechaInicio.year
    monthPeriodoInicio = periodo.fechaInicio.month
    monthPeriodoFin = periodo.fechaFin.month 
    bibliotecaCompleta = Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin])
    biblioteca = Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin]).distinct()
    cantidadDuplicados = 0

    for bc in bibliotecaCompleta:
        for bc2 in biblioteca:
            if bc.bibcode == bc2.bibcode:
                cantidadDuplicados = cantidadDuplicados + 1
    

    print(cantidadDuplicados)

    return cantidadDuplicados

def Reporte(request):
    document = Document()
    style = document.styles['Normal']
    font = style.font
    font.name = 'Calibri'
    #Objetos
    #periodo = Periodo.objects.last()
    periodo = Periodo.objects.get(id=1)

    yearPeriodo = periodo.fechaInicio.year
    monthPeriodoInicio = periodo.fechaInicio.month
    monthPeriodoFin = periodo.fechaFin.month 
    biblioteca = Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin])

    usuario = User.objects.filter(is_staff = 0) #exclude(email = 'astrofi@inaoep.mx')
    modelo1 = Modelo1.objects.filter(periodo_id = periodo.id)
    modelo2 = Modelo2.objects.filter(periodo_id = periodo.id)
    modelo3 = Modelo3.objects.filter(periodo_id = periodo.id)
    modelo4 = Modelo4.objects.filter(periodo_id = periodo.id)
    modelo5 = Modelo5.objects.filter(periodo_id = periodo.id)
    modelo6 = Modelo6.objects.filter(periodo_id = periodo.id)
    modelo7 = Modelo7.objects.filter(periodo_id = periodo.id)
    modelo8 = Modelo8.objects.filter(periodo_id = periodo.id)
    modelo9 = Modelo9.objects.filter(periodo_id = periodo.id)
    modelo10 = Modelo10.objects.filter(periodo_id = periodo.id)
    modelo11 = Modelo11.objects.filter(periodo_id = periodo.id)
    modelo12 = Modelo12.objects.filter(periodo_id = periodo.id)
    modelo13 = Modelo13.objects.filter(periodo_id = periodo.id)
    modelo14 = Modelo14.objects.filter(periodo_id = periodo.id)
    modelo15 = Modelo15.objects.filter(periodo_id = periodo.id)
    citas = Citas.objects.filter(periodo_id = periodo.id)
    numeral = Numeral.objects.all()
    obtenerDuplicados(request)


    #Variables contadoras de cada Categoria 
    investigadorPosdoctoral = User.objects.filter(categoria = 'Investigador posdoctoral' ).count()
    catedraConacyt = User.objects.filter(categoria='Cátedra CONACyT').count()
    investigadorAsociadoC = User.objects.filter(categoria= 'Investigador Asociado C').count()
    investigadorTitularA = User.objects.filter(categoria= 'Investigador Titular A').count()
    investigadorTitularB = User.objects.filter(categoria = 'Investigador Titular B').count()
    investigadorTitularC = User.objects.filter(categoria = 'Investigador Titular C').count()
    investigadorTitularD = User.objects.filter(categoria = 'Investigador Titular D').count()
    TotalNombramientos = investigadorPosdoctoral + catedraConacyt + investigadorAsociadoC + investigadorTitularA + investigadorTitularB + investigadorTitularC + investigadorTitularD
    #Variables contadoras del Nivel SNI:
    sniCandidato = User.objects.filter(nivelSni='Candidato').count()
    sniNivel1 = User.objects.filter(nivelSni='Nivel 1').count()
    sniNivel2 = User.objects.filter(nivelSni='Nivel 2').count()
    sniNivel3 = User.objects.filter(nivelSni='Nivel 3').count()
    sniEmerito = User.objects.filter(nivelSni='Emérito').count()
    TotalSNI = sniCandidato + sniNivel1  + sniNivel2 + sniNivel3 + sniEmerito
    
    
    fechaInicioPeriodo = periodo.fechaInicio
    yearPeriodo = str(fechaInicioPeriodo.year)
    #Fin objetos




    document.add_page_break()


    if fechaInicioPeriodo.month == 1:
        MesInicio = "ENERO"
        MesFin = "JUNIO"
    elif fechaInicioPeriodo.month == 6:
        MesInicio = "JUNIO"
        MesFin = "DICIEMBRE"

    for n in numeral:
        if n.id == 1:#Header del documento
            paragraph = document.add_paragraph()
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER 
            p = paragraph.add_run()
            p.bold = True
            p.text = "INAOE"
            p.font.size = Pt(13) #
            

            paragraph = document.add_paragraph()
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            p = paragraph.add_run()
            p.bold = True
            p.text = "Coordinación de Astrofísica"
            p.font.size = Pt(13) #

            paragraph = document.add_paragraph()
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            paragraph.underline = True
            p = paragraph.add_run()
            p.bold = True
            p.text = "Reporte de Productividad Unificado"
            p.font.size = Pt(13) #
            
            
            paragraph = document.add_paragraph()
            
            p = paragraph.add_run()
            p.text = "PERIODO DEL REPORTE: "+MesInicio + "-"+MesFin+" DE "+yearPeriodo
            p.bold = True
            p.underline = True
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
            
            document.add_paragraph()
            paragraph = document.add_paragraph()
            p = paragraph.add_run()
            p.bold = True
            p.text = "Estadísticas de Investigadores: Coordinación de Astrofísica"
            
            paragraph = document.add_paragraph("Número total de investigadores en la plataforma de reportes: ")
            p = paragraph.add_run()
            p.bold = True
            p.text = str(User.objects.filter(is_staff = 0).count())

            #Tabla de nombramiento 
#grid 4 enfasis 1
            table = document.add_table(rows=1, cols=2, style='Medium Shading 1 Accent 1')
            
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Nombramiento'
            hdr_cells[1].text = 'Número'

            
            row_cells = table.add_row().cells
            row_cells[0].text = "Postdocs"
            row_cells[1].text = str(investigadorPosdoctoral)
            
            row_cells = table.add_row().cells
            row_cells[0].text = "Cátedra CONACyT"
            row_cells[1].text = str(catedraConacyt)

            row_cells = table.add_row().cells
            row_cells[0].text = "Asociado C"
            row_cells[1].text = str(investigadorAsociadoC)

            row_cells = table.add_row().cells
            row_cells[0].text = "Investigador Titular A"
            row_cells[1].text = str(investigadorTitularA)

            row_cells = table.add_row().cells
            row_cells[0].text = "Investigador Titular B"
            row_cells[1].text = str(investigadorTitularB)

            row_cells = table.add_row().cells
            row_cells[0].text = "Investigador Titular C"
            row_cells[1].text = str(investigadorTitularC)

            row_cells = table.add_row().cells
            row_cells[0].text = "Investigador Titular D"
            row_cells[1].text = str(investigadorTitularD)

            row_cells = table.add_row().cells
            row_cells[0].text = "Total"
            row_cells[1].text = str(TotalNombramientos)
            
            document.add_paragraph()

            #Tabla Distincion SNI
            table = document.add_table(rows=1, cols=2, style='Medium Shading 1 Accent 1')
            table.alignment = WD_TABLE_ALIGNMENT.CENTER #ALINEACION CENTRAL
            table.allow_autofit = True
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Distinción SNI'
            hdr_cells[1].text = 'Número'

            row_cells = table.add_row().cells
            row_cells[0].text = "Candidato"
            row_cells[1].text = str(sniCandidato)
            
            row_cells = table.add_row().cells
            row_cells[0].text = "Nivel 1"
            row_cells[1].text = str(sniNivel1)

            row_cells = table.add_row().cells
            row_cells[0].text = "Nivel 2"
            row_cells[1].text = str(sniNivel2)

            row_cells = table.add_row().cells
            row_cells[0].text = "Nivel 3"
            row_cells[1].text = str(sniNivel3)

            row_cells = table.add_row().cells
            row_cells[0].text = "Emérito"
            row_cells[1].text = str(sniEmerito)

            row_cells = table.add_row().cells
            row_cells[0].text = "Total"
            row_cells[1].text = str(TotalSNI)

            document.add_paragraph()

            #Tabla 3 Datos Investigadores
            table = document.add_table(rows=1, cols=5, style='Medium Shading 1 Accent 1')
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Apellido'
            hdr_cells[1].text = 'Nombre'
            hdr_cells[2].text = 'Categoria'
            hdr_cells[3].text = 'SNI'
            hdr_cells[4].text = 'Reporte enviado'
            
            for investigador in usuario:
                try:
                    reporte = ReporteEnviado.objects.get(usuario_id = investigador.id)
                except:
                    reporte=""

                row_cells = table.add_row().cells
                row_cells[0].text = investigador.last_name
                row_cells[1].text = investigador.first_name
                row_cells[2].text = investigador.categoria
                row_cells[3].text = investigador.nivelSni
                if reporte:
                    row_cells[4].text = 'ok'
                else:
                    row_cells[4].text = ''


            document.add_page_break()

            paragraph = document.add_paragraph()
            paragraph.add_run("I.Resumen: Investigación").bold = True
            table = document.add_table(rows=1, cols=3, style='Medium Shading 1 Accent 1')
            
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Numeral'
            hdr_cells[1].text = 'Concepto'
            hdr_cells[2].text = 'Total en el periodo'

            row_cells = table.add_row().cells
            row_cells[0].text = "1"
            row_cells[1].text = "Artículos científicos arbitrados en revistas periódicas indizadas en el primer cuartil"
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 1).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "2"
            row_cells[1].text = "Artículos científicos arbitrados en revistas periódicas indizadas en segundo o tercer cuartil."
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 2).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "3"
            row_cells[1].text = "Artículos científicos arbitrados en revistas periódicas indizadas en cuarto cuartil"
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 3).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "4"
            row_cells[1].text = "Artículos científicos arbitrados en revistas del Índice CONACYT"
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 4).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "5"
            row_cells[1].text = "Artículos científicos arbitrados en revistas periódicas emergentes"
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 5).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "6"
            row_cells[1].text = "Artículos científicos arbitrados en revistas periódicas no indizadas"
            row_cells[2].text = str( Modelo1.objects.filter(periodo_id = periodo, numeral_id = 6).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "7"
            row_cells[1].text = "Artículos aceptados con arbitraje internacional en revistas periódicas indizadas"
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 7).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "8"
            row_cells[1].text = "Artículos aceptados con arbitraje en revistas periódicas no indizadas"
            row_cells[2].text = str( Modelo1.objects.filter(periodo_id = periodo, numeral_id = 8).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "9"
            row_cells[1].text = "Artículos enviados con arbitraje internacional en revistas periódicas indizadas"
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 9).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "10"
            row_cells[1].text = "Artículos enviados con arbitraje en revistas periódicas no indizadas"
            row_cells[2].text = str( Modelo1.objects.filter(periodo_id = periodo, numeral_id = 10).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "11"
            row_cells[1].text = "Artículos científicos arbitrados en extenso en memorias de congresos internacionales"
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 11).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "12"
            row_cells[1].text = "Artículos científicos arbitrados en extenso en memorias de congresos nacionales"
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 12).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "13"
            row_cells[1].text = "Artículos científicos no arbitrados en extenso en memorias de congresos internacionales"
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 13).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "14"
            row_cells[1].text = "Artículos científicos no arbitrados en extenso en memorias de congresos nacionales"
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 14).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "14a"
            row_cells[1].text = "Reportes científicos no arbitrados en publicaciones periódicas."
            row_cells[2].text = str( Biblioteca.objects.filter(fecha__year=yearPeriodo, fecha__month__range=[monthPeriodoInicio, monthPeriodoFin], numeral_id = 15).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "15"
            row_cells[1].text = "Autor o coautor de libros (no memorias de congreso)"
            row_cells[2].text = str( Modelo1.objects.filter(periodo_id = periodo, numeral_id = 16).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "16"
            row_cells[1].text = "Autor de capítulo de libro (no del mismo libro y no memoria de congreso)"
            row_cells[2].text = str( Modelo1.objects.filter(periodo_id = periodo, numeral_id = 17).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "17"
            row_cells[1].text = "Edición de libros / memorias"
            row_cells[2].text = str( Modelo1.objects.filter(periodo_id = periodo, numeral_id = 18).count() )

            row_cells = table.add_row().cells 
            row_cells[0].text = "18"
            row_cells[1].text = "Proyectos CONACyT"
            row_cells[2].text = str( Modelo2.objects.filter(periodo_id = periodo, numeral_id = 19).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "19"
            row_cells[1].text = "Proyectos institucionales"
            row_cells[2].text = str( Modelo2.objects.filter(periodo_id = periodo, numeral_id = 20).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "20"
            row_cells[1].text = "Proyectos externos"
            row_cells[2].text = str( Modelo2.objects.filter(periodo_id = periodo, numeral_id = 21).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "21"
            row_cells[1].text = "Proyectos interinstitucionales"
            row_cells[2].text = str( Modelo2.objects.filter(periodo_id = periodo, numeral_id = 22).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "22"
            row_cells[1].text = "Proyectos comercializados"
            row_cells[2].text = str( Modelo2.objects.filter(periodo_id = periodo, numeral_id = 23).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "23"
            row_cells[1].text = "Participación en el comité científico de conferencias internacionales (Scientific Organizing Committee; Steering Committee; similares)"
            row_cells[2].text = str( Modelo1.objects.filter(periodo_id = periodo, numeral_id = 24).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "24"
            row_cells[1].text = "Conferencias científicas internacionales."
            row_cells[2].text = str( Modelo3.objects.filter(periodo_id = periodo, numeral_id = 25).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "25"
            row_cells[1].text = "Conferencias científicas nacionales"
            row_cells[2].text = str( Modelo3.objects.filter(periodo_id = periodo, numeral_id = 26).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "26"
            row_cells[1].text = "Pláticas invitadas en conferencias internacionales"
            row_cells[2].text = str( Modelo3.objects.filter(periodo_id = periodo, numeral_id = 27).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "27"
            row_cells[1].text = "Pláticas invitadas en conferencias nacionales"
            row_cells[2].text = str( Modelo3.objects.filter(periodo_id = periodo, numeral_id = 28).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "28"
            row_cells[1].text = "Resúmenes en congreso internacionales"
            row_cells[2].text = str( Modelo3.objects.filter(periodo_id = periodo, numeral_id = 29).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "29"
            row_cells[1].text = "Resúmenes en congreso nacionales"
            row_cells[2].text = str( Modelo3.objects.filter(periodo_id = periodo, numeral_id = 30).count() )
            

            document.add_paragraph()

            paragraph = document.add_paragraph()
            paragraph.add_run("II.	Resumen: Formación de recursos humanos").bold = True
            table = document.add_table(rows=1, cols=3, style='Medium Shading 1 Accent 1')
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Numeral'
            hdr_cells[1].text = 'Concepto'
            hdr_cells[2].text = 'Total en el periodo'

            row_cells = table.add_row().cells
            row_cells[0].text = "31"
            row_cells[1].text = "Alumnos graduados de doctorado en tiempos PNPC"
            row_cells[2].text = str( Modelo4.objects.filter(periodo_id = periodo, numeral_id = 32).count() )
                        
            row_cells = table.add_row().cells
            row_cells[0].text = "32"
            row_cells[1].text = "Alumnos graduados de doctorado fuera de tiempo PNPC"
            row_cells[2].text = str( Modelo4.objects.filter(periodo_id = periodo, numeral_id = 33).count() )
            
            row_cells = table.add_row().cells
            row_cells[0].text = "33"
            row_cells[1].text = "Alumnos graduados de maestría en tiempos PNPC"
            row_cells[2].text = str( Modelo4.objects.filter(periodo_id = periodo, numeral_id = 34).count() )
                        
            row_cells = table.add_row().cells
            row_cells[0].text = "34"
            row_cells[1].text = "Alumnos graduados de maestría fuera de tiempo PNPC"
            row_cells[2].text = str( Modelo4.objects.filter(periodo_id = periodo, numeral_id = 35).count() )
            document.add_paragraph()

            paragraph = document.add_paragraph() 
            paragraph.add_run("III.	Resumen: Desarrollo tecnológico e innovación").bold = True
            table = document.add_table(rows=1, cols=3, style='Medium Shading 1 Accent 1')
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Numeral'
            hdr_cells[1].text = 'Concepto'
            hdr_cells[2].text = 'Total en el periodo'

            row_cells = table.add_row().cells # Modelo 7  40-41-42-43-44
            row_cells[0].text = "40"
            row_cells[1].text = "Derechos de autor y aseguramiento de propiedad intelectual"
            row_cells[2].text = str( Modelo7.objects.filter(periodo_id = periodo, numeral_id = 41).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "41"
            row_cells[1].text = "Patentes solicitadas"
            row_cells[2].text = str( Modelo7.objects.filter(periodo_id = periodo, numeral_id = 42).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "42"
            row_cells[1].text = "Patentes en proceso de evaluación que ya aprobaron el examen de forma (IMPI)"
            row_cells[2].text = str( Modelo7.objects.filter(periodo_id = periodo, numeral_id = 43).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "44"
            row_cells[1].text = "Patentes licenciadas"
            row_cells[2].text = str( Modelo7.objects.filter(periodo_id = periodo, numeral_id = 45).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "45"
            row_cells[1].text = "Dirección de proyectos de investigación tecnológica"
            row_cells[2].text = str( Modelo8.objects.filter(periodo_id = periodo, numeral_id = 46).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "46"
            row_cells[1].text = "Reportes técnicos registrados"
            row_cells[2].text = str( Modelo9.objects.filter(periodo_id = periodo, numeral_id = 47).count() )

            document.add_paragraph()

            paragraph = document.add_paragraph()
            paragraph.add_run("IV. Resumen: Apoyo Institucional").bold = True
            table = document.add_table(rows=1, cols=3, style='Medium Shading 1 Accent 1')
            hdr_cells = table.rows[0].cells
            hdr_cells[0].text = 'Numeral'
            hdr_cells[1].text = 'Concepto'
            hdr_cells[2].text = 'Total en el periodo'

            row_cells = table.add_row().cells
            row_cells[0].text = "48"
            row_cells[1].text = "Artículos de divulgación científica en medios masivos"
            row_cells[2].text = str( Modelo15.objects.filter(periodo_id = periodo, numeral_id = 49 ).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "49"
            row_cells[1].text = "Conferencias de divulgación en eventos masivos"
            row_cells[2].text = str( Modelo10.objects.filter(periodo_id = periodo, numeral_id = 50).count() )

            row_cells = table.add_row().cells
            row_cells[0].text = "50"
            row_cells[1].text = "Conferencias de difusión o promoción externas"
            row_cells[2].text = str( Modelo10.objects.filter(periodo_id = periodo, numeral_id = 53).count() )
                        
            row_cells = table.add_row().cells
            row_cells[0].text = "51"
            row_cells[1].text = "Conferencias de difusión o promoción internas"
            row_cells[2].text = str( Modelo10.objects.filter(periodo_id = periodo, numeral_id = 54).count() )
                        
            row_cells = table.add_row().cells
            row_cells[0].text = "52"
            row_cells[1].text = "Organización de eventos académicos vinculados al quehacer institucional"
            row_cells[2].text = str( Modelo10.objects.filter(periodo_id = periodo, numeral_id = 55).count() )
            

            document.add_paragraph()

            paragraph = document.add_paragraph()
            paragraph.add_run("I. INVESTIGACIÓN CIENTÍFICA").bold = True

        if n.id == 32:
            paragraph = document.add_paragraph()
            paragraph.add_run("II. FORMACIÓN DE RECURSOS HUMANOS").bold = True

        if n.id == 41:
            paragraph = document.add_paragraph()
            paragraph.add_run("III. DESARROLLO TECNOLÓGICO E INNOVACIÓN").bold = True

        if n.id == 48:
            paragraph = document.add_paragraph()
            paragraph.add_run("IV. APOYO INSTITUCIONAL").bold = True

        if n.id == 65:
            paragraph = document.add_paragraph()
            paragraph.add_run("V. INFORMACIÓN ADICIONAL").bold = True

        
        document.add_paragraph(n.nombre) #Nombre - Numerales
        
        for inv in usuario:   
            for item in biblioteca:
                if n.id == item.numeral_id  and inv.id == item.user_id:
                    if item.autores:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.autores)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.titulo)
                        paragraph.add_run(" ")
                        paragraph.add_run(str(item.fecha.month))
                        paragraph.add_run("/")
                        paragraph.add_run(str(item.fecha.year))
                        paragraph.add_run(" ")
                        paragraph.add_run(item.revistaPublicacion)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.paginas)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.volumen)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.estudiantesEnArticulo).font.color.rgb = RGBColor(255,0,0)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.doi)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.url).font.color.rgb = RGBColor(0x42, 0x24, 0xE9)
            
            for item in modelo1:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.autores:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.autores)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.titulo)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.revistaPublicacion)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.estudiantesEnArticulo).font.color.rgb = RGBColor(255,0,0)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.doi)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.url).font.color.rgb = RGBColor(0x42, 0x24, 0xE9)
            
            for item in modelo2:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.nombreProyecto:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.nombreProyecto)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.participantes)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.estudiantes)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.responsableTecParticipante)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.descripcion)
    
            for item in modelo3:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.tituloPresentacion:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.tituloPresentacion)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.autores)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.nombreConferencia)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.fecha)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.presentacionPoster)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.estudiantes)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.doi)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.url)
                    
            for item in citas:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.citas:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run("Citas: ")
                        paragraph.add_run(item.citas)

                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run("Citas obtenidas en periodo: ")
                        paragraph.add_run(item.citasObtenidasEnPeriodo)

                    if item.indiceH:
                        document.add_paragraph("30a. Índice H")
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run("Índice H: ")
                        paragraph.add_run(item.indiceH)



            for item in modelo4:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.nombreCompleto:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.nombreCompleto)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.tituloTesis)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.fecha)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.url)

            for item in modelo5:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.nombreCurso:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.nombreCurso)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.periodoNumeral)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.notas)

            for item in modelo6:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.nombre:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.nombre)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.tituloTesis)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.Grado)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.institucion)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.fecha)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.notas)

            for item in modelo7:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.autores:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.autores)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.descripcion)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.url)

            for item in modelo8:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.nombre:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.nombre)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.descripcion)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.participantes)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.url)

            for item in modelo9:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.titulo:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.titulo)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.autores)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.numeroReportes)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.fecha)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.url)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.revistaPublicacion)

            for item in modelo10:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.descripcion:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.descripcion)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.fecha)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.url)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.periodoNumeral)
                   

            for item in modelo11:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.nombreEstudiante:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.nombreEstudiante)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.descripcion)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.fecha)


            for item in modelo12:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.laboratorioTaller:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.laboratorioTaller)
                   

            for item in modelo13:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.descripcion:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.descripcion)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.agenciasFinancieras)
                   

            for item in modelo14:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.descripcion:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.descripcion)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.TelescopioInstrumentoInfra)
                        paragraph.add_run(" ")
                        paragraph.add_run(item.participantes)

            for item in modelo15:
                if n.id == item.numeral_id  and inv.id == item.usuario_id:
                    if item.descripcion:
                        document.add_paragraph(inv.nombreCorto)
                        paragraph = document.add_paragraph(style='List Bullet')
                        paragraph.add_run(item.descripcion)
                
        
    d = document.save('media/reporte.docx')

    return document