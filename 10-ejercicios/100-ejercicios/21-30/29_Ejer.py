"""
EJERCICIO 29:
Encuentra el menor de una lista de números usando la función min().
"""

numeros = list(map(int, input("Ingresa una lista de números separados por espacio: ").split()))

print(f"El número menor de la lista es {min(numeros)}")
