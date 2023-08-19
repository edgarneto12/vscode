nome = input('Digite seu nome: ').strip()
temsilva = 'silva' in nome.lower()
if temsilva is True:
    print('Tem silva no seu nome.')
else:
    print('Não tem silva no seu nome.')
