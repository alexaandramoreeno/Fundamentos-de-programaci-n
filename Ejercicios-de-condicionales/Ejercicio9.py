edad = int(input("dime tu edad: "))
if (0 <= edad < 4 ):
    print("entra gratis")
elif (4 <= edad <= 18):
    print("paga 5€")
elif (18 < edad ):
    print("paga 10€")
else:
    print("no existen edades negativas")