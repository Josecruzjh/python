# #creando una funcion que nos devuelva los numeros primos 
# #entre 0 y el argumento que pasamos 

# #crear una funcion que verifique si un numero es primo 
# def es_primo(num):
#     #verificamos que el numero pasado no pueda dividirse
#     #por ningun numero entre 2 y ese mismo numero -1
#     for i in range(2,num-1):
#         #si es divisivle por alguno retornamos false y termina en bucle
#         if num%i==0: return False
#        # si termina el bucle,significa que no fue divisible entonses es primo
#     return True

# #creando una funcion que retorne una lista con todos los primos
# def primos_hasta(num):
#     #creamos la lista
#     primos =[]
#     for i in range(3,num+1):
#         #verificamos si el valor es primo
#         resultado = es_primo(i)
#        # en caso de que sea lo agregamos a la lista 
#         if resultado == True: primos.append(i)
#        #devolvemos a la lista 
#     return primos

# #creamos el resultado llamado  a la fucion y lo mostramos
# resultado = primos_hasta(98)
# print(resultado)



#reducion de codigo
primos_hasta  = lambda num : list (filter(lambda x:all(x % i != 0 for i in range(2, int( x ** 0.5) + 1)),range (2,num )))
print(primos_hasta(15))