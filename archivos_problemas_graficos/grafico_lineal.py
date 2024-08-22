
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd .read_csv("archivos_problemas_graficos\\pedo.csv")
#CREANDO EL GRAFICO
sns.lineplot(x="fecha",y="pedo",data=df)

#creando un punto de mas en el MOMENTO MAYOR
plt.plot("01-09",17,"o")

#MOSTRANDO EL GRAFICO
plt.show()