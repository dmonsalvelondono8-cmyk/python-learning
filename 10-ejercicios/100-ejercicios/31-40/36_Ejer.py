"""
EJERCICIO 36:
Pide un carácter y determina
si es una vocal.
"""

caracter = input("Ingrese un caracter: ")

vocales = ['a', 'e', 'i', 'o', 'u']

if caracter.lower() in vocales:
    print("Es una vocal")
else:
    print("NO es una vocal")

