# usando open para abrir un archivo con una codificacion universal (UTF-8)
#aca estamos haciendo que todo el archivo sea igual a esta variable
archivo = open("archivos\\texto_de_dalto.txt",encoding="UTF-8") #encoding="UTF8" lo utilizamos para que no aparescan caracteres raros

#leer archivo completo
#archivo = archivo.read()#con la funcion read leemos el archivo

#leer una sola linea
#linea = archivo.readline()

#leer linea por linea 
#lineas = archivo.lines()

#cerrar el archivo 
archivo.close()

print(archivo)


