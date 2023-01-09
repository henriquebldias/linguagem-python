matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end = '')
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
soma = 0
for l in range(0, 3):
    soma += matriz[l][2]
maior = 0
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    elif maior < matriz[1][c]:
        maior = matriz[1][c]
print('=-=' * 30)
print(f'A soma dos valores pares é {spar}')
print(f'A soma da terceira coluna é {soma}')
print(f'O maior valor da segunda coluna é {maior}')