"""
EJERCICIO 72:
Escibe una función que cuente caracteres
especificos en un texto.
"""

def contar_caracteres(texto, caracter):
    contador = 0
    for char in texto:
        if char == caracter:
            contador += 1
    return contador

texto = "Hola, ¿cómo estás?"
caracter_a_contar = "o"
cantidad = contar_caracteres(texto, caracter_a_contar)
print(f"El caracter '{caracter_a_contar}' aparece {cantidad} veces.")