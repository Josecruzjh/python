import re
texto = '''hola maestro. ,es la cadena 1. como estas mi capitan 564
1esta es la segunda linea de texto.capitan 56444
esta es la segunda linea de texto.capitan abbbbb abaabab abababababab
y esta es la final definitiva capitan_'''

#asindo una busqueda simple
#search
#resultado = re.findall("esta",texto,flags=re.IGNORECASE)

#\d -> busca digitos numericos del 0-9
#resultado = re.findall(r"\d",texto)

#\D -> busca  TODO MENOS digitos numericos del 0-9
# resultado = re.findall(r"\D",texto)

#\W -> busca caracteres alfanumericos [a-zA-Z0-9_,]
#resultado = re.findall(r"\w",texto)

#\w -> busca caracteres alfanumericos [a-zA-Z0-9_,]
#resultado = re.findall(r"\w",texto)

#\W-> busca  TODO MENOS caracteres alfanumericos [a-zA-Z0-9_,]
#resultado = re.findall(r"\W",texto)


#\s-> busca   los espacios en blanco -> espacios,tabs,saltos de line
#resultado = re.findall(r"\s",texto)

#\S-> busca TODO MENOS   los espacios en blanco -> espacios,tabs,saltos de line
#resultado = re.findall(r"\S",texto)

# . -> busca TODO MENOS saltos en linea
# resultado = re.findall(r".",texto)

#\n -> busca saltos en linea
# resultado = re.findall(r'\n',texto)

#\-> canselar caracteres especiales,canselando la fun de punto y bucando puntos
#resultado = re.findall(r'\.',texto)

#armando una cadena que busque un numero ,segido de un punto y espacio 
#resultado = re.findall(f'\d\.\s',texto)
    
#busca el principio de una linea
#^ -> busca el comienzo de una linea buscando  hola a al principio de la linea
#flags=re.M activa la multilinea
#resultado = re.findall(f'^1',texto,flags=re.M)

#^ -> busca el final de la linea
#flags=re.M activa la multilinea
#resultado = re.findall(f'capitan$',texto,flags=re.M)

#{n}-> busca la cantidad de veses el valor de la izquierda
#resultado = re.findall(r'\d{3}',texto,)

#{n,m}-> al menos n,como maximo m
#resultado = re.findall(r'\d{1,4}',texto,) 

#{n,m}-> al menos n,como maximo m
#resultado = re.findall(r'ab{1,4}',texto,) 

#|-> busca una cosa o la otra
resultado = re.findall(r'\d{1,4}|hola',texto,) 
print(resultado)