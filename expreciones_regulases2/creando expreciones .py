import re
# detectando un numero CABA y ocultandolo

texto  = "hola pedo mi numero es: +52 496 118-8421 +52 496 118-8421"

pattern = r'\+\d{2}\s\d{3}\s\d{3}-\d{4}'
remplazo = re.sub(pattern,"(Numero oculto)",texto)

print(remplazo)