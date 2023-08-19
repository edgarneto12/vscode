a = input("Sou um analisador de palíndromos! \nDigite algo para analisar-lo: ")
if a.lower() == a[::-1].lower():
    print(f"Meus estudos dizem que {a} é um palíndromo!")
else:
    print(f"Meus estudos dizem que {a} não é um palíndromo...")
