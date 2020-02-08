    def post(self,request):
        #Obtenemos valores de bidcodes a buscar
        bibcodes = request.POST.getlist("seleccion[]") #Obtenemos bibcodes seleccionados en el template publicacones
        ads.config.token = '71EV2aJvIIiFZLSoA9cWRlxgjxTQKwykjEi3yQS7' #Configuramos el token de ADS para las consultas
        articulos = Biblioteca.objects.filter(user_id = request.user.id)  #Obtenemos articulos guardados en base de datos
        autorAux = "" #variable concatenadora de autores de los articulos
        consulta = [] #Se almacenan los bibcodes que no estan duplicados en la BD y que se agregaran a biblioteca

        for b in bibcodes:
            if b not in articulos:
                consulta.append(b)
        
        for bibcode in consulta:
            data = ads.SearchQuery(q=bibcode,fl='title,pubdate,author,doi,page,volume,pub',rows=1000)

            for dato in data:
                #Iteramos el titulo y lo agregamos al arreglo que tiene los titulos
                
                titulo = dato.title

                bibcode = bibcode  # Agregamos al arreglo el bibcode correspondiente al articulo
                revista = dato.pub  # Agregamos al arreglo la revista donde fue publicada correspondiente al articulo

                if dato.page:  # Evaluamos si el articulo tiene paginas 
                    # Si el articulo tiene paginas se itera y se agrega al arreglo si no se rellena con un campo vacio
                    p = ''.join(dato.page)
                    paginas = p
                else:
                    paginas = ''

                if dato.volume:
                    volumen = dato.volume  # Agregamos al arreglo el volumen  correspondiente al articulo
                else:
                    volumen = ''
                #Guardamos en la variable fechaBD la fecha que nos devuelve la API en formato YYYY-MM-DD (Donde solo nos devuelve YYYY-MM y DD por default es 00)
                fechaBD = dato.pubdate
                temp = len(fechaBD)  # Determinamos la longitud de la fecha recibida
                fechaBD = fechaBD[:temp - 3 ] 
                f = datetime.strptime(fechaBD, "%Y-%m") #Damos formato correcto a la fecha 
                fecha = f  # Procedemos a agregar la fecha al arreglo correspondiente al articulo

                #Iteramos el los autores
                for d in dato.author:
                    autorAux = autorAux + d + '; '  # Cambiamos el formato que nos regresa la API/NASA para que los autores sean separados por ;
                temp = len(autorAux)  # Comprobamos la longitud de la cadena de autores generada
                autorAux = autorAux[:temp - 2] #Eliminamos los ultimos caracteres de la cadena correspondientes a un ; y un " "
                autores = autorAux  # Procedemos a agregar los autores al arreglo correspondiente al articulo
                autorAux = ""  # Limpiamos la variable concatenadora

                if dato.doi:  # Evaluamos si el articulo tiene un doi relacionado
                    for d in dato.doi:  # Si el articulo tiene un doi relacionado se itera y se agrega al arreglo si no se rellena con un campo vacio
                        doi= d
                else:
                    doi = ""

                url = 'https://ui.adsabs.harvard.edu/abs/' + dato.bibcode + '/abstract'

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
                    user_id = request.user.id
                )
                obj.save()  
                    
            #Agregamos los articulos a la base de datos iterando un range en len(titulo) el cual nos regresara cuantos titulos hay que agregar e iterar.
            
        messages.success(request,'<strong>Publicaciones importadas correctamente.<br> Favor de editar la información de sus publicaciones: cuartil, estudiantes, congresos, etc.</strong>')
        return redirect("biblioteca:biblioteca_personal")