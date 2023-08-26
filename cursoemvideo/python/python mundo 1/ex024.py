cidade = input('Digite um nome de uma cidade: ').strip()
temsanto = cidade.lower().find('santo')
if temsanto == 0:
    print('O nome da sua cidade começa com santo.')
else:
    print('O nome da sua cidade não começa com santo.')
