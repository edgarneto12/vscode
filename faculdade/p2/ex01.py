somaaltura, mediaalturah, totmulher, listaaltura, tothomem  = 0, 0, 0, [], 0
for i in range(1, 16):
    print(f'-=-=- {i}ª Pessoa -=-=-')
    altura = float(input('Altura Ex:(1.70): '))
    sexo = input('Sexo [M/F]: ').strip()
    listaaltura.append(altura)
    if sexo in 'Mm':
        somaaltura += altura
        tothomem += 1    
    if sexo in 'Ff':
        totmulher += 1
        
if tothomem > 1:
    mediaalturah = somaaltura / tothomem 
    print(f'A maior altura informada é {max(listaaltura)} e a menor altura informada é {min(listaaltura)}.')
    print(f'A média de altura do grupo de homens é de {mediaalturah} metros.') 
    print(f'Ao todo são {totmulher} mulheres.')
else:
    print(f'A maior altura informada é {max(listaaltura)}M e a menor altura informada é {min(listaaltura)}M.')
    print('Não foi informado nenhum homem para calcular a média de altura de homens.') 
    print(f'Ao todo foram processadas {len(listaaltura)} pessoas e {totmulher} eram mulheres.')