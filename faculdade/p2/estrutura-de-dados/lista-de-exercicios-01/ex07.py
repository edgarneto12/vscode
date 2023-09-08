n = int(input("Digite um número: "))
a, b = 0, 1
print(f"A sequência de fibonacci até {n} é")
while a < n:
    print(a, end=', ')
    a, b = b, a+b