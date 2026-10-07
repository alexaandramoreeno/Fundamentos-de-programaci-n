nombre =input("dime el nombre del producto: ")
precio = float(input("dime el precio del producto: "))
unidades =int(input("dime el unidades del producto: "))

coste_total = precio * unidades

print(f"nombre , {precio:9.2f} , {unidades:3d} , {coste_total:11.2f}")
