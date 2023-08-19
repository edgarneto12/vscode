from math import hypot
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))
# hip = (co ** 2 + ca **2) ** (1/2)
hip = hypot(co, ca)
print(f'O comprimento da hipotenusa é igual a {hip:.2f}')
