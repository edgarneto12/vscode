valor_compra = float(input("Digite o valor da compra: "))
idade_cliente = int(input("Digite sua idade: "))

if idade_cliente >= 60:
    valor_desconto = valor_compra * 0.15
else:
    valor_desconto = valor_compra * 0.1
valor_final = valor_compra - valor_desconto
print(f"O valor final da compra é {valor_final}")