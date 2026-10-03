nombre =input("dime el nombre del producto: ")
precio = int(input("dime el precio del producto: "))
unidades =int(input("dime el unidades del producto: "))

coste_total = precio * unidades

print(nombre , "{precio:09.2f})" , "{unidades:03d}" , "{coste_total:08.2f}")

#POR ARREGLAR