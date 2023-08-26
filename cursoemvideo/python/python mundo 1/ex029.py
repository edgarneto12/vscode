v = int(input('Velocidade do veículo: '))
lim = v - 80
if v < 80:
    print('O veículo não ultrapassou o limite da via.')
else:
    print(f'O veículo ultrapasssou {lim}km/h do limite \nLogo foi multado em R${lim*7}')
