vetor = [3,8,7,2,6,1]

n = len(vetor)
print(vetor)

for i in range(n):
    for j in range(0,n-i-1):
        if vetor[j]>vetor[j+1]:
            aux=vetor[j]
            vetor[j]=vetor[j+1]
            vetor[j+1]=aux
print(vetor)