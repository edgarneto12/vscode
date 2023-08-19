s = float(input('Digite seu salário: R$'))
if s < 1251:
    print(f'Seu salário será R${s+(s*15/100)}')
else:
    print(f'Seu salário será R${s+(s*10/100)}')
