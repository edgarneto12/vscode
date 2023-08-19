nome_arquivo = 'vasco.txt'

with open(nome_arquivo, 'w', encoding='UTF-8') as file:
    file.write('Vamos todos cantar de coração!\n')
    file.write('Precisa trocar o Técnico!\n')
    print('Processamento finalizado...')

with open(nome_arquivo, 'a', encoding='UTF-8') as file:
    file.write('Esse time é muito ruim!!!\n')
    
with open(nome_arquivo, 'r', encoding='UTF-8') as file:
    conteudo = file.read()
    print(conteudo)
