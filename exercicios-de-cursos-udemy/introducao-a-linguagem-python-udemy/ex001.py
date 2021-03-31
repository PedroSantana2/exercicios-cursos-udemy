'''
Faça um programa que receba a idade do usuário e diga se ele é maior ou menor de idade.   
'''
idade = input('Digite sua idade: ')
resultado = 'menor'
if idade >= 18:
    resultado = 'maior'
print('Você é ' + resultado)
