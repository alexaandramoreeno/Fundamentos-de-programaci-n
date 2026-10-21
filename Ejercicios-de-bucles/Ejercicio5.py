cant = float(input("que cantidad quieres invertir?: "))
interes = float(input("que interes anual: "))
anios = int(input("numero de años: "))

interes = cant * (interes/100)

for i in range (1,anios+1,1):
    cant = cant + interes
    print(f"año {i}, cantidad: {cant}")

