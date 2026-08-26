"""
EJERCICIO 23:
Calcula la suma de todos los números pares
entre 1 y 50 utilizando un bucle for.
"""

suma = 0

for i in range(1, 51):
    if i % 2 == 0:
        suma += i

print(f"La suma de los números pares entre 1 y 50 es {suma}")
