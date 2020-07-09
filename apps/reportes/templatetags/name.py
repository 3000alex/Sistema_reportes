from django import template

register = template.Library()

@register.filter(name='nombreCorto')
def nombreCorto(cadenaAutores,nombreC):
    nombre = nombreC.split(",")
    autores = cadenaAutores.replace(nombreC,'<strong>{nombre}</strong>')
    return str(autores.format(nombre=nombreC))

@register.filter(name='nombreFile')
def nombreFile(nombreFile):
    nombre = nombreFile.replace("anexos/","")
    return nombre