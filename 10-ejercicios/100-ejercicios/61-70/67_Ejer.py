"""
EJERCICIO 67:
Escribe una función para calcular 
el volumen de un cilindro
v = pir^2h
"""

PI = 3.1416

def cilindro(radio, altura):
    return PI * radio**2 * altura

resultado = cilindro(3, 5)
print(resultado)