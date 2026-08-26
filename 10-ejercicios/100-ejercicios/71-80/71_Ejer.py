"""
EJERCICIO 71:
Crea una función que convierta 
un texto a mayúsculas.
"""

def convertir_a_mayusculas(texto):
    return texto.upper()    


texto = "Hola, ¿cómo estás?"
texto_mayusculas = convertir_a_mayusculas(texto)
print(texto_mayusculas)  # Salida: "HOLA, ¿CÓMO ESTÁS?"