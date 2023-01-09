dados = dict()
pessoa = list()
totIdade = 0
while True:
    dados['nome'] = str(input('Nome: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while sexo not in 'MF':
        print('ERRO! Por favor, digite apenas M ou F.')
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dados['sexo'] = sexo
    dados['idade'] = int(input('Idade: '))
    totIdade += dados['idade']
    pessoa.append(dados.copy())
    dados.clear()
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        print('ERRO! Responda apenas S ou N.')
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break
media = totIdade/len(pessoa)
print('-:-' * 40)
print(f'Ao todo temos {len(pessoa)} pessoas cadastradas;')
print(f'A média de idade é de {media:.2f} anos;')
print(f'As mulheres cadastradas foram ', end=' ')
for p in pessoa:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}; ', end='')
print()
print('Lista de pessoas que estão acima da média:')
for p in pessoa:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
print()
print('-:-' * 18, 'ENCERRADO', '-:-' * 18)

