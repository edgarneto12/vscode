def ordenar_em_ordem_decrescente(vetor):
    vetor.sort(reverse=True)

def contar_pares_impares(vetor):
    pares = 0
    impares = 0
    for numero in vetor:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

vetor = [64, 34, 25, 12, 22, 11, 90]

ordenar_em_ordem_decrescente(vetor)
print("Vetor ordenado em ordem decrescente:", vetor)

pares, impares = contar_pares_impares(vetor)
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")
