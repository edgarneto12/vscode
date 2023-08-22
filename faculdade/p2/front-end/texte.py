altura_maior = 0
altura_menor = 0
soma_altura_homem = 0
qtd_mulheres = 0

for i in range(3):
    altura = float(input(f"Digite a altura em metros da pessoa {i+1}: "))
    genero = input(f"Digite o gênero da pessoa {i+1} (M/F): ")

    if i == 0:
        altura_maior = altura
        altura_menor = altura
    else:
        if altura > altura_maior:
            altura_maior = altura
        if altura < altura_menor:
            altura_menor = altura

    if genero.upper() == 'M':
        soma_altura_homem += altura
    elif genero.upper() == 'F':
        qtd_mulheres += 1

media_altura_homens = soma_altura_homem / (3 - qtd_mulheres)

print("Maior altura informada: {:.2f} metros".format(altura_maior))
print("Menor altura informada: {:.2f} metros".format(altura_menor))
print("Média de altura dos homens: {:.2f} metros".format(media_altura_homens))
print("Quantidade de mulheres: {}".format(qtd_mulheres))
