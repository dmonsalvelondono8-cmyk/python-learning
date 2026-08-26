"""
EJERCICIO 44:
Genera un número aleatorio entre 1 y 10.
Luego pide al usuario adivinar el número
hasta que lo haga correctamente.
"""

import random

numero_secreto = random.randint(1, 10)
intentos = 0

while True:
    intento = int(input("Adivina el número: "))
    intentos = intentos + 1
    if intento == numero_secreto:
        print(f"Exito! tomo {intentos} intentos adivinar")
        break