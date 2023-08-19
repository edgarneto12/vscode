termo = int(input('Digite o primeiro termo: ')) # Solicitando o primeiro termo para o usuário
razao = int(input('Digite a razão: ')) # Solicitando a razão para o usuário
for n in range(1,11): # Criando repetição for com a quantidade de termos
    print(f'{n}º termo: {termo + (n - 1) * razao}') # Imprimindo um intervalo de 10 termos