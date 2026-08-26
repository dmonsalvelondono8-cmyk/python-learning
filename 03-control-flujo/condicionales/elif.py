ingreso_mensual = 12000
gasto_mensual = 4000

#este es un ejemplo de if anidados y else if (elif)

if ingreso_mensual > 10000:
    if ingreso_mensual - gasto_mensual > 3000: # estos son ifs aninados, osea que se puede meter uno entre otro para que cumpla una condicion solo de ese if
        print("Estas bien Bro")
    elif ingreso_mensual - gasto_mensual < 0:
        print("estas en deficit no te alcansa el dinero")
    else:
        print("Estas gastando mucho dinero, Hay que ver si te alcanza")

elif ingreso_mensual > 1000: # elif es else if y es como otra condicion en este caso si ganas 5000 estas bien en latinoamerica y no sos pobre
    print("Estas bien en latino america")

elif ingreso_mensual > 500: # se pueden añadir mas condiciones con elif
    print("Estas bien en colombia")

elif ingreso_mensual > 200: # se pueden añadir mas condiciones con elif
    print("Estas bien en Venezuela")


else:
    print("Sos pobre")