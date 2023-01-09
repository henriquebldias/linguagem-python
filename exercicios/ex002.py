#import math (importar biblioteca math inteira) ->usa .math antes da função
'''from math import sqrt, floor #importa só as funções especificadas sem usar .math
num = int(input('Digite um número: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {}'.format(num, floor(raiz)))

import random #random.random() número aleatório
n = random.randint(1,10) #randint pra número aleatório inteiro de 1 a 10
print(n)'''

'''from math import trunc
a = float(input('Digite um valor decimal: '))
print('A parte inteira do valor {} é {}'.format(a, trunc(a)))
print('A parte inteira do valor {} é {}'.format(a, int(a)))'''

'''from math import sin, cos, tan, radians
ang = float(input('Digite o ângulo: '))
seno = sin(radians(ang)) #função seno, cos ... Retorna em radianos
cosseno = cos(radians(ang))
tangente = tan(radians(ang))
print('O ângulo de {}° tem o sen: {:.2f} | cos: {:.2f} | tan: {:.2f}'.format(ang,seno,cosseno,tangente))'''

#Progressão Aritmética
'''print('='*29)
print('     10 TERMOS DE UMA PA')
print('='*29)
t = int(input('Primeiro termo: '))
r = int(input('Razão: '))
decimo = t + (10 - 1) * r
for a in range(t, decimo, r):
    print('{} '.format(a), end = '-> ')
print('FIM')'''

#Números Primos
n = int(input('Digite um número: '))
t = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[34m', end='')
        t += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes.'.format(n, t))
if t == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')
