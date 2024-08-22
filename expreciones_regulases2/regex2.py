import re 

#la cadena en la que se bucaran los numeros 
text = "La fecha es 23/06/2021n y el telefono es +52-496-118-84-21"

#el patron a buscar 
pattern = r"\d{2}/\d{2}/\d{4}"

#el texto con el que representara el patron
remplacement ="Fecha oculta"

#remplazar todas las apariciones del en la cadena  de texto
new_text = re.sub(pattern,remplacement,text)

#imprimir un resultado
print("texto modificado",new_text)
