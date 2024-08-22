
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd .read_csv("archivos_problemas_graficos\\bigotes.csv")
#CREANDO EL GRAFICO
sns.boxplot(x="categoria",y="valor",data=df)


#MOSTRANDO EL GRAFICO
plt.show()