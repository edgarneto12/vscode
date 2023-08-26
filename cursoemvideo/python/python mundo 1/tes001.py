while True:
    n1 = float(input('Digitar a primeira nota: '))
    if n1 > 10:
        print('Número invalido, tente um número entre 0 e 10')
        break
    else:
     continue
n2 = float(input('Digitar a segunda nota: '))
if n2 > 10:
        print('Número invalido, tente um número entre 0 e 10')
        exit()
nf = ((n1 + n2) / 2)
if nf >= 6:
        print(f'A média é {nf:.1f}, aprovado.')
if nf < 6:
        print(f'A média é {nf:.1f}, reprovado.')

