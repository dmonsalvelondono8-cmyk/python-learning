"""
EJERCICIO 46:
Solicita al ususario ingresar un número 
y cuenta cuantos digítos tiene.
"""

num = int(input("Ingrese un número: "))
contador = 0

while num != 0:
    num = num // 10
    contador = contador + 1
print(f"Digitos: {contador}")