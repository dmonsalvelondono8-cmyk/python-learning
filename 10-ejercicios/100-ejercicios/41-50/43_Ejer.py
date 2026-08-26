"""
EJERCICIO 43:
Solicita al ususario ingresar un 
número n, e imprime el factorial de 
ese número.
5! = 5 x 4 x 3 x 2 x 1 = 120
"""
num = int(input("Ingresa un numero: "))

resul = 1

for i in reversed(range(1, num+1)):
    resul = resul * i
    i = i * 1
print(f"El factorial de {num} es: {resul}")
    

