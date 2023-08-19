while True:
    try:
        numeros = [int(input('Digite um número inteiro: ')) for a in range(20)]
        break
    except ValueError:
        print('Digite um número válido')
numeros.reverse()
print(numeros)
