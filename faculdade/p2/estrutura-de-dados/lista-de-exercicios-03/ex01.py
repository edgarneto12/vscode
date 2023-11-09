notas = []
for i in range(5):
    nota = float(input(f"Insira a nota {i + 1}: "))
    notas.append(nota)

media = sum(notas) / len(notas)

if media >= 7:
    print(f"Média: {media:.2f}. Aluno Aprovado!")
else:
    print(f"Média: {media:.2f}. Aluno Reprovado.")