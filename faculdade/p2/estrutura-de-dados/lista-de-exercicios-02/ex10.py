class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumentar_salario(self, percentual_aumento):
        if percentual_aumento > 0:
            self.salario += self.salario * (percentual_aumento / 100)
            return f"O salário de {self.nome} foi aumentado em {percentual_aumento}% para R${self.salario:.2f}"
        else:
            return "O percentual de aumento deve ser maior que zero."

funcionario1 = Funcionario("João", 5000, "Analista de Sistemas")
funcionario2 = Funcionario("Maria", 6000, "Gerente de Projetos")

print(funcionario1.aumentar_salario(10))
print(funcionario2.aumentar_salario(5))
