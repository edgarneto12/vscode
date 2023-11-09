try:
    numero = int(input("Insira um número inteiro positivo: "))
    if numero < 0:
        print("Por favor, insira um número inteiro positivo.")
    else:
        numero_str = str(numero)
        soma = 0

        for digito in numero_str:
            soma += int(digito)

        print(f"A soma dos dígitos de {numero} é {soma}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
