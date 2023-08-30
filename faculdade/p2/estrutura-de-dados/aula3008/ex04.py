numeros, soma, somapar = [5, 10, 15, 20, 25], 0, 0
for numero in numeros:
    if numero %2 ==0:
        somapar += numero
    soma += numero
    
print(f"Soma dos numeros é: {soma} \nA soma dos numeros pares é: {somapar}")