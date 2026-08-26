"""
EJERCICIO 47:
Hacer un menú de opciones que 
incluya la opción del salir del programa.
"""

while True:
    print("1___Sumar")
    print("2___Restar")
    print("3___Salir")
    
    opcion = int(input("Ingrese una opción: "))
    
    if opcion == 1:
        print("Usted esta sumando")
    elif opcion == 2:
        print("Usted esta restando")
    elif opcion == 3:
        break
    else:
        print("Esta opción no es valida.")
        
print("Vuelva pronto")