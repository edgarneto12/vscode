s1 = float(input(f'Digite o primeiro seguimento: '))
s2 = float(input(f'Digite o segundo seguimento: '))
s3 = float(input(f'Digite o terceiro seguimento: '))
if (s1+s2) > s3 and (s1+s3) > s2 and (s2+s3) > s1:
    print('Podem formar um triângulo.')
    if s1 == s2 == s3:
        print('Triângulo Equilátero, ou seja, todos lados são iguais.')
    if s1 == s2 and s2 == s3 and s1 == s3:
        print('Triângulo Isóceles, ou seja, apenas dois lados são iguais.')
    else:
        print('Triângulo Escaleno, ou seja, todos lados são diferentes.')
else:
    print('Não podem formar um triângulo.')