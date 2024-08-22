#creando funcion que suma numeros
def sumar_dos():
    #inisio de bucle
    while True:
        #pidiendo numeros
        a=input("Numero 1:")
        b=input("Numero 2:")
        #intentando convertirlos a entero y sumarlos 
        try:
            resultado = int(a) + int(b)
           # si lanzo una excepcion, pedir le que rejiste los datos
        except ValueError as e:
          print("Te pedi un numero salme, no te agas el gracioso")
          print(f"ERROR{e}")
          #si todo salio bien terminamos el bucle
        else:
            break
        #el finally se ejecuta simpre
        finally:
            print("esto se ejecuta siempte")
            
        #mostrnado el resultado
    return resultado


print(sumar_dos())