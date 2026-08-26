#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv") #Aca estamos añadiendo la ruta para leer datos.csv

#convertir a string los datos de una columna
df["edad"] = df["edad"].astype(str) #aca le dijimos que la edad la ponga en texto str

#mostrar el tipo de dato del primer elemento de la columna edad
#print(type(df["edad"][0]))

#remplazando los datos "dalto" por "maestro"
df['apellido'] = df['apellido'].replace('dalto','maestro',inplace=True) 

#mostrando la columna apellido 
#print(df['apellido'])

#eliminando las filas con datos vacios
df = df.dropna() #con Axis=1 podemos eliminar las columnas faltantes 
#print(df)

#eliminando las filas repetidas
df = df.drop_duplicates()
#print(df)

#creando un csv con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")


