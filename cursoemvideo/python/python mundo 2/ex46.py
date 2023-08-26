from time import sleep
contagem = ['10','9','8','7','6','5','4','3','2','1','0']
for c in contagem:
    print(c, end=' \r')
    sleep(1)
print('🎆')