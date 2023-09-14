lista, soma, contador = [12, 8, 17, 14, 5, 10, 23, 6, 9, 16, 31, 18, 27, 7, 22, 4, 11, 20, 29, 2, 35, 42, 53, 38, 45, 26, 33, 19, 15, 37, 21, 3, 25, 30, 36, 47, 34, 28, 39, 50], 0, 0
for i in lista:
    if i%2 == 0:
        soma += i;
        contador += 1;
print(f"A média dos números pares presentes na lista é: {soma/contador:.2f}")
print(f"Debug Contador: {contador} soma: {soma}")
