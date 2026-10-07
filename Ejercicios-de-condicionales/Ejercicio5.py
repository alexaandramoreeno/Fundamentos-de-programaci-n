edad = int(input("dime tu edad: "))
ingresos = float(input("dime tus ingresos mensuales: "))

if edad <= 16 or ingresos < 1000:
    print("no tiene que tributar")
else:
    print("tiene que tributar")