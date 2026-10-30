num = int(input("Dime un número entero: "))
vector = []

for i in range(1, num + 1, 2):
    
    # Metemos el número actual al principio de la lista para que 
    # quede al revés
    vector.insert(0, i)
    for numero in vector: #imprimimos 
        print(numero, end=" ")
        
    print() # Hacemos un salto de línea 