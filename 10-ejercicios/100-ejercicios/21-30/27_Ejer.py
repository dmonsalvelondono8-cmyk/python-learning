"""
EJERCICIO 27:
Imprime los primeros 10 números de la 
serie fibonacci utilizando bucle for
"""

a, b = 0, 1

print(a)

for _ in range(9):
    print(b)
    a, b = b, a + b

