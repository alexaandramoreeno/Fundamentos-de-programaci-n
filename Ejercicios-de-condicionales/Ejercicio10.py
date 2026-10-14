opcion = input("Pizza vegetariana (1) / Pizza no vegetariana (2): ")

if (opcion == "1"):
    print("Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas")
    opcion2 = input("Ingredientes vegetarianos: Pimiento(1) y tofu(2).")
    if(opcion2 == "1"):
        print("tu pizza lleva Tomate Mozarella y Pimiento")
    elif(opcion2 == "2"):
        print("tu pizza lleva Tomate Mozarella y Tofu")
    else:
        print("opcion no valida")
elif (opcion == "2"):
    print("Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en todas las pizzas")
    opcion2 = input("Ingredientes no vegetarianos: Peperoni(1), Jamón(2) y Salmón(3)")
    if(opcion2 == "1"):
        print("tu pizza lleva Tomate Mozarella y Pepperoni")
    elif(opcion2 == "2"):
        print("tu pizza lleva Tomate Mozarella y jamón")
    elif(opcion2 == "3"):
        print("tu pizza lleva Tomate Mozarella y Salmón")
    else:
        print("opcion no valida")
else:
    print("Váyase de aqui :)")
