def frase(nombre, apellido, adjetivo): # estos son parametros posicionales
    return f'hola {nombre} {apellido}, sos muy {adjetivo}'

frase_resultante = frase("diego","Alejandro","inteligente")

print(frase_resultante)




# def frases(nombre,apellido,abjetivo):
#     return f'hola {nombre} {apellido}, sos muy {abjetivo}'
# #utlizando keyword arguments
# frase_resul = frases(abjetivo = "pro", nombre = "monsalve",apellido = "alejandro")
# print(frase_resul)


#creando la misma funcion con un parametro opcional y un valor por defecto 
def frases(nombre,apellido,abjetivo = "tonto"): # aca estoy definiendo abjetivo tonto de forma preterminada
    return f'hola {nombre} {apellido}, sos muy {abjetivo}'
frase_resulta = frases("diego","Alejandro","inteligente") # aca redefini tonto por inteligente, si no estuviera inteligente daria tonto
print(frase_resulta)
