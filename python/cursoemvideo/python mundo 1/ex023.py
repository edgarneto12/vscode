'''n = str(input("Digite um número inteiro de 0 a 9999: "))
print(f'Unidade: {n[3]}')
print(f'Dezena: {n[2]}')
print(f'Centena: {n[1]}')
print(f'Milhar: {n[0]}')'''
n = int(input('Digite um número inteiro entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena {d}')
print(f'Centena {c}')
print(f'Milhar: {m}')