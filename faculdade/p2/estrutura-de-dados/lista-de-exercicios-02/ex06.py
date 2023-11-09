class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_total(self):
        return self.preco * self.quantidade

produto1 = Produto("Camiseta", 20.0, 3)
produto2 = Produto("Tênis", 50.0, 2)

total1 = produto1.calcular_total()
total2 = produto2.calcular_total()

print(f"Total do {produto1.nome}: R${total1:.2f}")
print(f"Total do {produto2.nome}: R${total2:.2f}")
