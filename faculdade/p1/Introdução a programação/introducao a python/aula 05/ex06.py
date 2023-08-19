convidados = ['Ednaldo Pereira', 'Caneta Azul', 'Luva de Pedreiro', 'Victor', 'Sofia']
print(f"Lista dos que serão convidados:")
convidados.sort()
num = 1
for convidado in convidados:
    print(f"{num}. {convidado}")
    num += 1
naocomp = input("Quem não poderá comparecer ao jantar? ")
naocomp = naocomp.title()
if naocomp in convidados:
    convidados.remove(naocomp)
    print(f"O convidado {naocomp} foi removido da lista")
else:
    print(f"{naocomp} não está na lista de convidados")
while True:
    print("A lista atual ficou: ")
    num = 1
    convidados.sort()
    for convidado in convidados:
        print(f"{num}. {convidado}")
        num += 1
    remove = input("Deseja Remover mais alguém? ")
    if remove == "sim":
        naocomp = input("Quem deseja remover da lista? ")
        naocomp = naocomp.title()
        if naocomp in convidados:
            convidados.remove(naocomp)
            print(f"O convidado {naocomp} foi removido da lista")
        else:
            print(f"{naocomp} não está na lista de convidados.")
    elif remove == "nao":
        break
    else:
        print("\033[31mPor favor responda com sim ou nao\033[0;0m")
print("A lista autal ficou:")
num = 1
convidados.sort()
for convidado in convidados:
    print(f"{num}. {convidado}")
    num += 1
while True:
    add = input("Deseja Adicionar mais alguém? ")
    if add == "sim":
        add = input("Quem quer adicionar? ")
        add = add.title()
        convidados.append(add)
        print(f"O convidado {add} foi adicionado")
    elif add == "nao":
        break
    else:
        print("\033[31mPor favor responda com sim ou nao\033[0;0m")
print("Os convites foram enviados para os seguintes convidados: ")
num = 1
convidados.sort()
for convidado in convidados:
    print(f"{num}. {convidado}")
    num += 1
    print(f"Olá {convidado}, você está sendo convidado para um jantar em minha casa!")
