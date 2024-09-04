listap, listai = [], []

for i in range(210,512,2):
    listap.append(i)
    listai.append(i-1)
    
print(f'Lista dos valores pares: \n{listap} \nO número de elementos é: {len(listap)} \nA soma dos elementos é: {sum(listap)} \nA média dos elementos é: {sum(listap)/len(listap)} \nO maior elemento é: {max(listap)} \nO menor elemento é: {min(listap)} \n----------------------')

print(f'Lista dos valores ímpares: \n{listai} \nO número de elementos é: {len(listai)} \nA soma dos elementos é: {sum(listai)} \nA média dos elementos é: {sum(listai)/len(listai)} \nO maior elemento é: {max(listai)} \nO menor elemento é: {min(listai)}')