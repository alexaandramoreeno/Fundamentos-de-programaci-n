peso = float(input("Dime tu peso en kg:"))
altura = float(input("Dime tu altura en metros:"))
imc = peso / (altura)**2

print (f"tu imc es {round(imc,2)}")