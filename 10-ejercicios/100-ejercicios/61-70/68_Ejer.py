"""
EJERCICIO 68:
Escribe una función que pida por teclado
la distancia y la velocidad para
poder calcular el tiempo de viaje.
"""

def tiempo():
    distancia = int(input("Ingrese la distancia: "))  
    velocidad = int(input("Ingrese la velocidad: "))  
    return distancia / velocidad

print(f"El tiempo es: {tiempo()}")