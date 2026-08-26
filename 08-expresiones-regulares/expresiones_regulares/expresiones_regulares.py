import re

texto = '''Holababab maestro. esta es la cadena 1. como estas mi capitan
Esta es la linea 20 de texto.
Y Estaabab es la final (linea 3) definitiva mi capitan'''

# haciendo busquedas
#resultado = re.search("Hola",texto) #search para buscar solo una primera cosa findall para encontrar todo lo que le digamos
#resultado = re.findall("Esta",texto,flags=re.IGNORECASE) #hay dije que busque todos los esta y que ignore las mayusculas

#\d -- busca digitos numerico del 0 al 9
#resultado = re.findall(r"\d",texto) #r se utiliza para indicar que se van a usar expresiones regulares 

#\D -- busca TODO MENOS digitos numerico del 0 al 9
#resultado = re.findall(r"\D",texto)

#\w -- busca caracteres alfanumericos[a-z A-Z 0-9 tambien _]
#resultado = re.findall(r"\w",texto)

#\W -- busca TODO MENOS caracteres alfanumericos[a-z A-Z 0-9 tambien _]
#resultado = re.findall(r"\W",texto)

#\s -- busca espacios en blanco -> espacios, tabs, saltos de line
#resultado = re.findall(r"\W",texto)

#\S -- busca TODO MENOS espacios en blanco -> espacios, tabs, saltos de line
#resultado = re.findall(r"\W",texto)

#. -> busca TODO MENOS saltos de linea 
#resultado = re.findall(r'.',texto)

#\n -> busca saltos de linea 
#resultado = re.findall(r'\n',texto)

#\ -> cancelar caracteres especiales, cancelando la funcion del punto y buscando puntos
#resultado = re.findall(r'\.',texto)

#armando una cadena que busque un numero, seguido de un punto y un espacio 
#resultado = re.findall(r'\d\.\s',texto)

#^ -> buscando el comienzo de una linea (buscando Hola al principio de la linea) 
#resultado = re.findall(r'^Hola',texto)
#con el parametro flags=re.M esto significa que quiere que sea multilinea cada linea la identifica como una linea nueva

#$ -> busca el final de una linea
#resultado = re.findall(r'capitan$',texto)

#{n} -> busca n cantidad de veces el valor de la izquierda (2 numeros juntos esta vez)
#resultado = re.findall(r'\d{2}',texto)

#{n,m} -> al menos n, como maximo m cantidad de caracteres
#resultado = re.findall(r'\d{1,2}',texto)

# | -> busca una cosa o la otra si encuentra una la muestra sin encuentra las dos tambien
#resultado = re.findall(r'\d{2,4}|Hola',texto)

#print(resultado)
