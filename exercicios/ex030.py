'''print('Controle de Terrenos')
print('-' * 30)
def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a} m^2.')


l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l, c)'''


'''from time import sleep
def contador(i, j, k):
    print(f'Contagem de {i} até {j} de {k} em {k}')
    sleep(1.5)
    if k < 0:
        k *= -1
    if k == 0:
       k = 1
    if i < j:
        cont = i
        while cont <= j:
            print(f'{cont} ', end='', flush=True)
            sleep(0.25)
            cont += k
        print('FIM!')
    else:
        cont = i
        while cont >= j:
            print(f'{cont} ', end='', flush=True)
            cont -= p
        print('FIM!')


contador(1, 10, 1)
contador(0, 100, 10)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
pas = int(input('Passo: '))
contador(ini, fim, pas)'''

'''from time import sleep
def maior(* num):
    print('-' * 40)
    cont = maior = 0
    print('Analisando os valores passados... ')
    for valor in num:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)'''

from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando valores de uma lista: ', end='')
    for cont in range(0, 5):
        lista.append(randint(1, 10))
        sleep(0.3)
    print(lista, end=' ')
    print('PRONTO!')

def somaPar(lista):
    soma = 0
    for cont in range(0, 5):
        if lista[cont] % 2 == 0:
            soma += lista[cont]
    print(f'Somando valores pares de {lista}, temos {soma}')


numeros = list()
sorteia(numeros)
somaPar(numeros)