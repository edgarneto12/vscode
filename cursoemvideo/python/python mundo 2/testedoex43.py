peso, altura = float(input('Digite seu peso em kg(ex: 62.4): ')), float(input('Digite sua altura em metros(ex: 1.74)')) # solicitando o  peso e a altura do usuário
imc = peso / altura**2 # calculando imc
if imc < 18.5: 
    print(f'Seu imc é {imc:.2f}, logo você está abaixo do peso ideal!') # Imprimindo caso o imc for menor que 18.5
elif imc >= 18.5 and imc < 25:
    print(f'Seu imc é {imc:.2f}, logo você está no peso ideal!') # Imprimindo caso o imc estiver entre 18.5 e 25
elif imc >= 25 and imc < 30:
    print(f'Seu imc é {imc:.2f}, logo você está sobrepeso!') # Imprimindo caso o imc estiver entre 25 e 30
elif imc >= 30 and imc < 40:
    print(f'Seu imc é {imc:.2f}, logo você está em obesidade!') # Imprimindo caso o imc estiver entre 30 e 40
else: 
    print(f'Seu imc é {imc:.2f}, logo você está em obesidade mórbida!') # Imprimindo caso o imc for maior que 40
