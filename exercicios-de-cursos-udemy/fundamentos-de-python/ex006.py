'''
Escreva um programa que receba dois números de ponto flutuante e mostre na tela o maior número digitado. Considere a possibilidade de o usuário digitar dois números iguais.
'''
lista = []
for i in range(2):
    numero = float(input('Digite um número: '))
    lista.append(numero)
print(max(lista))
