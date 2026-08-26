"""
EJERCICIO 75:
Escribe una función que calcule 
el promedio de una lista.
"""
def carcular_promedio(lista):
    promedio = sum(lista) / len(lista)
    return promedio


lista = [2, 4, 6, 8, 10]
promedio = carcular_promedio(lista)
print(f"El promedio es: {promedio}")