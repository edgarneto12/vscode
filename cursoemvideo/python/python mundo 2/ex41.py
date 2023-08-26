from datetime import date
ano = int(input('Digite o ano em que você nasceu: '))
idade = date.today().year - ano
if idade <= 9:
    print('Você está na classificação MIRIM')
elif idade <= 14:
    print('Você está na classificação INFANTIL')
elif idade <= 19:
    print('Você está na classificação JUNIOR')
elif idade <= 20:
    print('Você está na classificação SÊNIOR')
else:
    print('Você está na classificação MASTER')