# #crear una funcion de 3 parametros
# def frase (nombre,apellido,adjetivo):
#     return f'Hola{nombre} {apellido},sos muy {adjetivo}'

# #utilizando keyword arguments
# frase = frase_resultante = frase(adjetivo = "capo",nombre="Lucas",apellido="Dalto",)
# print(frase_resultante)


#creando la misma funcion con un parametro opcional y un valor por defecto
def frase (nombre,apellido,adjetivo ="Tonto"):
     return f'Hola{nombre} {apellido},sos muy {adjetivo}'
 
frase_resultante = frase(nombre="Lucas",apellido ="Dalto",adjetivo="intelijente",)
print(frase_resultante)

