'''
n1 = int(input('Digite o primeiro peso: '))
n2 = int(input('Digite o segundo peso: '))
n3 = int(input('Digite o terceiro peso: '))
n4 = int(input('Digite o quarto peso: '))
n5 = int(input('Digite o quinto peso: '))
menor = n1
if n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5:
    menor = n2
if n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5:
    menor = n3
if n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5:
    menor = n4
if n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4:
    menor = n5
maior = n1
if n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5:
    maior = n2
if n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5:
    maior = n3
if n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5:
    maior = n4
if n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4:
    maior = n5
print(f'O menor peso é {menor}')
print(f'O maior peso é {maior}')
'''
'''
menor, maior = 0, 0
for p in range(1,6):
    peso = float(input(f'Peso da {p}ª pessoa: '))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi {menor}Kg')
'''
pesos = [float(input(f'Peso da {a}ª pessoa:')) for a in range(1,6)]
print(f'O maior peso foi de {max(pesos)}Kg \nO menor peso foi de {min(pesos)}Kg')