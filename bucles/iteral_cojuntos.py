animales = {"gato","perro","loro","cocodrilo"}
numeros  ={52,16,14,72}
#recoriendo la conjunto animales
for animal in animales:
    print(f'aora la variavle animal es igual a {animal}')
    
#recoriendo lasconjuntos  numeros y multiplicando las conjuntos por 10
for numero in numeros:
        resultado = numero * 10
        print (resultado)
        
#iterando las conjuntos del mismo tamaño al mismo tiempo
        for numero ,animal in zip(animales,numeros):
            print(f"recoriendo conjuntos 1:{numero}")
            print(f"recoriendo conjuntos 2:{animal}")
            
  
    #forma no optima de recorer un lista     con su idise (no funciona en conjuntos)   
            # for num in range(len(numeros)): 
            #     print(numeros[num])
                
                
#usando el for else
for numero  in numeros:
 print(f"ejecutando el ultimo bucle, valor actual: {numero}")
else:
 print ("el bucle termino")
 
 #todo lo anterior funciona exactamente igual para tuplas y  conjuntos