'''valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print('Na posição {} encontrei o valor {}!'.format(c, v))
print('Cheguei ao final da lista.')'''

'''a = [2, 3, 4, 7]
#b = a Ao igualar uma lista é feita uma ligação entre elas (NÃO É UMA CÓPIA)
b = a[:] #Faz uma cópia de a em b
b[2] = 8
print('Lista A: {}'.format(a))
print('Lista B: {}'.format(b))'''

lista = []
maior = 0
menor = 0
for c in range(0, 5):
    lista.append(int(input('Digite um valor para a Posição {}: '.format(c))))
    if c == 0:
        maior = menor = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
        if lista[c] < menor:
            menor = lista[c]
print('=-' * 30)
print('Você digitou os valores {}'.format(lista))
print('O maior valor digitado foi {} nas posições '.format(maior), end='')
for i, v in enumerate(lista):
    if lista[i] == maior:
        print('{}...'.format(i), end='')
print()
print('O menor valor digitado foi {} nas posições '.format(menor), end='')
for i, v in enumerate(lista):
    if v == menor:
        print('{}...'.format(i), end='')
print()

