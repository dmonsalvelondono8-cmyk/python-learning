"""
EJERCICIO 24:
Calcula el factorial de un número dado
utilizando un bucle while.
"""

numero = int(input("Ingresa un número: "))

factorial = 1
contador = 1

while contador <= numero:
    factorial *= contador
    contador += 1
    
print(f"El factorial de {numero} es {factorial}")

