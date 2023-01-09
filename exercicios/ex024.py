ficha = list()
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('=' * 26)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)
for i, j in enumerate(ficha):
    print(f'{i:<4}{j[0]:<10}{j[2]:>8.1f}')
print('-' * 26)
escolha = 0
while True:
    escolha = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if escolha < len(ficha):
        print(f'Notas de {ficha[escolha][0]} são {ficha[escolha][1]}')
        print('=' * 37)
    elif escolha == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    else:
        print('Aluno não cadastrado.')
