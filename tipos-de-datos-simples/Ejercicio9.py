dinero = float(input("cantidad de dinero "))
interes = float(input("interes anual "))
anios = float(input("cantidad de años "))

capital = dinero * (1+ interes /100 ) ** anios 

print (f"Capital obtenido por la inversion:{capital}")










