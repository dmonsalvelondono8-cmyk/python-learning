#2 listas, una con nombre otra con apellidos
nombres = ["Lucas","Matias","Camila","Pedro","Roberto"]
apellidos = ["Dalto","Zing","Dalto","Robetix","tarado"]


#Registrar esta informacion en un TXT de forma optima 
with open("C:\\Users\\diego\\python\\archivos_problemas\\nombre_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son:\n\n")
    [arch.writelines(f'Nombre: {n}\nApellido: {a}\n-----------\n') for n,a in zip(nombres,apellidos)] # todo el codigo se encierra en lista para que funcione

#aca estamos creando un archivo .txt y escribiendo en el 
