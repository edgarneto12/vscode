quantatual = int(input('Qual o estoque atual? '))
quantmax = int(input('Qual é o max. do estoque? '))
quantmin = int(input('Qual é o min. do estoque? '))
quantmed = ((quantmax + quantmin) / 2)
quantnec = (quantmed - quantatual)
if quantatual >= quantmed:
    print('Não é necessário efetuar a compra de mais itens.')
if quantatual < quantmed:
    print(f'É necessário efetuar a compra de {quantnec:.0f} uni.')
