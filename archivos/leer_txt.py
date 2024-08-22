# archivo_sin_leer = open ("archivos\\texto_de_jose.txt",encoding="UTF-8")
#usando el archivo con una codificasion universal(UTF-8)a "archivo"
archivo = open ("archivos\\texto_de_jose.txt",encoding="UTF-8")

#leer archivo completo
#archivo = archivo_sin_leer.read()

# leer una sola linea
#linea = archivo_sin_leer.readline(10)
# print(linea)

# leer una sola linea
#archivo = archivo.readline(10)
# print(linea)


#leer linea por linea
lineas = archivo.readlines()

#cerrar el archivo
archivo.close()


print(lineas)

