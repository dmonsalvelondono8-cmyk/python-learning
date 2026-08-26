"""
EJERCICIO 40:
Calcular el IMC e 
interpretarlo.
"""

peso = 70
estatura = 1.70

imc = peso / (estatura * estatura)

print(imc)

if imc < 18.5:
    print('Bajo de peso')
elif imc < 25:
    print('Peso normal')
elif imc < 30:
    print('Sobrepeso')
elif imc < 35:
    print('Obesidad grado I')
elif imc < 40:
    print('Obesidad grado II')
else:
    print('Obesidad grado III')