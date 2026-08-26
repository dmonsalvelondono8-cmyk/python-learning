animales = {"perro","gato","tortuga","loro","camello"}
numeros = {1,2,3,4,5}

#recorriendo las lista animales 
for animal in animales:
    print(f'ahora la variable animal es igual a: {animal}')

#recorriendo la lista numeros 
for numero in numeros:
    resultado = numero * 2
    print(f'este es el numero multiplicado por dos: {resultado}') # lo que permite for in es recorrer el codigo 

# si quisieramos recorrer listas al mismo tiempo seria haci 
# ambas deben de tener la misma cantidad de elementos
for numero,animal in zip(animales,numeros): # con zip podemos recorrer dos listas al tiempo
    print(f'recorriendo lista 1 {animal}')
    print(f'recorriendo lista 2 {numero}')
# podemos iterar mas listas al tiempo si queremos el requisito es que deben de tener ka la misma cantidad de elementos


# tambien podemos interar usando la funcion range 

for num in range(10,20): # el primero esta incluido pero el ultimo no en este caso cuenta el 10 pero no el 20 
    print(num)

for num2 in range(5): # si se pone un solo numero itera desde el 0 hasta el numero que colocamos sin contarlo
    print(num2)

#forma correcta de recorrer una lista con su indice
for numeros_listas in enumerate(numeros):
    indice = numeros_listas[0]
    valor = numeros_listas[1]
    print(f'el indice es {indice} y es valor es {valor}') 
# por que se puede ayar indice y valor, por que numeros_listas devuelve una tupla y recordemos que las tuplas 
# devuelven indice y valor

# usando el for/else
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
    print("el bucle termino") #asi no hallan elementos y no hallan datos el else se ejecuta


#todo lo anterior funciona exactamente igual para tuplas, listas y conjuntos (con conuntos hay unas pequeñas diferencias)