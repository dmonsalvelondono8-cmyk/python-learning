# Creando diccionarios con dict(), esta es otro forma de crear dicconarios 
diccionario = dict(nombre="diego",apellido="monsalve")

print(diccionario)
#recordar: no pedomos crear diccionarios vacios sin la funcion dict, tampoco tuplas sin tuple y listas sin list 

#las listas no pueden ser claves por que cambian de valor (mutables)  y no tienen valor fijo (no hasheables) los conjuntos tampoco
diccionario = {frozenset(["diego","mejor" ]):"jajas"} # con frozenset se puede hacer 

#creando diccionarios con fromkeys()
# Aca creamos un diccionario con valores sin definir none
diccionario = dict.fromkeys(["nombre","apellido","años"]) # da none por que no se definio 

# Aca creamos un diccionario con valores definiendo none a "no se que significa"
diccionario = dict.fromkeys(["dm","ml","rat"],"no se que significa") # aca si de definio 

#si no tuviera los corchetes [] el primer obtejo es el iterable y el segundo es como lo que lo va a definir
definicion = dict.fromkeys("iterable","definicion")
print(definicion)


print(diccionario)