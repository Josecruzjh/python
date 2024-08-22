frutas = ["banana","manzana","ciruela","pera","naranja","granada","durazno"]
cadena = "hola dalto"
numeros =[2,6,4,7,3,1]


#evitando que se coma una manzanacon la sentencia continue
for fruta in frutas:
    if fruta == 'manzana':
        continue
    print(f'Me boy a comer una {fruta}')
    
    #evitar que el bucle siga ejecutandose el else no se ejecuta tampoco 
for fruta in frutas:
    if fruta == 'pera':
         break
        
         print("bucle termonado")
    else:
        print("terminado")
# recorer una cadena de texto
for letra in cadena:
    print(letra)
 
 #   for en una sola linea de codigo
# numeros_duplicaos = list()
# for numero in numeros:
#     numeros_duplicaos.append(numero*2)
# print(numeros_duplicaos)

#otra forma  de for en una sola linea de codigo duplicams los numeros
numeros_duplicaos =[x*2 for x in numeros]
print(numeros_duplicaos)