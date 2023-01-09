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
lista.sort()
print('=' * 100)
print('Você adicionou os valores {}'.format(lista))

