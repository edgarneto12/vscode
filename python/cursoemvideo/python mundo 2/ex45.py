from random import randrange
from time import sleep
teste = ['Processando.', 'Processando..', 'Processando...',]
print('Vamos jogar pedra, papel e tesoura!')
print('-' * 18)
print('[1] Pedra \n[2] Papel \n[3] Tesoura')
print('-' * 18)
while True:
    usuario = int(input('Digite o número correspondente a sua escolha: '))
    maquina = randrange(1,4)
    if usuario < 1 or usuario > 3:
        print('Digite um número válido.')
    elif usuario >= 1 and usuario <= 3:
        break
#print(f'Debug \nusuario:{usuario} \nmaquina:{maquina}')
print('Jo \n Ken \n  Po')
for l in teste:
    print(l, end="\r")
    sleep(1)
if maquina == 1 and usuario == 1:
    print('Houve um empate!  \nEscolha da máquina: Pedra \nSua escolha: Pedra')
elif maquina == 1 and usuario == 2:
    print('Você ganhou!  \nEscolha da máquina: Pedra \nSua escolha: Papel')
elif maquina == 1 and usuario == 3:
    print('Você perdeu!  \nEscolha da máquina: Pedra \nSua escolha: Tesoura')
elif maquina == 2 and usuario == 1:
    print('Você Perdeu!  \nEscolha da maquina: Papel \n Sua escolha: Pedra')
elif maquina == 2 and usuario == 2:
    print('Houve um empate!  \nEscolha da máquina: Papel \nSua escolha: Papel')
elif maquina == 2 and usuario == 3:
    print('Você Ganhou!  \nEscolha da máquina: Papel \nSua Escolha: Tesoura')
elif maquina == 3 and usuario == 1:
    print('Você Ganhou!  \nEscolha da máquina: Tesoura \nSua escolha: Pedra')
elif maquina == 3 and usuario == 2:
    print('Você perdeu!  \nEscolha da máquina: Tesoura \nSua escolha: Papel')
elif maquina == 3 and usuario == 3:
    print('Houve um empate!  \nEscolha da máquina: Tesoura \nSua escolha: Tesoura')
elif usuario > 4 or usuario < 1:
    print('Digite um número válido.')
