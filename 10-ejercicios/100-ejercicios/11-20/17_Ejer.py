"""
EJERCICIO 17:
Reemplaza todas las vocales en una 
frase por un asterisco(*).
"""

palabra = "Tacos al pastor" 
vocales = "aeiouAEIOU" 

print(palabra)

for vocal in vocales: 
    palabra = palabra.replace(vocal, "*") 
    
print(f"Frase nueva: '{palabra}'")