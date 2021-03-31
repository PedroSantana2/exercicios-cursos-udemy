'''
Escreva um programa que solicite o nome e o sobrenome do usuário. Ao final o programa deverá apresentar o nome completo do usuário na tela.
'''
nome = input('Digite seu nome: ').strip().lower()
sobrenome = input('Digite seu sobrenome: ').strip().lower()
print('Seu nome é: {}'.format((nome + ' ' + sobrenome).title())) 
