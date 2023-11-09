class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def detalhes(self):
        return f"Carro: {self.marca} {self.modelo}, Ano: {self.ano}"

meu_carro = Carro("Ford", "Mustang", 2022)
carro_amigo = Carro("Toyota", "Corolla", 2021)

print(meu_carro.detalhes())
print(carro_amigo.detalhes())
