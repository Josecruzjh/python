#inportando un modulo y asignandole el  nombre "m_saludar"
#import modulo_saludar as m_saludar

#desde ese modulo inportamos 2 funciones
from modulos.funciones_buenas.saludar import saludar as saludar_normal,saludar_raro as saludar_como_coscu
# import modulo_saludar as m_saludar

#creamos las variables  con los resultados
saludo = saludar_normal("lucas")
saludar_raro = saludar_como_coscu("frank")


#mostramos los resultados
print (saludo)
print (saludar_raro)

# para ver las propiedades y metodos de el namespace
# print(dir(m_saludar))

# saludo = modulo_saludar.saludar("lucas")
# print (saludo)

#accedemos al nombre de este modulo
print(__name__)

