#avriendo el archivo con with open
with open("archivos\\texto_de_jose.txt",encoding="UTF-8") as archivo:
    #leemos archivo
    contenido = archivo.read()
    
    #mostramos el archivo
    print(contenido)
    
    #no es nesesario cerrarlo al usar  with open
    