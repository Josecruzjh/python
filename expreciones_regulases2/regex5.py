import re 

text = "Este es un ejempolo de una pajina web: https://www.exaple.com y tambien podemos "

pattern="https?://[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

result = re.match(pattern, text)

print(result)