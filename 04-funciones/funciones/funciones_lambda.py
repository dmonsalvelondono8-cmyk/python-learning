numeros = [1,2,3,4,5,6,7,8,9]

# Creando una funcion lambda para multiplicar por dos 
multiplicar_por_dos = lambda x : x*2 # retorna automaticamnete los datos 
#print(multiplicar_por_dos(20))

# creando funcion comun que diga si es par o no
# def es_par(num):
#     if (num%2==0):# esta es para los numeros pares, impares seria %2==1
#         return True
# #usando filter con una funcion comun
# numeros_pares = filter(es_par,numeros)

# Creando lo mismo que antes pero con funcion lambda

numeros_pares = filter(lambda numero:numero%2 == 0, numeros) # filter ejecuta cada uno de los valores de un iterable

print(list(numeros_pares))