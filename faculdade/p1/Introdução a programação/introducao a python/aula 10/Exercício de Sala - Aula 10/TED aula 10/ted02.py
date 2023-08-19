from collections import defaultdict
while True:
    try:
        VET = [int(input('Digite um número inteiro: ')) for a in range(10)]
        break
    except ValueError:
        print('Digite um número válido')
posicoes = defaultdict(list)
for posicao, valor in enumerate(VET):
    posicoes[valor].append(posicao)
print('Os números que se repetem são:')
for valor in posicoes:  
    if len(posicoes[valor]) > 1:
        print(f'{valor} se repete nas posiçoes: {posicoes[valor]}')
