'''lanche = ('suco', 'pudim', 'hamburguer', 'maçã')#Tuplas são imutáveis / apenas atribui na declaração

for pos, comida in enumerate(lanche):
    print('Eu vou lanchar {} na posição {}'.format(comida, pos))

print(sorted(lanche))
print('-'*30)
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(c.index(5, 1))
print('-'*30)
pessoa = ('Gustavo', 39, 'M', 97.88)
print(pessoa)
del(pessoa)#deleta tupla'''

#Times com tuplas
'''times = ('Vila Nova', 'Palmeiras', 'Flamengo', 'Vasco da Gama', 'Fluminense', 'Santos', 'Chapecoense')
print('-'*100)
print('Lista de times: ')
for t in times:
    print(t)
print('-' * 100)
print('Os cinco primeiros times são: {}'.format(times[:5]))
print('-'*100)
print('Os quatro últimos times são: {}'.format(times[-4:]))
print('Times em ordem alfabética: {}'.format(sorted(times)))
print('O Chapecoense está na {}ª posição'.format(times.index('Chapecoense')+1))'''

'''from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ', end = ' ')
for n in numeros:
    print('{} '.format(n), end = ' ')
print('\nO maior valor sorteado foi {}'.format(max(numeros)))#max retorna o maior valor
print('O menor valor sorteado foi {}'.format(min(numeros)))#min retorna o menor valor'''
