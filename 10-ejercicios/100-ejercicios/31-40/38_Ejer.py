"""
EJERCICIO 38:
Determina si un número es 
divisile entre 5 y 7.
"""

num = input("Ingrese un número: ")

num = int(num)

if num % 5 == 0 and num % 7 == 0:
    print("EL número es divisible por 5 y 7")
else:
    print("El numero no es divisible.")