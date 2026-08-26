"""
EJERCICIO 19:
Cuenta las ocurrencias de un carácter 
especifico en una cadena.
"""

cadena = "Tacos Messi"
print(cadena)

palabras = cadena.split()
conteo = len(palabras)

print(f"La frase tiene: {conteo} palabras")
