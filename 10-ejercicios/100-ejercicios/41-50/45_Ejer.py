"""
EJERCICIO 45:
Imprime la tabla de multiplicar de
un número ingresado por el usuario.
"""

tabla = int(input("Ingresa un número: "))

for i in range(1, 11):
    resul = tabla * i
    print(f"{tabla} x {i} = {resul}")