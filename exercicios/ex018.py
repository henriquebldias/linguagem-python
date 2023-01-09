'''lista = []
for i in range(0, 5):
    valor = int(input('Digite um valor: '))
    if i == 0 or valor > lista[-1]:
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(lista):
            if valor <= lista[pos]:
                lista.insert(pos, valor)
                print('Adicionado na posição {} da lista'.format(pos))
                break
            pos += 1
print('-=' * 30)
print('Os valores digitados em ordem foram {}'.format(lista))'''

lista = []
escolha = ''
while escolha != 'N':
    valor = int(input('Digite um valor: '))
    if valor not in lista:
        lista.append(valor)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    while True:
        escolha = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if escolha not in 'NS':
            print('Opção inválida.')
        else:
            break
print('A lista completa é {}'.format(lista))
listaPares = []
listaImpares = []
for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        listaPares.append(lista[i])
    else:
        listaImpares.append(lista[i])
print('A lista de pares é {}'.format(listaPares))
print('A lista de ímpares é {}'.format(listaImpares))


