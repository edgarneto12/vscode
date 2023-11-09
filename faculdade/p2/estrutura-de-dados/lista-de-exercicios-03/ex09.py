def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Divisão por zero."
    return a / b

print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")

opcao = input("Opção (1/2/3/4): ")

numero1 = float(input("Insira o primeiro número: "))
numero2 = float(input("Insira o segundo número: "))

if opcao == "1":
    resultado = somar(numero1, numero2)
    operacao = "adição"
elif opcao == "2":
    resultado = subtrair(numero1, numero2)
    operacao = "subtração"
elif opcao == "3":
    resultado = multiplicar(numero1, numero2)
    operacao = "multiplicação"
elif opcao == "4":
    resultado = dividir(numero1, numero2)
    operacao = "divisão"
else:
    resultado = "Opção inválida."
    operacao = ""

if operacao:
    print(f"Resultado da {operacao}: {resultado:.2f}")
else:
    print(resultado)
