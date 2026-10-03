fecha = input("dime tu fecha de nacimiento dd/mm/aaaa: ")

#OTRA MANERA:
#dia, mes, anio = fecha.split("/")
#print("dia: " + dia + " mes: " + mes + " año: " + anio)

lista = fecha.split("/")
print("dia: " , lista[0] , " mes: " , lista[1] , " año: ", lista[2])

#ejercicio adaptado a enteros
lista = fecha.split("/")
print("dia: " , int(lista[0]) , " mes: " , int(lista[1]) , " año: " , int(lista[2]))
