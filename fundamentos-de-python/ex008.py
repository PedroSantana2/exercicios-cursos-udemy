'''
Escreva um script que mostre na tela o preço de um produto associado a uma categoria especificada pelo usuário. Utilize como referência as informações a seguir. Caso o usuário não digite uma categoria válida (número entre 1 e 10) mostre na tela uma mensagem personalizada.
'''
dicionario_preco = {1: 0.5, 2: 11.3, 3: 17.5, 4: 33.97, 5: 103.47, 6: 44.67, 7: 12.55, 8: 14.87, 9: 98.12, 10: 131.4}
categoria = int(input('Digite a categoria do produto: '))
try: 
    print('O preço do produto é: $ {}'.format(dicionario_preco[categoria]))
except:
    print('Opção ínvalida')
