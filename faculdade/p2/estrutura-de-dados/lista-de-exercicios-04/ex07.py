def terceiro_maior(vetor):
    vetor_sem_duplicatas = list(set(vetor))
    
    if len(vetor_sem_duplicatas) < 3:
        return "Não há terceiro maior número no vetor."

    vetor_sem_duplicatas.sort(reverse=True)
    
    return vetor_sem_duplicatas[2]

vetor = [10, 5, 5, 8, 2, 2, 1, 1, 3, 3]

terceiro = terceiro_maior(vetor)
print(f"O terceiro maior número no vetor é: {terceiro}")
