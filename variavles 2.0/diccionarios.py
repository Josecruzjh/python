#creando diccionarios con dict()

diccionario = dict(nombre ="jose",apellidos="cruz")


#las no pueden ser claves y usamos usamos frozenset para meter conjuntos
diccionario ={frozenset(["jose","rancio"]):"jaja"}

#creando diccionarios con fromkeys()valor por defecto none
diccionario = dict.fromkeys (["nombre","apellido"])

#creando diccionarios con fromkeys()valor por defecto no se
diccionario = dict.fromkeys(["nombre","apellido"],"no se")


print(diccionario)