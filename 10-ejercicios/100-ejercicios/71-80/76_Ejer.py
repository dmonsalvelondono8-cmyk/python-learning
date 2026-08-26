"""
EJERCICIO 76:
Encuentra las palabras más grandes 
de un texto usando bucles.
"""
def palabras_mas_grandes(texto):
    palabras = texto.split()
    max_longitud = 0
    palabras_grandes = []

    for palabra in palabras:
        longitud = len(palabra)
        if longitud > max_longitud:
            max_longitud = longitud
            palabras_grandes = [palabra]
        elif longitud == max_longitud:
            palabras_grandes.append(palabra)

    return palabras_grandes

texto = "El rápido zorro marrón salta sobre el perro perezoso"
resultado = palabras_mas_grandes(texto)
print(resultado)  # Salida: ['rápido', 'marrón', 'perezoso']    