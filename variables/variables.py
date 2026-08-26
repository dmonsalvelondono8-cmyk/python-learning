# LAS VARIABLES SON ESPACIOS QUE SE ALMACENAN EN NUESTRO PROGRAMA (Por que son variables, por que pueden variar)
a = 2
e = 12
c = a + e
print(c)

#LAS VARIABLES SE DECLARAN Y SE DEFINEN Por ejm, declare que la variable se va a llamar nombre y esa variable que ya devclare va a tener el valor de diego Monsa hay la estoy definiendo.
nombre = "diego Monsa"
print(nombre)
#las variables son para guardar info que sea util

#las variables se pueden redifinir por ejm
nombres = "diego"
nombres = "alejandro"
nombres = "Cristian"
print(nombres)
# Al imprimir solo me da cristian por que estoy redefiendo la variable, primero era diego, despues lo redefini a alejandro y por ultimo a cristian
#Otro ejm
numero = 10
numero += 5 # el mas significa el valor que ya tiene mas el numero que este despues del =, Es mejor haci que poner el numero, Tamnbien se puede usar con el menos 
print(numero)

#ejm con el menos 
numeros = 15 
numeros -= 5
print(numeros) #como puedo ver se resta

#CONCATENAR con +
#se utiliza para unir strings por ejm

nombrar = "diego"
bienvenia = "Hola " + nombrar + " ¿como estas?"
print(bienvenia)

#Ahora quiero concatenar pero con numeros y texto haci se hace
#CONCATENAR con f strings
nombra = 5
bienvenido = f"Hola {nombra} ¿como estas?" #se añade f antes del texto y comillas en la variable que queramos transformar
print(bienvenido)
#hay lo que se hizo fue transformar el numero en texto e incluso los datos cambian a texto tambien

# DEL es un oiperador para borrar datos, variables, etc por ejm 
nombri = 5
bienvenida = f"Hola {nombri} ¿como estas?" 
del(bienvenida) #Aca borre la variable bienvenida pero si lo quisiera hacer con nombre no da hay por que nombre en este caso paertenece a bienvenida y si quiero borrarlo debo de ponerlo antes de bienvenida
print(bienvenida)