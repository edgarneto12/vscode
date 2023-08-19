from datetime import date
c, maior, menor = 0, 0, 0
while True:
    try:
        ano = int(input('Digite o ano de nascimento: '))
        if ano < 1900 or ano > date.today().year:
            print('Insira um número válido! ex: 1995')    
        else:
            idade = date.today().year - ano
            c = c + 1
            if idade >= 18:
                maior = maior + 1
            else:
                menor = menor + 1
            if c == 7:
                break     
    except ValueError:
        print('Insira um número válido! ex: 1995')
print(f'Das sete pessoas {maior} são de maior de idade e {menor} são de menor')
