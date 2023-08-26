d = float(input('Quantos dias você ficou com o carro? '))
k = float(input(f'Quantos km você rodou no período de {d:.0f} dias? '))
print(f'Valor a pagar pelo aluguel: R${((d*60)+(k*0.15)):.2f}')
