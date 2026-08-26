"""
EJERCICIO 30:
Calcula la suma de todos los elementos de una lista usando un bucle for.
"""

numeros = list(map(int, input("Ingresa una lista de números separados por espacio: ").split()))

suma = 0

for num in numeros:
    suma += num

print(f"La suma de los elementos de la lista es {suma}")
