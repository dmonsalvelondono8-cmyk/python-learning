#creando mi propia excepcion personalizada
class MiExcepcion(Exception):
    def __init__(self,err):
        print(f"Impresionante, cometiste el siguiente error {err}")

#lanzando mi propia excepcion
#raise MiExcepcion("jajajajajajaj, persona poco culta")

#manejandola
try:
    raise MiExcepcion("jajajajajajaj, persona poco culta")
except:
    print("como vas a cometer ese error?")

