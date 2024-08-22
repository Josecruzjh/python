diccionario = {
    "nombre":"Lucas",
    "apellido":"cruz",
    "subs":1000
}

#recoriendo diccionario para optener claves
for key in diccionario:
   key 
   print(f"la clave es:{key}")

#recoriendo diccionario con items () para optener la clave y el valor
for datos in diccionario.items():
   key = datos [0]
   value = datos[1]
   print(f"la clave es:{key} y el valor es :{value}")
   