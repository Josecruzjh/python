ingreso_mensual = 81000
gasto_mesual= 80000

#if animados y else if(elif)

if ingreso_mensual > 10000: 
    if ingreso_mensual - gasto_mesual < 0:
        print("estas en deficit")
    elif ingreso_mensual - gasto_mesual < 3000:
        print("bien pa estas bien") 
    else:
        print("estas gastando una banda ,hay que ber si te calcanza")

if ingreso_mensual > 1000 :
    print("esta bien en cuaquier patre del mundo")

elif ingreso_mensual > 1000:
    print("esta bien en latinoamerica")
    
elif ingreso_mensual > 500:
    print("esta bien en arjentina")
elif ingreso_mensual > 200:
    print("esta bien en venenzuela")

else:
    print("son pobres")