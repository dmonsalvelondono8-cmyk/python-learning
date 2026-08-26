"""
EJERCICIO 31:
Pide un número y verifica si es 
positivo, negativo o cero.
"""

numero = int(input("Ingrese un número: "))

if numero > 0:
    print(f"{numero} es positivo.")
elif numero == 0:
    print(f"{numero} es cero. ")
else:
    print("El número es negativo.")