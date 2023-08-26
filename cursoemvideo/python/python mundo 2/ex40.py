n1 = float(input('Digitar a primeira nota: '))
n2 = float(input('Digitar a segunda nota: '))
nf = ((n1 + n2) / 2)
if nf < 5:
    print(f'Média {nf:.1f}, REPROVADO')
elif nf < 6.9:
    print(f'Média {nf:.1f}, RECUPERAÇÃO')
elif nf >= 7:
    print(f'Média {nf:.1f}, APROVADO')
else:
    print('Número inválido')
