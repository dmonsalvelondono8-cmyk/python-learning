# Keys() -> devuelve las claves (tambien nos sirve para iterar que significa que podemos recorrer un elemento)
# get() -> devuelve el valor de una clave clear) -> elimina todos los elementos (por ejemplo el valor de nombre es diego)
# pop() -> elimina un elemento 
# items() -> para iterar el dict

diccionario = {
    "nombre" : 'diego',
    "apellido" : 'monsalve',
    "años" : 18
}

#nos devuelve un objeto dict_item (un objeto que se puede iterar)
claves = diccionario.keys()

#obteniendo un elemento con get
valor_de_apellido = diccionario.get("apellido") #los corchetes tambien servirian para hacer lo mismo pero hay una diferencia
# los [] lanzan error si no encuentran, en cambio get no, lanza none y el codigo sigue funcionando 

#eliminando todo del diccionario
# diccionario.clear()

#eliminando un elemento de el diccionario
diccionario.pop("nombre","años")

#obteniendo un elemento dict_items iterable 
diccionario_iterable = diccionario.items()

print(diccionario_iterable)