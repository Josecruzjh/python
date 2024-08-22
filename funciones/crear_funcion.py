#creando una funcion simple
#def saludar():
   # print("hola lucas mi maestro ¿como andas?")
    #ejecutando la funcion simple
    #saludar()
    
    
#crear una funcion que tenga parametros
def saludar (nombre,sexo):
     sexo = sexo.lower()
     if (sexo == "mujer"):
         adjetivo = "reina"
     elif (sexo =="hombre"):
         adjetivo = "titan"
     else:
         adjetivo = 'amor'
     print (f"Hola {nombre}, mi {adjetivo} ¿como andas?")
    
     saludar ("Camila","mujer")
     saludar ("Dalto","hombre")
     saludar ("Fran","no binario")
    
#crear una funcion que nos retorne Valores
def crear_contraseña_random(num):
            chars = "abcdefghij"
            num_entero = str(num)
            num = int(num_entero[0])
            c1 = num - 2
            c2 = num
            c3 = num - 5
            contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
            print(contraseña)
        
crear_contraseña_random(4)
    
    
    
    # password = crear_contraseña_random(1)
    # frase = f"Tu contraseña nueva es: {password}"
    # print(frase)
    
