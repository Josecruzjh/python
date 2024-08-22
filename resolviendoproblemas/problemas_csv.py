#cmbiar el tipo de dato de una columna
import pandas as pd
df =pd.read_csv("resolviendoproblemas\\datos.csv")

#combertir a string los datos de una columna
df["edad"] = df ["edad"].astype(str)

#mostrar los dato del primer elemento  de la columna de edad
#print(type(df["edad"][0]))

#remplazandolos datos"dalto" por "maestro"
df ["apellido"].replace("dalto","maestro",inplace=True)


#eliminando las filas con datos faltntes
df = df.dropna()


#eliminando las filas repetidas
df =df.drop_duplicates()

#creando un CSVcon el data frame resultante(limpio)
df .to_csv("resolviendoproblemas\\datos_limpios.csv")
print(df)
