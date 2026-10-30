frase = input("dime una frase:")
letra = input("dime una letra:")
contador = 0

lista = list(frase)

for i in range (0,len(frase)):
    if lista[i] == letra:
        contador= contador+1

print(f"la letra {letra} sale {contador} veces")