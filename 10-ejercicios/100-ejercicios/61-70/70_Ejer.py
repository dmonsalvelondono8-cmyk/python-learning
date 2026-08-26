"""
EJERCICIO 70:
Escribe una función para clasificar 
si una sustancia es ácida, básica o neutra
a partir de su PH
"""

def sustancia(ph):
    if ph < 7:
        return "ácida"
    elif ph > 7:
        return "Básica"
    else:
        return "Neutra"
    
resultado = sustancia(8)

print(resultado)