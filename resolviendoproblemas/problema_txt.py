#2 listas, una con nombres otra con apellidos
nombres =["Lucas","Matias","Camila","Pedro","Roberto"]
apellido=["Dalto","Zing","Dalto","Robetix","Tarado"]

#rejistrar esta informacin en un TXT de forma optima
with open("resolviendoproblemas\\nombres_y_apellidos.txt","w") as arch:
    arch.writelines("los datos son:\n\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n---------\n") for n,a in zip(nombres,apellido)]
    
    