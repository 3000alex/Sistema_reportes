from django import template

register = template.Library()

@register.filter(name='nombreCorto')
def nombreCorto(cadenaAutores,nombreC):
    autores = cadenaAutores.replace(nombreC,'<strong>{nombreC}</strong>')
    return str(autores.format(nombreC=nombreC))