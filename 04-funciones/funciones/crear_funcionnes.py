#creando una funcion simple
# def saludar():
#     print("hola lucas, mi maestro ¿como andas?")
# #ejecutando la funcion simple 
# saludar()
# saludar()
# saludar()

#creando una funcio que tenga parametros (los parametros son variables que se crean para usar dentro de la funcion)
def saludar(nombre,sexo):
    sexo = sexo.lower() 
    if (sexo == "mujer"):
        adjetivo = "Reina"
    elif (sexo == "hombre"):
        adjetivo = "Maestro"
    else:
        adjetivo = 'amor'
    
    print(f'hola {nombre}, mi {adjetivo} ¿como andas?')

saludar("lucas","hoMbre")
saludar("lucia","mujER")
saludar("Mos","no binario")

#crear una funcion que nos retorne multiples valores
def crear_contraseña_random(num):
    chars = "abcdefghij"
    num_entero = str(num)
    num = int(num_entero[0])
    c1 = num - 2
    c2 = num
    c3 = num - 5
    contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num * 2}"
    return contraseña,num # con esto puedo utilizar datos afuera de las funciones 

#Desempaquetando la funcion
password,primer_numero = crear_contraseña_random (398)

#mostrando los resultados obtenidos y los datos utilizados para obtenerlo
print(f"Tu contraseña nueva es: {password}")
print(f"El numero de tu contraseña es: {primer_numero}")