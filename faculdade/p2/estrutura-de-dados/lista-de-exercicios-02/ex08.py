class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

aluno1 = Aluno("João", [8.5, 7.0, 9.5, 6.5])
aluno2 = Aluno("Maria", [9.0, 8.0, 8.5, 7.5])

media1 = aluno1.calcular_media()
media2 = aluno2.calcular_media()

print(f"A média de notas do aluno {aluno1.nome} é {media1:.2f}")
print(f"A média de notas do aluno {aluno2.nome} é {media2:.2f}")
