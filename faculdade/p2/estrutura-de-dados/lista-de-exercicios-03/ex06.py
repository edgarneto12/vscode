texto = input("Insira um texto: ")

contador_vogais = 0

texto = texto.lower()

for caractere in texto:
    if caractere in "aeiou":
        contador_vogais += 1

print(f"A quantidade de vogais na string é: {contador_vogais}")
