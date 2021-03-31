'''
Escreva um programa que resolva uma equação de segundo grau.   
'''
from math import sqrt


def delta(a, b, c):
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('O número não possui raízes reais')
        exit()
    return delta


def conferir_delta(delta):
    resposta = 1
    if delta > 0:
        resposta = 2
    return resposta


def x(delta, a, b, mais_menos):
    x = (-b + sqrt(delta)) / (2 * a)
    if mais_menos == '-':
        x = (-b - sqrt(delta)) / (2 * a)
    return x


a = float(input('Digite o valor de a: ')).strip()
b = float(input('Digite o valor de b: ')).strip()
c = float(input('Digite o valor de c: ')).strip()

delta = delta(a, b, c)
x2 = x(delta, a, b, '+')
x1 = x2
if conferir_delta(delta) == 2:
    x1 = x(delta, a, b, '-')

print('X1: {:.2f}, X2: {:.2f}'.format(x1, x2))
