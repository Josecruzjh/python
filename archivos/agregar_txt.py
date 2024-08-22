with open('archivos\\texto_de_jose.txt','a',encoding="UTF-8") as archivo:
    
    #sobre escriviendo el archivo
    archivo.write("jjajjaajajte la recotra teclee")
    archivo.write("hola como estas")
    archivo.write("\n")
    #agregar el archivo
    #usando un bucle para agregar varias lineas 
    for i in range(5):
        archivo.write(f"Linea{i+1}agregada\n")
    
    