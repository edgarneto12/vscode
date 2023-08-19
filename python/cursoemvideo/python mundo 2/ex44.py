precooriginal = float(input('Digite o preço do produto (ex: 5.45): R$')) # Solicitando o preço original do produto
print('-' * 18)
print('[1] À Vista \n[2] Crédito 1x \n[3] Crédito 2x \n[4] Crédito 3x ou mais') # Imprimindo escolhas para forma de pagamento
print('-' * 18)
while True:
    try:
        formadepg = int(input('Digite o número correspondente a forma de pagamento: ')) # Solicitando escolha da forma de pagamento
        if formadepg == 1:
            print(f'Valor a pagar: R${precooriginal * 0.9}') # Imprimindo preço caso a forma de pagamento seja à vista 
            break
        elif formadepg == 2:
            print(f'Valor a pagar: R${precooriginal * 0.95}') # Imprimindo preço caso a forma de pagamento seja à prazo em 1x
            break
        elif formadepg == 3:
            print(f'Valor a pagar: R${precooriginal}') # Imprimindo preço caso a forma de pagamento seja à prazo em 2x
            break
        elif formadepg == 4:
            print(f'Valor a pagar: R${precooriginal * 1.2}') # Imprimindo preço caso a forma de pagamento seja à prazo em 3x ou mais
            break
        else:
            print('INSIRA UM NÚMERO VÁLIDO!') # Imprimindo erro caso o numero escolhido não exista nas escolhas 
    except ValueError:
        print('INSIRA UM NÚMERO VÁLIDO!')
        