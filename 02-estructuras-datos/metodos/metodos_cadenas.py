#DIR- devuelve la lista de atributos validos del objeto pasado 

#UPPER -convierte a mayuscula 
#LOWER -convierte a minuscula
#CAPITALIZE -primera en mayuscula

#FIND -metodo encuentra la primera aparicion del valor especifico, sino devuelve 1
#INDEX -metodo encuentra la primera aparicion del valos especifico, sino devuelve una exepcion 

#ISNUMERIC -si es numerico devuelve true 
#ISALPHA -si es alfa numerico devulve true

#COUNT -devuelve el numero de ocurrencias de una subcadena en la cadena dada
#LEN -cuenta los caracteres de una cadena

#ENDSWITH -verifica si una cadena comienza con 
#STARTSWITH -vefifica si una cadena termina con

#REPLACE -remplaza un valor por otro 
#SPLIT -separa por el parametro dado

cadena1 = "diego mon"
cadena2 = "Bienvenido crack"

#convierte a mayusculas
mayusc = cadena1.upper() #haci se utilzan los metodos en cadena 1 se puede cambiar a texto tambien, etc
#su estructura es Dato.metodo o funcion y ()

#convierte a minusculas
minusc = cadena1.lower()

#primera letra en mayuscula: primero pone todo en minuscula luego la primera en mayuscula 
primera_letra_mayusc = cadena1.capitalize() 

#buscamos una cadena en otra cadena, si no hay cooncidencias devulve -1 
busqueda_find = cadena1.find("a")

#buscamos una cadena en otra cadena, si no hay cooncidencias devuelve error
busqueda_index = cadena1.index("d")

#Si es numerico devuelve true, sino false
es_numerico = cadena1.isnumeric()

#si es alfanumerico devuelve true, sino false
es_alfanumerico = cadena1.isalpha() #los espacios no son alfanumericos entonces si hay espacios da false

#buscamos una cadena en otra cadena, devuelve la cantidad de veces que coincida si no se encuentra da cero
contar_coincidencias = cadena1.count("o")

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1) # len se utiliza haci por que es una funcion no un metodo 

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve True
empieza_con = cadena1.startswith("d")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve True
termina_con = cadena1.endswith("n")

#remplaza un pedazo de la cadena dada, por otra dada si no se encuentran coincidencias a la cadena original devuelve la cadena original
cadena_nueva = cadena1.replace("mon","monsalon") #puedo reemplazar cualquier caracter hasta espacios
# cadena_nueva_2 = cadena_nueva.capitalize() con este codigo le puedo añadir otra funcion mas a la cadena

#separar cadenas con la cadena que le pasemos 
cadena_separada = cadena1.split(" ") # crea una lista en la que separa todo lo que le pasemos
# print(cadena_separada[1]) aca es para econtrar una cadena especifica de la lista en este caso 1 es mon

print(contar_caracteres)