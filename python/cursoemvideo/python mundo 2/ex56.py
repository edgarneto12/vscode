somaidade, mediaidade, maioridadedehomem , nomevelho, totmulher20 = 0, 0, 0, '', 0
for i in range(1, 5):
    print(f'-=-=- {i}ª Pessoa -=-=-')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()
    somaidade += idade
    if i == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print(f'A média de idade do grupo é de {mediaidade} anos.') 
print(f'O homem mais velho tem {maioridadedehomem} anos e se chama {nomevelho}.')
print(f'Ao todo são {totmulher20} mulheres tem menos de 20 anos.')
