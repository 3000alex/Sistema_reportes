from django.http import HttpResponse
# Manejo Word
import docx
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.style import WD_STYLE_TYPE
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
    font.name = 'Times New Roman'
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
    investigadorPosdoctoral = str(User.objects.filter(categoria = 'Investigador posdoctoral' ).count())
    catedraConacyt = str(User.objects.filter(categoria='Cátedra CONACyT').count())
    investigadorAsociadoC = str(User.objects.filter(categoria= 'Investigador Asociado C').count())
    investigadorTitularA = str(User.objects.filter(categoria= 'Investigador Titular A').count())
    investigadorTitularB = str(User.objects.filter(categoria = 'Investigador Titular B').count())
    investigadorTitularC = str(User.objects.filter(categoria = 'Investigador Titular C').count())
    investigadorTitularD = str(User.objects.filter(categoria = 'Investigador Titular D').count())

    #Variables contadoras del Nivel SNI:
    sniCandidato = str(User.objects.filter(nivelSni='Candidato').count())
    sniNivel1 = str(User.objects.filter(nivelSni='Nivel 1').count())
    sniNivel2 = str(User.objects.filter(nivelSni='Nivel 2').count())
    sniNivel3 = str(User.objects.filter(nivelSni='Nivel 3').count())
    sniEmerito = str(User.objects.filter(nivelSni='Emérito').count())
    
    
    fechaInicioPeriodo = periodo.fechaInicio
    yearPeriodo = str(fechaInicioPeriodo.year)
    #Fin objetos

    document.add_paragraph("Resumen de categoria, SNI, y total de entradas por numeral del reporte")
    document.add_paragraph("Categoria: ")

    paragraph = document.add_paragraph(style='List Bullet')
    paragraph.add_run("Investigador Posdoctoral: ")
    paragraph.add_run(investigadorPosdoctoral)

    paragraph = document.add_paragraph(style='List Bullet')
    paragraph.add_run("Cátedra CONACyT: ")
    paragraph.add_run(catedraConacyt)

    paragraph = document.add_paragraph(style='List Bullet')
    paragraph.add_run("Investigador Asociado C: ")
    paragraph.add_run(investigadorAsociadoC)

    paragraph = document.add_paragraph(style='List Bullet')
    paragraph.add_run("Investigador Titular A: ")
    paragraph.add_run(investigadorTitularA)

    paragraph = document.add_paragraph(style='List Bullet')
    paragraph.add_run("Investigador Titular B: ")
    paragraph.add_run(investigadorTitularB)

    paragraph = document.add_paragraph(style='List Bullet')
    paragraph.add_run("Investigador Titular C: ")
    paragraph.add_run(investigadorTitularC)

    paragraph = document.add_paragraph(style='List Bullet')
    paragraph.add_run("Investigador Titular D: ")
    paragraph.add_run(investigadorTitularD)

    document.add_page_break()

    #Tabla 1 Datos Investigadores
    table = document.add_table(rows=1, cols=5, style='Medium Grid 2 Accent 6')
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Apellido'
    hdr_cells[1].text = 'Nombre'
    hdr_cells[2].text = 'SNI'
    hdr_cells[3].text = 'Categoria'
    hdr_cells[4].text = 'Reporte enviado'
    
    for investigador in usuario:
        try:
            reporte = ReporteEnviado.objects.get(usuario_id = investigador.id)
        except:
            reporte=""

        row_cells = table.add_row().cells
        row_cells[0].text = investigador.last_name
        row_cells[1].text = investigador.first_name
        row_cells[2].text = investigador.nivelSni
        row_cells[3].text = investigador.categoria
        if reporte:
            row_cells[4].text = 'ok'
        else:
            row_cells[4].text = ''

    
    document.add_paragraph()
    document.add_paragraph()

    #Tabla 2 (Citas)
    table = document.add_table(rows=1, cols=4, style='Medium Grid 2 Accent 6')
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Citas'
    hdr_cells[1].text = 'Nombre Corto'
    hdr_cells[2].text = 'Totales'
    hdr_cells[3].text = 'Periodo'
    
    for cita in citas:
        row_cells = table.add_row().cells
        row_cells[0].text = cita.citas
        row_cells[1].text = str(cita.usuario.nombreCorto)
        row_cells[2].text = cita.citasObtenidasEnPeriodo
        row_cells[3].text = periodo.nombrePeriodo

    document.add_paragraph()
    document.add_paragraph()

    #Tabla 3 (Indice H)
    table = document.add_table(rows=1, cols=2, style='Medium Grid 2 Accent 6')
    hdr_cells = table.rows[0].cells
    hdr_cells[0].text = 'Nombre Corto'
    hdr_cells[1].text = 'Indice-h'
    
    for cita in citas:
        row_cells = table.add_row().cells
        row_cells[0].text = cita.usuario.nombreCorto
        row_cells[1].text = cita.indiceH


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
            paragraph.add_run("INAOE").bold = True
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

            paragraph = document.add_paragraph()
            paragraph.add_run("Reporte de Productividad Unificado").bold = True
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER

            paragraph.underline = True

            paragraph = document.add_paragraph()
            p = paragraph.add_run()
            p.text = "PERIODO DEL REPORTE: "+MesInicio + "-"+MesFin+" DE "+yearPeriodo
            p.bold = True
            p.underline = True
            
            document.add_paragraph("El presente reporte agrupa toda la información de productividad del investigador y es solicitado dos veces al año. La información aquí" +
                                   "contenida es utilizada para los reportes bianuales entregados a H. Junta de Gobierno y para el proceso" +
                                   "de asignación de Estímulos al Desempeño Académico (EDA).")
            document.add_paragraph("Se solicita resaltar la participación de estudiantes en los puntos en que estén involucrados" +
                                   "(publicaciones, proyectos, patentes, etc.) colocando sus nombres en texto color rojo.")


            paragraph = document.add_paragraph()
            paragraph.add_run("I. INVESTIGACIÓN CIENTÍFICA").bold = True
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if n.id == 32:
            paragraph = document.add_paragraph()
            paragraph.add_run("II. FORMACIÓN DE RECURSOS HUMANOS").bold = True
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if n.id == 41:
            paragraph = document.add_paragraph()
            paragraph.add_run("III. DESARROLLO TECNOLÓGICO E INNOVACIÓN").bold = True
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if n.id == 48:
            paragraph = document.add_paragraph()
            paragraph.add_run("IV. APOYO INSTITUCIONAL").bold = True
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if n.id == 65:
            paragraph = document.add_paragraph()
            paragraph.add_run("V. INFORMACIÓN ADICIONAL").bold = True
            paragraph_format = paragraph.paragraph_format
            paragraph_format.alignment = WD_ALIGN_PARAGRAPH.CENTER
        
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
                        paragraph.add_run(item.cursosCortosDescripcion)
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
                        paragraph.add_run(" ")
                        paragraph.add_run(item.fechaPeriodo)


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
                
        
    d = document.save('demo.docx')

    return document