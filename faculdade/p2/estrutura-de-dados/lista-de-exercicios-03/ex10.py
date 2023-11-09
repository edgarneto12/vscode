def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    sequencia = [0, 1]
    while len(sequencia) < n:
        proximo = sequencia[-1] + sequencia[-2]
        sequencia.append(proximo)
    
    return sequencia

num_termos = int(input("Insira o número de termos desejado na sequência de Fibonacci: "))

resultado = fibonacci(num_termos)
print("Sequência de Fibonacci:")
print(resultado)
