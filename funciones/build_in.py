numeros = [4,7,1,42,15] # funciona con tuplas y conjuntos tambien lo que hace es determinar el numero mas alto de un iterable

#encontrando el numero mayor de una lista 
numero_mas_alto = max(numeros)
print(numero_mas_alto)

#encontrando el numero menor de una lista 
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

#redondeando a 6 decimales
numero = round(12.23764327,2) # si le añado una coma despues de el numero es para definir los decimales ya sea 1,2,3,4 o ninguno sin la coma
print(numero)

#retorna False -> 0, vacio(lista vacia, tupla vacia, etc), False, none / True -> distinto a 0, True, cadena o datos no vacios
resultado_bool = bool("")
print(resultado_bool)

#retorna true, si todos los valores son verdaderos
resultado_all = all([234,"true",[344,23]]) #devuelve practicamnete todo true ecepto los datos de bool 
print(resultado_all)

#suma todos los valores de un iterable
suma_total = sum(numeros)
print(suma_total)


