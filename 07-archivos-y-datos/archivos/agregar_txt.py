with open("archivos\\texto_de_dalto.txt",'a',encoding="UTF-8") as archivo: # "a" lo que hace es agregar cada vez que iniciemos el codigo
    #agregando el archivo
    #archivo.write("jajajja te la re contra teclee")
    
    #usando un bucle para agregar varias lineas
    #con el for seria asi
    #con archivo.write("\n") se agrega un espacio antes pero como lo tengo hay tambien da
    for i in range(5):
        archivo.write(f"\nLinea {i+1} agregada")
