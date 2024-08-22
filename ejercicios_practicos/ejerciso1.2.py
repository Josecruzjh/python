#Le pedimos al usuario que nos diera una frase o varias
frase = input("desirme una frase y te calculo cunto tardarias si tubieras que desirlo:")
#Creamos una lista con todos las palabras de la frase se separan cada vez que hay un espacio en blanco
palabras_separadas = frase.split(" ")
#Usamos len para ver la cantidad de elementos que hay en una lista
cantidad_de_palabras = len(palabras_separadas)
#En caso de que tarde más de un minuto en decirlo le decimos para que pare un poco
print(f'Dijiste{cantidad_de_palabras} palabras, y tardarias {cantidad_de_palabras} segundos en decirlo')
print(f'Dalto lo dira en {cantidad_de_palabras * 100 // 2*1.3 / 100} segundos {cantidad_de_palabras} segundos')
