"""
EJERCICIO 74:
Calcula cuantos días faltan para 
terminar el año usando la libreria 
datatime.
"""
import datetime

def dias_para_fin_de_anio():
    hoy = datetime.date.today()
    fin_de_anio = datetime.date(hoy.year, 12, 31)
    diferencia = fin_de_anio - hoy
    return diferencia.days  

dias_faltantes = dias_para_fin_de_anio()    
print(f"Faltan {dias_faltantes} días para terminar el año.")