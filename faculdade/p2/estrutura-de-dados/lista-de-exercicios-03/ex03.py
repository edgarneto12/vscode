import re

def e_palindromo(texto):
    # Remove espaços e pontuações do texto e converte para letras minúsculas
    texto = re.sub(r'[^a-zA-Z]', '', texto).lower()
    # Verifica se o texto é igual ao seu inverso
    return texto == texto[::-1]


frase = "A base do teto desaba"
if e_palindromo(frase):
    print(f'"{frase}" é um palíndromo.')
else:
    print(f'"{frase}" não é um palíndromo.')
