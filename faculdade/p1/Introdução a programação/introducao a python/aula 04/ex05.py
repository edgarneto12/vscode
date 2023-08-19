n = int(input('Digite o número da conta: '))
s = float(input('Digite o saldo da conta: '))
d = float(input('Digite o débito da conta: '))
c = float(input('Digite o crédito da conta: '))
sa = ((s-d)+c)
print(f'{("-"*35)} \nConta nº{n} \nO saldo atual é de R${sa:.2f}')
if sa < 0:
    print(f'Saldo negativo! \n{("-"*35)}')
else:
    print(f'Saldo positivo! \n{("-"*35)}')
