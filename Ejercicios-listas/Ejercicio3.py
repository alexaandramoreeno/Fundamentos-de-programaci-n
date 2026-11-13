asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
for i in asignaturas:
    nota = input(f"¿que has sacado en {i} ? ")
    notas.append(nota)

for j in range (0,len(asignaturas),1):
    print(f"has sacado un {notas[j]} en {asignaturas[j]}")

