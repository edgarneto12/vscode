numero, lista = int(input("Digite um número: ")), []
lista.append(numero)
while numero > 0:
    if numero%2 == 0:
        numero -= 2
        lista.append(numero)
    elif numero%2 != 0 and numero != 0:
        numero -= 1
        lista.append(numero)
print(f"Todos números pares até {lista[0]}: {lista}")
     