temp = list()
princ = list()

while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print('Os dados foram {}'.format(princ))
print('Ao todo, você cadastrou {} pessoas.'.format(len(princ)))
print('O maior peso foi de {} Kg'.format(mai))
print('| ', end = '')
for p in princ:
    if p[1] == mai:
        print('{}'.format(p[0]), end=' | ')
print()
print('O menor peso foi de {} Kg'.format(men))
print('| ', end = '')
for p in princ:
    if p[1] == men:
        print('{}'.format(p[0]), end=' | ')