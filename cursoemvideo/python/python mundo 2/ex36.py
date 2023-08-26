# solicitando o valor da casa
valor_casa = float(input('Digite o valor da casa: R$'))
# solicitando o salario
salario = float(input('Digite o seu salário: R$'))
# solicitando em quantos anos ele quer pagar
anos = float(input('Em quantos anos deseja pagar a sua casa? '))
# transformando os anos em meses
meses = anos * 12
# calculando a prestação
mensal = valor_casa / meses
# calculando 30% do salario
porcentagem = salario * 0.3
# imprimindo o quanto ele terá que pagar por mes
print(f'Para pagar uma casa de R${valor_casa:.2f} em 7 anos a prestação será de R${mensal:.2f}')
# verificando se ele pode pagar pela casa com uma margem de 30% do salario 
if mensal < porcentagem:
    print(f'Parabéns, seu empréstimo foi aceito.')
else:
    print('Infelizmente seu empréstimo foi negado')
