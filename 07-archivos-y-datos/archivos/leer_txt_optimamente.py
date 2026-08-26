# abriendo el archivo con with open
# es lo mismo de leer_txt.py pero mejor y tira menos errores
with open("archivos\\texto_de_dalto.txt",encoding="UTF-8") as archivo:
    #leemos el archivo 
    contenido = archivo.read() # esto signica que el archivo se abrio ejecuto el bloque y se cerro
    
    #mostramos el archivo
    print(contenido)

#no es necesario cerrarlo al usar with open