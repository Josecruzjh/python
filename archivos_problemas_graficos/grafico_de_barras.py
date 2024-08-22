
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd .read_csv("archivos_problemas_graficos\\cofla_ingresos.csv")
#CREANDO EL GRAFICO
sns.barplot(x="fuente",y="ingresos",data=df)

#opteniendo el total de de ingresos 
total_ingresos =df['ingresos'].sum()

#mostrando el total 
print(f"el total de ingresoses de {total_ingresos}USD")

#MOSTRANDO EL GRAFICO
plt.show()