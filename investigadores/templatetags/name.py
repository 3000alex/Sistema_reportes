from django import template

register = template.Library()

@register.filter(name='nombreCorto')
def nombreCorto(cadenaAutores,nombreC):
    nombre = nombreC.split(",")
    autores = cadenaAutores.replace(nombre[0],'<strong>{nombre}</strong>')
    return str(autores.format(nombre=nombre[0]))