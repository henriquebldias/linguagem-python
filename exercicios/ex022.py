numero = [[], []]
for i in range(1, 8):
    valor = int(input(f'Digite o {i}ª valor: '))
    if valor % 2 == 0:
        numero[0].append(valor)
    else:
        numero[1].append(valor)
numero[0].sort()
numero[1].sort()
print('-=-' * 30)
print(f'Os valores pares digitados foram: {numero[0]}')
print(f'Os valores ímpares digitados foram: {numero[1]}')