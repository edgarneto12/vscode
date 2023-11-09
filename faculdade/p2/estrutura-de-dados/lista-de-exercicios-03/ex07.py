def calcular_imc(peso, altura):
    if altura <= 0:
        return "A altura deve ser maior que zero."
    
    imc = peso / (altura ** 2)
    return imc

peso = float(input("Insira o peso (em quilogramas): "))
altura = float(input("Insira a altura (em metros): "))

resultado_imc = calcular_imc(peso, altura)

if isinstance(resultado_imc, str):
    print(resultado_imc)
else:
    print(f"O IMC é {resultado_imc:.2f}")
