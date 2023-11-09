def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

opcao = input("Escolha a conversão:\n1. Celsius para Fahrenheit\n2. Fahrenheit para Celsius\nOpção: ")

if opcao == "1":
    celsius = float(input("Insira a temperatura em Celsius: "))
    fahrenheit = celsius_para_fahrenheit(celsius)
    print(f"{celsius} graus Celsius equivalem a {fahrenheit:.2f} graus Fahrenheit.")
elif opcao == "2":
    fahrenheit = float(input("Insira a temperatura em Fahrenheit: "))
    celsius = fahrenheit_para_celsius(fahrenheit)
    print(f"{fahrenheit} graus Fahrenheit equivalem a {celsius:.2f} graus Celsius.")
else:
    print("Opção inválida. Escolha 1 para Celsius para Fahrenheit ou 2 para Fahrenheit para Celsius.")
