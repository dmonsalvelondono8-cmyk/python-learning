"""
EJERCICIO 28:
Solicita al usuario una lista de números y encuentra el mayor. Usa la función incorporada max()
"""

numeros = list(map(int, input("Ingresa una lista de números separados por espacio: ").split()))

print(f"El número mayor de la lista es {max(numeros)}")
