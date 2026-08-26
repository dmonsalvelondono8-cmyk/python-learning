with open("archivos\\texto_de_dalto.txt",'w',encoding="UTF-8") as archivo: #"w" lo que hace es sobreescribir
    #sobreescribiendo el archivo 
    #archivo.write("jajajja te la re contra teclee")
    
    #agregando dos lineas con writelines
    archivo.writelines(["- hola maestro como andas\n","- misericordia\n"]) #\n sirve para añadir un salto de linea
    #agregando otras dos lineas
    archivo.writelines(["- no se porque dijiste eso\n","- yo tampoco"]) #cuando tengo dos writelines se sobreescriben las lineas es como si se acumularan al igual que con write
    
    #lo anterior tambien es como hacer esto 
    #archivo.writelines(["hola maestro como andas\n","misericordia","hola maestro como andas\n","misericordia"])