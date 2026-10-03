productos = input("dime los productos que llevas en la cesta: (separados por comas) ")

lista = productos.split(",")

for producto in lista:
    print(producto)