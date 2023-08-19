# Solicitando uma sequência de números
nums = input("Digite uma sequência de números inteiros separado apenas por espaços: ")
# transformando a sequêcia digitada em uma lista
lista = nums.split()
# ordenando a lista em ordem numérica
lista.sort(key=int)
# imprimindo o menor e o maior número da lista
print(f"O menor número é {min(lista)} e o maior é {max(lista)}")
