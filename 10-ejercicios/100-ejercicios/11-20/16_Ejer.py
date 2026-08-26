""""
EJERCICIO 16:
Determina si una palabra es
palíndromo.
"""

palabra = input("Ingrese una palabra: ")

nueva = palabra[::-1]
print(nueva)

# if palabra == palabra[::-1]:
#     print(f"{palabra} es un palindromo.")
# else:
#     print(f"{palabra} no es un palindromo.")