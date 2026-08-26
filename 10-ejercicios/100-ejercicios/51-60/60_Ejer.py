"""
EJERCICIO 60:
Imprimir la suma de los numeros pares
del 1 al 10 utilizando for.
"""

suma = 0

for i in range(1, 11):
    if i % 2 == 0:
        suma = suma + i
        print(suma)
        