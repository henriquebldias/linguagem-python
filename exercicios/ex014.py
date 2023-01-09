'''numero = (int(input('Digite um número: ')), int(input('Digite um número: ')),
          int(input('Digite um número: ')), int(input('Digite um número: ')),)

print('Você digitou os valores {}'.format(numero))
print('O valor 9 apareceu {} vezes'.format(numero.count(9)))
if 3 in numero:
    print('O valor 3 foi digitado na posição {}'.format(numero.index(3)+1))
else:
    print('O valor 3 não foi digitado em nenhuma posição')
cont = 0
for n in numero:
    if n % 2 == 0:
        print('({}),'.format(n), end = ' ')
        cont = 1
if cont == 1:
    print(' foram os valores pares digitados', end = '')
else:
    print('Nenhum valor par foi digitado.')'''

#Tupla ()
listagem = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor', 4.20, 'Compasso',
            9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
print('-' * 37)
print('         LISTAGEM DE PREÇOS')
print('-' * 37)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print('{:.<30}'.format(listagem[pos]), end = '')
    else:
        print('R$ {:>1.2f}'.format(listagem[pos]))