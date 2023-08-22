numero, resultado, contador = int(input("Digite um número inteiro: ")), 1 , 1
while contador <= numero:
    resultado *= contador
    contador +=1
print(f"Farotial de {numero} é {resultado}")
