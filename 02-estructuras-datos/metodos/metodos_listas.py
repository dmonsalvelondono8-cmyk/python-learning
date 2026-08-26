# LIST - crea una lista (lista es una funcion) los de abajo son metodos 

# LEN - cuenta la cantidad de elementos de una lista (Len es una funcion)

# APPEND - agrega un elemento a la lista
# INSERT - agrega un elemento a la lista en el indice especificado
# EXTEND - agrega varios elementos a la lista

# POP - elimina un elemento de una lista, pide indice y devuelve valor
# REMOVE - remueve un elemento de una lista, pide valor
# CLEAR - elimina todos los elementos de una lista

# SORT - ordena una lista de forma ascendente a descendente
# REVERSE - invierte los elementos de una lista

# Creando una lista con list()
lista = list([10,2,34])

#devuelve la cantidad de elementos de la lista
cantidad_elementos = len(lista)

#agregando un elemento a una lista
lista.append(20) # aca no llamamos a otra variable sino que ponemos a la que le queremos agregar de una vez en este caso lista

#agregando un elemento a la lista en un indice especifico
lista.insert(0,28)

#agregando varios elementos a la lista
lista.extend([7,3]) #para agregar los elementos a la lista se ponen los corchetes por que le estamos pasando una lista a otra lista

#eliminando un elemento de una lista (por su indice)
lista.pop(0) #un truco es si le pusieramos -1 nos eliminaria el ultimo, -2 el penultimo, etc.

#removiendo un elemento de la lista por su valor (por su nombre)
lista.remove(2)

#eliminando todos los elementos de la lista 
#lista.clear()

#ordenando la lista (si usamos lista.sort(reverse=True) lo ordena al contrario)
lista.sort() # sort no funciona con texto 

#invirtiendo los elementos de una lista
lista.reverse() # con sort reverse los pone al contrario pero ordenados y ya reverse solo los pone al contrario
#pero desordenados 

#verificando si un elemento se encuentra en la lista 
elemento_encontrado = lista.index(10) #index busca elementos completos no caracteres 

print(elemento_encontrado)