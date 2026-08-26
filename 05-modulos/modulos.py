# importando un modulo y asignando el nombre "m_saludar"
# import mudolo_saludar as m_saludar #as sirve para asignar un nuevo nombre al madulo 

#desde ese modulo importamos dos funciones y les cambiamos el nombre con As
from modulo_saludar import saludar as saludar_normal,saludar_raro as saludar_como_coscu

#creamos las variables con los saludos
saludo = saludar_normal("Diego")
saludo_raro = saludar_como_coscu("Jesus")

#mostramos los resultados
print(saludo)
print(saludo_raro) 

#con dir 
# print(dir(m_saludar)) podemos ver las proiedades y metodos de namesspace

#accedemos al nombre de este modulo 
print(__name__)

#accedemos al nombre del modulo llamado 
#print(m_saludar._name_)