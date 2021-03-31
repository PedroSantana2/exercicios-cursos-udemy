'''
Considere a tupla1 e responda as seguintes questões:



tupla1=('A','B','A','Z','Z','X','A','E','K','G','H')



a) mostre na tela o tamanho desta tupla;

b) ordene a tupla e mostre o resultado na tela;

c) mostre na tela o número de ocorrências da string 'A';

d) mostre na tela o número de ocorrências da string 'B';

e) mostre na tela o índice da string 'X';

f) mostre na tela o último elemento da tupla1.
'''
tupla1 = ('A','B','A','Z','Z','X','A','E','K','G','H')
print(len(tupla1))
print(sorted(tupla1))
print(tupla1.count('A'))
print(tupla1.index('X'))
print(tupla1[-1])
