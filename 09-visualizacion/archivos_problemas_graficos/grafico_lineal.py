import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns

df = pd.read_csv("archivos_problemas_graficos\\ventas.csv")

#creando el grafico 
sns.lineplot(x="fecha",y="ventas",data=df)

#creando un punto en la fecha con mas ventas
plt.plot("01-09",17,"o")

#mostrando el grafico 
plt.show()
