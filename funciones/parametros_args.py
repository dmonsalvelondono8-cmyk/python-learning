# #forma no optima de sumar valores 
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados = numeros_sumados + numero
#     return numeros_sumados

# resultado = suma([2,4,5,3,34,22])

#forma optima de sumar valores
def suma_total(numeros):
    return sum([*numeros])

resultados = suma_total([1,2,3,4,5])
print(resultados)

#lo mismo de arriba pero utilizando el operador * como parametro (*args)
#asterisco convierte en este caso a numero en una lista, convierte los parametros en uno
def suma(nombre,*numeros): # el asterisco siempre debe de ir de ultimo con la variable o si no no funciona 
    return f"{nombre} la suma de tus numeros es {sum(numeros)}"

resultado = suma("Diego",4,5,6,7,9)
print(resultado)

