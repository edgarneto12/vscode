# solicitando número desejado para converter
numero = int(input('Digite o número decimal que você quer converter: '))
while True:
    # imprimindo layout com escolhas
    print('-' * 18)
    print('[1] Binário \n[2] Octal \n[3] Hexadecimal')
    print('-' * 18)
    # lendo a escolha do usuario
    base = int(input('Digite o número correspondente a base da conversão: '))
    if base == 1:
        print(f'{numero} em binário é {bin(numero)[2::]}')
        break
    elif base == 2:
        print(f'{numero} em octal é {oct(numero)[2::]}')
        break 
    elif base == 3:
        print(f'{numero} em hexadecimal é {hex(numero)[2::]}')
        break
    else:
        print('\033[31mDigite um número válido!\033[m')
        