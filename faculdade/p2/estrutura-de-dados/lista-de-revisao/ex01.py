import random
import time

vetor = [random.randint(1, 100000) for _ in range(10000)]

inicio = time.time()

vetor_ordenado = sorted(vetor)

fim = time.time()

tempo_gasto = fim - inicio

print(f"Tempo gasto para ordenar o vetor: {tempo_gasto:.6f} segundos")
