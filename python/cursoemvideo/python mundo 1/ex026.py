frase = input('Digite uma frase: ').strip()
print(f'Sua frase tem {frase.lower().count("a")} letras a')
print(f'A posição da primeira letra a: {frase.lower().find("a")+1}')
print(f'A posição da última letra a: {frase.lower().rfind("a")+1}')
