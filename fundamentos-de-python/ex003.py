'''
Escreva um programa que peça o nome e a idade do usuário. Caso a idade do usuário seja maior ou igual a 18 anos apresente a seguinte mensagem: "Seja bem-vindo ao nosso site [nome]!"; caso contrário, apresente a seguinte mensagem: "Você não pode acessar nosso site [nome]'''
nome = input('Digite seu nome: ').strip().title()
idade = int(input('Digite sua idade: '))
resposta = "Seja bem-vindo ao nosso site {}!".format(nome)
if idade < 18:
    resposta = "Você não pode acessar nosso site {}.".format(nome)
print(resposta)
