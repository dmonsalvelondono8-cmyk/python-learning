"""
EJERCICIO 13:
Cuenta cuantas vocales hay en una palabra.
"""


palabra = "Tacos al pastor"
vocales = ["a", "e", "i", "o", "u"]
contador = 0

for letra in palabra.lower():  
    if letra in vocales:
        contador += 1

print(f"Frase: '{palabra}'")
print(f"Hay {contador} vocales")
