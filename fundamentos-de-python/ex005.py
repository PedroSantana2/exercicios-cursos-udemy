'''
O Índice de Massa Corporal (IMC) é utilizado para mensurar o peso ideal de uma pessoa. Escreva um programa que peça o nome, a idade , o peso e a altura do usuário. Ao final calcule e mostre o resultado do seu IMC e classifique este resultado de acordo com a regra a seguir.



IMC<17 - Muito abaixo do peso ideal

17<=IMC<18,5 - Abaixo do peso

18,5<=IMC<25 - Peso normal

25<=IMC<30 - Acima do peso

30<=IMC<35 - Obesidade I

35<=IMC<40 - Obesidade II (severa)

IMC>=40 - Obesidade III (mórbida)



Lembre que: IMC=massa/(altura*altura)
'''
nome = input('Digite seu nome: ').strip().title()
peso = int(input('Digite seu peso: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2
print('{}, veja seu resultado: '.format(nome))

if imc < 17:
    resposta = 'Muito abaixo do peso ideal'
elif (17 <= imc < 18.5):
    resposta = 'Abaixo do peso'
elif (18.5 <= imc < 25):
    resposta = 'Peso normal'
elif (25 <= imc < 30):
    resposta = 'Acima do peso'
elif (30 <= imc < 35):
    resposta = 'Obesidade I'
elif (35 <= imc < 40):
    resposta = 'Obesidade II'
else:
    resposta = 'Obesidade III'

print(resposta)
