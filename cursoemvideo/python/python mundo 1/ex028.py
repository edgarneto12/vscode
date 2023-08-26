from random import randrange
n = randrange(6)
i = int(input('Vamos brincar, imaginei um número entre 0 e 5 \nConsegue descobrir em qual número eu pensei? '))
if i == n:
    print('Droga, você ganhou de mim!')
else:
    print('Não foi dessa vez! Quem sabe na próxima.')
