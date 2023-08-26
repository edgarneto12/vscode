t = 0
c = 0
while True:
    n = int(input('Digite um número inteiro:'))
    c = c + 1
    if n % 2 == 0:
        t = t + n    
    if c == 6:
            break
    print(t, n)
print(f'A soma de todos números pares é: {t}')
