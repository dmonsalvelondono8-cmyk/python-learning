"""
EJERCICIO 48:
Simular un volado o 
lanzamiento de una moneda.
"""

import random 

while True:
    moneda = random.randint(1, 2)
    if moneda == 1:
        print("Cara")
    else:
        print("Cruz")
    jugar = input("Tirar de nuevo (S/N)")
    if jugar.lower() == 'n':
        break
print("Gracias por jugar")