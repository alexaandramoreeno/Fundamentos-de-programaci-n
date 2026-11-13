asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for i in asignaturas:
    nota = float(input(f"¿que has sacado en {i} ? "))
    if nota < 5:
        notas.append(nota)    

for j in range (0,len(notas),1):
    print(f"repites {asignaturas[j]} con un {notas[j]} ")
