#DATOS COMPUESTOS
#son datos que adentro tienen datos simples o tambien compuestos que podemos agrupar para acceder a ellos
#1 LISTAS
lista = ["diego Monsa","Soy diego",True,1.85]
print(lista[1]) #por que da soy diego por que se cuenta desde el cero y en este caso el 1 es soy diego, para acceder a un elemento de la lista se ponen []
#una lista es una matrix que esuna matrix un conjunto de datos

#2 TUPLAS
#Son casi lo mismo que las listas pero con parentesis y no se pueden modificar 
tupla = ("diego Monsa","Soy diego",True,1.85)
#tupla[1] = "popocho" #no se puede modificar 
print(tupla[0])

#ejm de modificacion de lista 
list = ["messi","cristiano",False,20]
list[1] = "Crsitiano aca no va messi es el mejor"
print(list[1])
#para mostrar algo ya sea en listas o tuplas simepre se utilizan los corchetes en ambas

#SET (conjunto)
#para crearllo usamos llaves, el set son elementos desordenados y que pueden cambiar son casi iguales que las listas
conjunto = {"diego Monsa","Soy diego",True,1.85} # el conjunto se puede modificar pero los elementos no como las tuplas, se pueden redefinir
# conjunto = {"todo esto es falso"} en los conjuntos puedo redefinir como aca
# tupla = ("jajajaj")y si añadimos tupla tambien funciona podemos redefinir

# los conjuntos no dejan acceder a un indice especifico de esta forma como en las listas: print(conjunto[1]) sino con un bucle que vamos a ver despues tambien se puede de esta forma en general 
print(conjunto) 
#otra cosa importante de los conjuntos es que nos se pueden añadir datos iguales

#DICT (DICCIONARIO)
#su estructura es clave : valor en este ejm clave en la primera linea es 'nombre' : valor es "diego monsalve" y separamos por comas 
diccionario = {
    'nombre' : "diego monsalve",
    'edad' : 18,
    'le_gusta_python' : True,
    'altura' : 1.80,
    'dato_duplicado' : "diego monsalve"
}
# en los diccionarios nosotros denominamos el indice con un nombre, en las listas se denomina por defecto 
print(diccionario['edad'] + 2) #Aca le dije a diccionario que le sumara 2 a la edad 
