import pandas as pd #pd es el diminutivo de pandas

#usando la funcion read_csv para leer el archivo CSV
df = pd.read_csv("archivos\\datos.csv")
df2 = pd.read_csv("archivos\\datos.csv")                         
#names=["name","lastname","age"]) #se usa names para cambiar el nombre del encabezado juntandolo con la funcion de arriba

# obteniendo los datos de la columna nombre
nombres = df["nombre"]


#cadena = "0123456789"
#print(cadena[0:4])# los dos puntos o eslaicing sirve para decirle la pocion de inicio y finaL que quereremos que recorra el codigo el final no lo cuenta

#ordenando el dataframe por la edad de menor a mayor
df_orden_ascendente = df.sort_values("edad")

#ordenandolo de mayor a menor
df_orden_desendente = df.sort_values("edad",ascending=False)

#concatenando los 2 dataframes
df_concatenado = pd.concat([df,df2])

#accediendo a la primera fila con head()
primer_fila = df.head(1) # si le damos cero muestra encabezado, si le damos uno muestra el encabezado y la primera fila y haci sucecivamente

#accediendo a las ultimas filas con tail()
segunda_fila = df.tail(1)

#accediendo a la cantidad de filas y columnas con shape
filas_totales,columnas_totales = df.shape

#obteniendo data estadistica del dataframe:
df_info = df.describe()

#accediendo a un elemto especifico del df con loc de la fila 2
elemento_especifico_loc = df.loc[2,"edad"]

#accediendo a un elemto especifico del df con iloc de la fila 2 (aca se busca es por indice)
elemento_especifico_loc = df.iloc[2,2]

#accediendo a todas los apellidos con loc
apellidos_loc = df.loc[:,"apellido"]

#accediendo a todas los apellidos con iloc
apellidos = df.iloc[:,1]

#accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

#accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

#accediendo a filas con mayor edad a 30
mayor_que_30 = df.loc[df["edad"]>30,:] # la rpimera que pide son las filas y la segunda las columnas en este caso todas 

print(mayor_que_30)