#utiliza el operador *como argumento(*args)
def suma(nombre,*numeros):
    return f"{nombre},la suma de tus numeros es: {sum(numeros)}"

#lo mismo en la de avajo pero utiliza el operador *como parametro(*args)
def suma_total(numeros):
   # print(*numeros)
    return sum([*numeros])

resultado2 =suma_total([5,3,9])

print(resultado2)







#forma optima de sumar valores utilizando el parametro args
#utiliza el operador *como argumento(*args)
#def suma(nombre,*numeros):
#   return f"{nombre},la suma de tus numeros es: {sum(numeros)}"

#resultado = suma("jose",5,3,9)
#print(resultado)










# #forma no optimaq de sumar valores
# def suma(lista):
#     numeros_sumados = 0
#     for numero in lista:
#         numeros_sumados = numeros_sumados + numero
#     return numeros_sumados

# resultado = suma([5,3,9])
# print(resultado)
