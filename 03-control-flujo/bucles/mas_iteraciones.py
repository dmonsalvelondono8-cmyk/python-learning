#creando las listas
frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "hola dalto"
numeros = [2,5,8,10]

# evitando que se coma una manzana con la sentencia continue
for fruta in frutas:
    if fruta == 'granada':
        continue #este se utiliza para saltear lo que queramos saltear
    print(f'me voy a comer una: {fruta}')

#evitar que el bucle siga ejecutandose (el else no se ejecuta tampoco)
for fruta in frutas:
    print(f'me voy a comer una: {fruta}')
    if fruta == 'pera':
        break #es para terminar el bucle aca, en este caso termina en pera y puedo continar normal
else:
    print("bucle terminado")

# Recorrer una cadena de texto por letra
for letra in cadena:
    print(letra)


#for en una sola linea de codigo
numeros_duplicados = [x*2 for x in numeros] # aca decimos que x se va a multiplicar por dos y el valor que va a tener ahora es el resultado
print(numeros_duplicados) # x*2 (esa es la expresion matematica) si quiero puedo sumar multiplicar dividir etc.

