rentaAnual = float(input(" Cual es tu renta anual?: "))

if rentaAnual < 10000:
    print("te corresponde 5%")
elif 10000 <= rentaAnual < 20000:
    print("te corresponde 15%")
elif 20000 <= rentaAnual < 35000:
    print("te corresponde 20%")
elif 35000 <= rentaAnual < 60000:
    print("te corresponde 30%")
elif 60000 <= rentaAnual :
    print("te corresponde 45%")