with open('archivos\\texto_de_jose.txt','w',encoding="UTF-8") as archivo:
    
    #sobre escriviendo el archivo
    #archivo.write("te la recotra teclee")
    
    #agregando 2 lineas con writelines
    archivo.writelines(["-hola maestro como andas\n","-Misericordia\n"])
    
    #agregando otras 2 lineas
    archivo.writelines(["-nose por que dijite eso\n","-yo tampoco"])