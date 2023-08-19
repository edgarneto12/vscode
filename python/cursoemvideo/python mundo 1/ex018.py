from math import sin, cos, tan, radians
angulo = int(input('Digite o ângulo: '))
conversao = radians(angulo)
sen = sin(conversao)
cos = cos(conversao)
tan = tan(conversao)
print(f'Ângulo: {angulo}\nSeno:{sen:.2f} \nCoseno: {cos:.2f}\nTangente: {tan:.2f}')
