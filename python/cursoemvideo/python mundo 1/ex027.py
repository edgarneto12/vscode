nome = input('Digite seu nome completo: ').strip()
nomelista = nome.split()
print(f'Primeiro nome: {nomelista[0]}')
print(f'Último nome: {nomelista[len(nomelista)-1]}')
