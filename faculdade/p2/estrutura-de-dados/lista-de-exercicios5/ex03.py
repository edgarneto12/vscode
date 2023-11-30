import time
import random

def bubble_sort(vetor):
  n=len(vetor)
  for i in range(n):
    for j in range(0,n-i-1):
      if vetor[j]>vetor[j+1]:
        aux=vetor[j]
        vetor[j]=vetor[j+1]
        vetor[j+1]=aux
  return (vetor)

def select_sort(vetor):
  n=len(vetor)
  for i in range(n):
    id_min=i
    for j in range(i+1,n):
      if vetor[id_min]>vetor[j]:
        id_min=j
    aux=vetor[i]
    vetor[i]=vetor[id_min]
    vetor[id_min]=aux
  return (vetor)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

vetor = [random.randint(1, 1000) for _ in range(1000)]

# Tempo de Execução Bubble Sort
inicio = time.time()
resultado = bubble_sort(vetor)
fim = time.time()
tempo_execucao = fim - inicio
print(f"bubble sort 1000: {tempo_execucao}")

# Tempo de Execução Select Sort
inicio = time.time()
resultado = select_sort(vetor)
fim = time.time()
tempo_execucao = fim - inicio
print(f"select sort 1000: {tempo_execucao}")

# Tempo de Execução Quick Sort
inicio = time.time()
resultado = quick_sort(vetor)
fim = time.time()
tempo_execucao = fim - inicio
print(f"quick sort 1000: {tempo_execucao}")

vetor = [random.randint(1, 10000) for _ in range(10000)]

# Tempo de Execução Bubble Sort
inicio = time.time()
resultado = bubble_sort(vetor)
fim = time.time()
tempo_execucao = fim - inicio
print(f"bubble sort 10000: {tempo_execucao}")

# Tempo de Execução Select Sort
inicio = time.time()
resultado = select_sort(vetor)
fim = time.time()
tempo_execucao = fim - inicio
print(f"select sort 10000: {tempo_execucao}")

# Tempo de Execução Quick Sort
inicio = time.time()
resultado = quick_sort(vetor)
fim = time.time()
tempo_execucao = fim - inicio
print(f"quick sort 10000: {tempo_execucao}")

vetor = [random.randint(1, 100000) for _ in range(100000)]

# Tempo de Execução Bubble Sort
inicio = time.time()
resultado = bubble_sort(vetor)
fim = time.time()
tempo_execucao = fim - inicio
print(f"bubble sort 100000: {tempo_execucao}")

# Tempo de Execução Select Sort
inicio = time.time()
resultado = select_sort(vetor)
fim = time.time()
tempo_execucao = fim - inicio
print(f"select sort 100000: {tempo_execucao}")

# Tempo de Execução Quick Sort
inicio = time.time()
resultado = quick_sort(vetor)
fim = time.time()
tempo_execucao = fim - inicio
print(f"quick sort 100000: {tempo_execucao}")