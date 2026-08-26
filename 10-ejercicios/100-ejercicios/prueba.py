numero = int(input("Ingresa un número: "))

es_primo = True

if numero > 1:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print(f"{numero} es un número primo")
    else:
        print(f"{numero} no es un número primo")
else:
    print("El número debe ser mayor que 1 para verificar si es primo")
