"""
EJERCICIO 69:
Escribe una función para calcular 
la tasa de desempleo

td = no_desempleados / fuerza_laboral X 100
"""

def desempleo(no_em, si_em):
    return (no_em / si_em) * 100

resultado = desempleo(100, 900)
print(resultado)