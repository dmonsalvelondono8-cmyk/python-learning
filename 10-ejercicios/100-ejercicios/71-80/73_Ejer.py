"""
EJERCICIO 73:
Filtra palabras mayores a 5 caracteres
de una lista usando comprensión de listas.
"""
def filtrar_palabras_largas(palabras):
    return [palabra for palabra in palabras if len(palabra) > 5]

lista_palabras = ["manzana", "sol", "elefante", "casa", "programación", "gato"]
palabras_largas = filtrar_palabras_largas(lista_palabras)
print(palabras_largas)  # Salida: ['manzana', 'elefante', 'programación']

