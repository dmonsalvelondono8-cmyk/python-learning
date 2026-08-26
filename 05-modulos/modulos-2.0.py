# si el modulo estuviera dentro de una carpeta en la misma ruta seria asi
# import funciones_buenas.saludar as m_saludar

import sys

sys.path.append("c:\\Users\\diego\\python\\funciones_buenas")
print(sys.path) # con esto podemos ver la ruta de los modulos

import saludar as modulo_saludo

print(modulo_saludo.saludar("diego")) 