"""
EJERCICIO 26:
Escribe un programa donde el usuario 
adivine un número entre 1 y 10. Usa un 
bucle while hasta que acierte
"""

import random

numero_secreto = random.randint(1, 10)
intento = 0

while intento != numero_secreto:
    intento = int(input("Adivina un número entre 1 y 10: "))
    if intento == numero_secreto:
        print("¡Correcto! Adivinaste el número.")
    else:
        print("Incorrecto, intenta de nuevo.")
