animales = ["gato","perro","loro","cocodrilo"]
numeros  =[52,16,14,72]
#recoriendo la lista animales
for animal in animales:
    print(f'aora la variavle animal es igual a {animal}')
    
#recoriendo laslistas  numeros y multiplicando las listas por 10
for numero in numeros:
        resultado = numero * 10
        print (resultado)
        
#iterando las listas del mismo tamaño al mismo tiempo
        for numero ,animal in zip(animales,numeros):
            print(f"recoriendo listas 1:{numero}")
            print(f"recoriendo listas 2:{animal}")
            
  #forma no optima de recorer un lista          
            for num in range(len(numeros)): 
                print(numeros[num])
                
                for num in enumerate(numeros):
                    indice = num [0]
                    valor =num[1]
                    print(f'el indise es :{indice} y el valor es:{valor}')
                    
#usando el for else
for numero  in numeros:
 print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
 print ("el bucle termino")
