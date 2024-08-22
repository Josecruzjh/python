#falto el profesor y los alumnos van a armar la clase.
#pedir el nombre y la edad de los compañeros que vinieron hoy a clase.

def optener_copañeros(cantidad_de_compañeros):
    
    #creando la lista con los compañeros
    compañeros = []
    
    #ejecutando un for para pedir informacion de cada compañero
    for i in range(cantidad_de_compañeros):
        nombre  = input("ingrese el nombre del compañero:")
        edad = int (input("ingese la edad del compañero:"))
        compañero = (nombre,edad)
        
        #agregando la informacion a la lita 
        compañeros.append(compañero)
        
        #ordenandolos de menor a mayor segun su edad 
    compañeros.sort(key=lambda x:x[1])
    
    #compañeros [x] devuelve una tupla con (nombre,edad)y despues accedemos al nombre 
    # para definir al asistente y al profesor.
    asistente = compañeros[0][0]
    profesor = compañeros[-1][0]
    
    #retornamos una tupla 
    return asistente,profesor

#desempaquetamos lo que nos retorna la funcion 
asistente,profesor = optener_copañeros(5)

#mostrar el resultado
print(f"el profesor es :{profesor} y su asistente es :{asistente}")

