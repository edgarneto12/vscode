estoque = [
    ["Camiseta", 25.99, 10],
    ["Calça", 59.99, 5],
    ["Tênis", 99.99, 3],
    ["Boné", 15.99, 20]
]

# nome do produto | Valor | Qtd Estoque
print('-'*16)
for produto in estoque:
    print(f'Produto: {produto[0]} | R$ {produto[1]} | Quant: {produto[2]}')
print('-'*16)