#promedio de duracion

ostros_cursos_min = 2.5
ostros_cursos_max = 7
ostros_cursos_promedio = 4
dalto_curso = 1.5

#duracion de crudo
crudo_promedio = 5
crudo_dalto = 3.5

#diferencia de duracion 
diferencia_con_min = 100 - dalto_curso / ostros_cursos_min * 100
diferencia_con_max = 100 - dalto_curso *1000 // ostros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso / ostros_cursos_promedio * 100

#calculando el porsentaje de tiempo vacio removido
iempo_vacio_promedio = 100 - ostros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 -dalto_curso * 1000 // crudo_dalto /10

#mostrando las diferencias de duracion( ejercicio A)
print("------------")
print("el cuso de dalto dura :")
print(f'- un {diferencia_con_min}% menos que el mas raoido')
print(f'- un {diferencia_con_max}% menos que el mas raoido')
print(f'- un {diferencia_con_promedio}% menos que el mas raoido')
print("------------")

#Mostrar la cantidad de espacios vacíos que se remueven ejercicio b)
print(f'el curso promedio elimina un  {iempo_vacio_promedio}%de tiempovacio')
print(f'el curso promedio elimina el {tiempo_vacio_dalto}%de tiempovacio')
print("------------")

#mostrardiferencias si los cursos duran 10 horas
print(f'Ver 10 horas de este curso equivalente a ver  {ostros_cursos_promedio * 1000 // dalto_curso / 10}hora de otros cursos')
print(f'Ver 10 horas de este curso equivalente a ver  {dalto_curso * 1000 // ostros_cursos_promedio / 10}hora de otros curso')
print("------------")