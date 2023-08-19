palavra = str(input('Digite uma palavra:'))
def conta_vogais(string):
    vogais = "aeiouAEIOU"
    count= 0
    for char in string:
            if char in vogais:
                count += 1
    return count
contagem = conta_vogais(palavra)
print(f'A palavra que você digitou tem {contagem} vogais')
