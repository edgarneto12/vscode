def calcular_media(lista):
    soma = sum(lista)
    media = soma / len(lista)
    return media

numeros = [10, 20, 30, 40, 50]
media = calcular_media(numeros)
print(f"A media é: {media}")