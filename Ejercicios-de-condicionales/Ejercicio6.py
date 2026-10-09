nombre = input("dime tu nombre: ")
sexo = input("dime tu sexo (F/M): ")

inicial= nombre[:1]
print(inicial)

if ( inicial < "M" and sexo == "F") or (inicial > "M" and sexo == "M"):
    print ("grupo A")

else: 
    print ("grupo B")