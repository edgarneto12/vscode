print(f'Preço da maça: R$1,30 a partir de 12 unidades: R$1,0 Cada')
macas = int(input('Quantas maças vai querer? '))
preco = macas * 1.3
precodesconto = macas * 1
if macas < 1:
    print(f'Como assim você quer comprar {macas} maças?')
elif macas == 1:
    print(f'O preço de {macas} maça é R${preco:.1f}')
elif macas < 12:
    print(f'O preço de {macas} maças é R${preco:.1f}')
else:
    print(f'O preço de {macas} maças é R${precodesconto:.1f}')
