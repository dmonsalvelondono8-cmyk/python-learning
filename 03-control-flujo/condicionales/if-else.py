# if True:
    #la accion se ejecuta

# if False:
    #la accion no se ejecuta

edad = 16

if edad >= 18:
    print("puedes pasar")
    print("Felicidades eres mayor de edad") # este tambien da por que forma parte de la condicion como se si forma parte, por el espacio

else: #Aca ya no hace parte de la condicion porque no esta en el espacio
    print("no puedes pasar")
    print("eres menor de edad")

# ejemplo con contraseñas

contraseña_almacenada = "diegoMonsa"
contraseña_escrita = "diegoMonsa"

if contraseña_almacenada == contraseña_escrita:
    print("INICIANDO SECCION...")

else:
    print("CONTRASEÑA EQUIVOCADA, INTENTE DE NUEVO")
