class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        else:
            return None

    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]
        else:
            return None

    def esta_vazia(self):
        return len(self.items) == 0

def encontrar_vogais(palavra):
    vogais = "aeiouAEIOU"
    pilha = Pilha()
    vogais_encontradas = set()

    for letra in palavra:
        if letra in vogais:
            if letra.lower() not in vogais_encontradas:
                vogais_encontradas.add(letra.lower())
                pilha.empilhar(letra)

    return pilha

palavra = "Disciplina"
pilha_de_vogais = encontrar_vogais(palavra)

vogais_unicas = []
while not pilha_de_vogais.esta_vazia():
    vogais_unicas.append(pilha_de_vogais.desempilhar())

print("Vogais únicas na palavra:", vogais_unicas)
