#creando funcion que suma numeros
def sumar_dos():
    #iniciando un bucle
    while True:
        #pidiendo numeros
        a = input("numero 1: ")
        b = input("numero 2: ")
        #intentando convertirlos a entero y sumarlos
        try:
            resultado = int(a) + int(b)
        #si lanzo una excepcion, pedirle que reingrese los datos
        except Exception as e:
            print("te pedi un texto no te hagas el gracioso estupido")
            print(f'ERROR: {e}')
        #si todo sale bien terminamos el bucle
        else:
            break
        finally: # si el codigo funciona o no funciona siempre se ejecuta
            print("manejo de exepcion finalizado")

    #mostrando el resultado 
    return resultado
    
print(sumar_dos())
