interes = float(0.04)

capitalinicial = float(input("cantidad de dinero depositada: "))

capitalfinal1 = capitalinicial* (1 + interes) 
capitalfinal2 = capitalinicial* (1 + interes) ** 2
capitalfinal3 = capitalinicial* (1 + interes) ** 3

print (f"capital el primer año {round(capitalfinal1,2)}")
print (f"capital el segundo año {round(capitalfinal2,2)}")
print (f"capital el tercer año {round(capitalfinal3,2)}")

