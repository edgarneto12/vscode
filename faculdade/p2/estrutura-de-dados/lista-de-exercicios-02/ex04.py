class ContaBancaria:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}"
        else:
            return "Valor de depósito inválido. O valor deve ser maior que zero."

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado com sucesso. Novo saldo: R${self.saldo:.2f}"
        elif valor <= 0:
            return "Valor de saque inválido. O valor deve ser maior que zero."
        else:
            return "Saldo insuficiente para efetuar o saque."


conta = ContaBancaria("João da Silva", 1000.0)
print(conta.depositar(500.0))
print(conta.sacar(200.0))
