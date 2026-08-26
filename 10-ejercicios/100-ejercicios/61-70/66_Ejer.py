"""
EJERCICIO 66:
Escribe una función para calcular
el promedio de una lista de números.
"""

def promedio(lista):
    return sum(lista) / len(lista)
    
resultado = promedio([1, 2, 4, 1])

print(resultado)
