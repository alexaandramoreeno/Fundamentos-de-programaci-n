num = int(input("dime un numero > 1: "))
div = 0

for i in range (1,num+1,1):
    if num%i == 0:
        div = div + 1
    
if div == 2 :
    print(f"numero {num} es primo")
else:
    print(f"numero {num} no es primo")