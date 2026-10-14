puntuacion = float(input("Dime tu puntuación: "))

if(puntuacion == 0):
    print("tu nivel de rendimiento es: inaceptable")
    print(f"dinero: {puntuacion * 2.400+2400}")
elif(puntuacion == 0.4):
    print("tu nivel de rendimiento es: Aceptable")
    print(f"dinero: {(puntuacion * 2.400)+2400}")
elif (puntuacion >= 0.6): 
    print("tu nivel de rendimiento es: meritorio")
    print(f"dinero: {(puntuacion * 2.400)+2400}")