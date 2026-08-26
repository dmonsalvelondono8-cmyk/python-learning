#promedio de duracion 
otros_curso_min = 2.5
otros_curso_max = 7
otros_curso_promedio = 4
dalto_curso = 1.5

#duracion de crudos (video entero sin editar)
crudo_promedio = 5
crudo_dalto = 3.5


#diferencias de duracion

diferencia_con_min = round(100 - dalto_curso / otros_curso_min * 100)
diferencia_con_max = round(100 - dalto_curso / otros_curso_max * 100,1)                 
diferencia_con_promedio = round(100 - dalto_curso / otros_curso_promedio * 100,1)

#Calculando el porcentaje de tiempo vacio removido

tiempo_vacio_promedio = round(100 - otros_curso_promedio / crudo_promedio * 100)    
tiempo_vacio_dalto = round(100 - dalto_curso / crudo_dalto *100,1)

print("------------------")
print("el curso de dalto dura:")
print(f' - un {diferencia_con_min}% menos que el mas rapido')
print(f' - un {diferencia_con_max}% menos que el mas lento')
print(f' - un {diferencia_con_promedio}% menos que el promedio')
print("------------------")

#Mostrando la cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso promedio elimina un  {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio')
print("------------------")

#Mostrando diferencias si los cursos duraran 10 horas
print(f'ver 10 horas de este curso equivale a ver {round(otros_curso_promedio * 10 / dalto_curso,2)} horas de otros cursos')
print(f'ver 10 horas de otros cursos equivale a ver {round(dalto_curso * 10 / otros_curso_promedio,2)} horas de este curso')
print("------------------")
