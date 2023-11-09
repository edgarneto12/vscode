def calcular_fatorial(numero):
    if numero < 0:
        return "Número negativo não tem fatorial."
    elif numero == 0:
        return 1
    else:
        resultado = 1
        for i in range(1, numero + 1):
            resultado *= i
        return resultado

try:
    numero = int(input("Insira um número inteiro positivo: "))
    resultado = calcular_fatorial(numero)
    print(f"{numero}! = {resultado}")
except ValueError:
    print("Por favor, insira um número inteiro válido.")
