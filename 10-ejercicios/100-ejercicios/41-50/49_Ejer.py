"""
EJERCICIO 49:
Simular el lanzamiento de un dado
hasta obtener un 6.
"""

import random

numero = 0

while numero != 6:
    numero = random.randint(1, 6)
    print(f"Has sacado {numero}")
    
print("Sacaste un 6")