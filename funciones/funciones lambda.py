numeros =[1,2,3,4,5,6,7,8,9,11,12,13,14,15,20]
#creando un funcion lambda para multiplicar por dos
multiplicar_por_dos = lambda X :X*2
#creando una function comun que diga si es par o no      //pares y inpares
# def es_par (num):
#     if (num%2==1):
#         return True
#usando filter con una funcion comun
numeros_pares =filter(lambda numero:numero%2 == 0,numeros)

print(list(numeros_pares))










# numeros =[1,2,3,4,5,6,7,8,9,11,12,13,14,15,20]
# #creando un funcion lambda para multiplicar por dos
# multiplicar_por_dos = lambda X :X*2
# #creando una function comun que diga si es par o no      //pares y inpares
# def es_par (num):
#     if (num%2==1):
#         return True
# #usando filter con una funcion comun
# numeros_pares =filter(es_par,numeros)


# print(list(numeros_pares))