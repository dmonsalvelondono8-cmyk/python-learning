"""
EJERCICIO 33:
Determina si un año es biciesto
Regla de Negocio:
    - Divisible por 4.
    - No divisible por 100.
    - Divisible por 400.
"""

anio = int(input("Ingrese un año: "))

if (anio % 4 == 0 and anio % 100 != 0) or (anio % 100 == 0):
    print("Es año biciesto") 
else:
    print("NO es")