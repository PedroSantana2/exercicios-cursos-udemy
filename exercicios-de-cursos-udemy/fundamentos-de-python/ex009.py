'''
Escreva um script para classificar um triângulo de acordo com o tamanho dos seus lados. Considere as seguintes informações:

Triângulo equilátero: todos os lados possuem o mesmo tamanho;

Triângulo escaleno: todos os lados possuem medidas diferentes;

Triângulo isósceles: caracterizado por ter dois lados com o mesmo tamanho.
'''
lista = []
for i in range(3):
    lado = float(input('Digite o lado do triângulo: '))
    lista.append(lado)

resposta = 'Triângulo equilátero'
if lista[0] != lista[1] != lista[2]:
    resposta = 'Triângulo escaleno'
if (lista[0] == lista[1] != lista[2]) or (lista[1] == lista[2] != lista[0]) or (lista[0] == lista[2] != lista[1]):
    resposta = 'Triângulo isósceles'
print(resposta)
