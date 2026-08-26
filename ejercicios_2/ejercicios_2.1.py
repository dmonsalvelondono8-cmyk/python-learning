# Falto el profe y los pibes van a armar la clase 
# pedir el nombre y la edad de los compañeros que vinieron a clases 

#funcion para obtener la asistencia y al profesor segun la edad.
def obtener_compañeros(cantidad_de_compañeros):

    #creando la lista con los compañeros
    compañeros = []

    #ejecutando un for para pedir informacion a cada compañero
    for i in range(cantidad_de_compañeros):
        nombre = (input("ingrese el nombre del compañero: "))
        edad = int(input("ingrese la edad del compañero: "))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lista
        compañeros.append(compañero)
    
    #ordenandolos de menor a mayor segun su edad
    compañeros.sort(key=lambda x:x[1]) # con esta funcion estamos ordenando los compañeros por edad de menor a mayor 
    
    #compañeros[x] devuelve una tupla con (nombre,edad) y despues accedemos al nombre
    #para definir al asistente y al profesor.
    asistente = compañeros[0][0] # aca le estamos diciendo que acceda al elemento 0 ese elemento tiene dos elementos y le estamos diciendo que acceda 
    profesor = compañeros[-1][0]# al elemnto cero del el elemento cero en general
    
    #retornamos una tupla
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion
asistente,profesor = obtener_compañeros(5)
print(f"el profesor es: {profesor} y su asistente es: {asistente}")
