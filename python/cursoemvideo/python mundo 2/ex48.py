s = 0
for c in range(0,500,3):
    if c % 2 != 0:
        s += c
print(f'A soma de todos números ímpares que são múltiplos de três é {s}')