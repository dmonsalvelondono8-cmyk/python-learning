"""
EJERCICIO 21:
Genera una tabla de multiplicar de un
número dado usando for.
"""

numero = int(input("Ingresa un número: "))

for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
