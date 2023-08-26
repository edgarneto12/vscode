d = int(input('Qual será a distância da viagem em km? '))
if d < 201:
    print(f'O preço da viagem será de R${d*0.50}')
else:
    print(f'O preço da viagem será de R${d*0.45}')