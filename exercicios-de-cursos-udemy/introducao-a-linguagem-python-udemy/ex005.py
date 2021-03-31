'''
Escreva um programa que receba dois números e um sinal, e faça a operação matemática definida pelo sinal.   
'''
numero_1 = float(input('Digite o primeiro numero: '))
numero_2 = float(input('Digite o segundo numero: '))
sinal = input('Digite o sinal da operação: ').strip()
resultado = eval('numero_1 {} numero_2'.format(sinal))
print(resultado)
