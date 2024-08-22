import pandas as pd
#usando la funcion read_csv para leer losarchivos SCV

# df =pd.read_csv("archivos\\datos.csv",names=["name","lastname","age"])
df =pd.read_csv("archivos\\datos.csv")
df2 =pd.read_csv("archivos\\datos.csv")

#opteniendo los nombres de la columna nombre
# nombres = df ["name"]

nombres = df ["nombre"]

#eslaising
# cadena ="0123456789"
# print(cadena[2:10])

# print(df)

#ordenar el dataframe por la edad
df_orden_asendente =df.sort_values("edad")
#print (df_orden_asendente)

#ordenandolo de forma  desendente
df_orden_desendente =df.sort_values("edad",ascending=False)
# print (df_orden_desendente)

# concatenando los dos dataframes
df_concatenado =pd.concat([df,df2])
# print(df_concatenado)

#accediendo a las primeras 3 filas con hea()
primer_fila = df.head(2)
# print(primer_fila)

#accedieendo a las ultimas 
ultimas_filas = df .tail(2)
# print(ultimas_filas)

#accediendo a la cantidad de  filas  y columnas con shape

# filas_y_columas_totales  = df.shape
# print(filas_y_columas_totales )

filas_totales,columnas_totales = df.shape
# print(columnas_totales)

#opteniendo data estadistica de dataframe
df_info = df.describe()
# print(df_info)

#acediendo  a la edad de la fila 2
elemento_especificado_loc = df.loc[2,"edad"]
# print(elemento_especificado_loc)

#acediendo  a la edad de la fila 2 con iloc
elemento_especificado_iloc = df.iloc[2,2]

apellidos_loc = df.loc[:,"apellido"]

#accediendo a todas la filas de un coumna
apellidos = df.iloc[:,1]
# print(apellidos)

fila_3 =df.loc[2,:]


#acediendo a al fila  con edad mayor que 30

mayor_que_30 = df. loc[df["edad"]>30,]
print(mayor_que_30)