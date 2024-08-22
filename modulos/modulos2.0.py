#si el modulo estubiera dentro de una carpeta en la misma ruta 
#import funciones_buenas.saludar as  m_saludar

import sys

sys.path.append("d:\\curso py\\funciones_buenas")

import saludar as modulo_saludo

print(modulo_saludo.saludar("Dalto"))
# print(m_saludar.saludar.saludar("lucas"))