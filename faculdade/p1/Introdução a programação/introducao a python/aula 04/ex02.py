n1 = float(input('Digitar a primeira nota: '))
n2 = float(input('Digitar a segunda nota: '))
nf = ((n1 + n2) / 2)
if nf >= 6:
    print(f'A média é {nf:.1f}, aprovado.')
if nf < 6:
    print(f'A média é {nf:.1f}, reprovado.')
