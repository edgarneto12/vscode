def mediana(vetor):
    vetor_ordenado = sorted(vetor)
    tamanho = len(vetor_ordenado)

    if tamanho % 2 == 1:
        indice_mediana = tamanho // 2
        return vetor_ordenado[indice_mediana]
    else:
        indice1 = (tamanho - 1) // 2
        indice2 = tamanho // 2
        return (vetor_ordenado[indice1] + vetor_ordenado[indice2]) / 2

vetor = [10, 5, 8, 2, 1, 3, 7]

resultado = mediana(vetor)
print(f"A mediana do vetor é: {resultado}")
