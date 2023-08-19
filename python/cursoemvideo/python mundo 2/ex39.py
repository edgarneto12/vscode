from datetime import date
ano = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - ano
faltam = 18 - idade
passaram = idade - 18
if idade < 18:
    print(f'Você ainda vai se alistar em {faltam} anos.')
elif idade == 18:
    print('Está na hora de você se alistar.')
else:
    print(f'Já passou {passaram} anos do tempo de você se alistar.')
