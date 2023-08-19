n = input("Digite seu nome: ")
i = int(input("Digite sua idade: "))
if i >= 18:
    print(f"{n.title()} é apto para dirigir um veículo")
else:
    print(f"{n.title()} não é apto para dirigir um veículo")
