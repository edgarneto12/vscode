n = int(input('Digite um número inteiro: '))
if n == 2 or n == 3 or n == 5 or n == 7:
    print(f'{n} é Primo')
elif n != 1 and n % 2 != 0 and n % 3 != 0 and n % 5 != 0 and n % 7 != 0:
    print(f'{n} é primo')
else:
    print(f'{n} não é primo')