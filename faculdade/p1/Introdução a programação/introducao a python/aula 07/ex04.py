n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
n4 = float(input('Digite a quarta nota: '))
nf = ((n1 + n2 + n3 + n4) / 4)
if nf >= 7:
    print(f'A média é {nf:.1f}, aprovado.')
if nf < 7:
    print(f'A média é {nf:.1f}, reprovado.')
