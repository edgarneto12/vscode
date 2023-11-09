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

def encontrar_operadores(expressao):
    operadores = set("+-*/^()")

    pilha = Pilha()
    operadores_encontrados = set()

    for caractere in expressao:
        if caractere in operadores:
            if caractere == ")":
                while not pilha.esta_vazia() and pilha.topo() != "(":
                    operadores_encontrados.add(pilha.desempilhar())
                pilha.desempilhar()  # Desempilha o "(" correspondente
            elif caractere == "(":
                pilha.empilhar(caractere)
            else:
                while not pilha.esta_vazia() and prioridade(caractere) <= prioridade(pilha.topo()):
                    operadores_encontrados.add(pilha.desempilhar())
                pilha.empilhar(caractere)

    while not pilha.esta_vazia():
        operadores_encontrados.add(pilha.desempilhar())

    return operadores_encontrados

def prioridade(operador):
    if operador in "*/^":
        return 2
    elif operador in "+-":
        return 1
    else:
        return 0

expressao = "(2+3)*(8-9)/(7^3)"
operadores_encontrados = encontrar_operadores(expressao)
print("Operadores matemáticos encontrados na expressão:", operadores_encontrados)
