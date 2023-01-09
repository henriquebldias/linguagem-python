'''tot18 = 0
totH = 0
totM20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == 'M':
        totH += 1
    if sexo == 'F' and idade < 20:
        totM20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('Total de pessoas com mais de 18 anos: {}'.format(tot18))
print('Ao todo temos {} homens cadastrados'.format(totH))
print('E temos {} mulheres com menos de 20 anos'.format(totM20))'''

'''print('-'*40)
print('         LOJA SUPER BARATÃO')
print('-'*40)
qtd1000 = soma = menorPreco = cont = 0
while True:
    produto = input('Nome do Produto: ')
    preco = float(input('Preço: R$ '))
    cont += 1
    soma += preco
    if preco > 1000:
        qtd1000 += 1
    if cont == 1:
        menorPreco = preco
        nome = produto
    else:
        if preco < menorPreco:
            menorPreco = preco
            nome = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-'*20, end = '')
print('FIM DO PROGRAMA', end = '')
print('-'*20)
print('O total da compra foi R$ {}'.format(soma))
print('Temos {} produtos custando mais de R$ 1000.00'.format(qtd1000))
print('O produto mais barato foi {} que custa R$ {}'.format(nome, menorPreco))'''

print('=' * 30)
print('{:^30}'.format('BANCO CEV'))
print('=' * 30)
valor = float(input('Que valor você quer sacar? R$ '))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print('Total de {} cédulas de R$ {:.2f}'.format(totced, ced))
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
                break
print('=' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')