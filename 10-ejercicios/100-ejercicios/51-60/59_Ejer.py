"""
EJERCICIO 59:
Pedir al usuario un número e 
imrpimir la tabla de multiplicar 
del mismo
"""

num = int(input("Ingrese un número: "))

for i in range(1, 11):
    multi = num * i
    print(f"{num} X {i} = {multi}")