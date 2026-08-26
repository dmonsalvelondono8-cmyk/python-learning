# Creando un conjunto con set
# conjunto = set(["Dato 1",("dato 3")]) a los conjuntos se les pueden añadir tuplas adentro
conjunto = set(["Dato 1",]) 

# metiendo un conjunto dentro de otro conjunto 
conjunto1 = frozenset(["dato 1", "dato 2"]) #frozenset permite meter un conjunto dentro de otro conjunto
conjunto2 = {conjunto1,"dato 3"}

print(conjunto2)


# Teoria de conjuntos 

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#Verificando si es un subconjunto y si lo es poque el conjunto 2 tiene datos del 1 y son mas pocos 
resultado = conjunto2.issubset(conjunto1) # lo que hace la variable issubset es decir si conjunto 1 es subconjunto de conjunto 2

#otra forma de verificar tambien es esta
resultado = conjunto2 <= conjunto1 

# Verificando si es super conjunto es lo contrario de lo de arriba 
resultado = conjunto2.issuperset(conjunto1)
resultado = conjunto2 > conjunto1
# recordar que superconjunto es un conjunto que tiene mas datos que un conjunto que tenga menos datos y parecidos al superconjunto

# verificar si hay algun numero en comun
resultado = conjunto2.isdisjoint(conjunto1) #va a ser true si no hay ni un solo dato igual, si hay haci sea uno va a ser false

print(resultado)