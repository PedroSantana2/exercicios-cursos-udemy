'''
Faça um programa que solicite três números inteiros do usuário e imprima a soma destes.
'''
lista = []
for i in range(3):
    numero = int(input('Digite um número: '))
    lista.append(numero)
print(sum(lista))
