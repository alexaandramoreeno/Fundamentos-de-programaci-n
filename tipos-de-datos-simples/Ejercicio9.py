dinero = int(input("cantidad de dinero "))
interes = int(input("interes anual "))
anios = int(input("cantidad de años "))

capital = dinero * (1+ interes /100 ) ** anios 

print (f"Capital obtenido por la inversion:{capital}")










