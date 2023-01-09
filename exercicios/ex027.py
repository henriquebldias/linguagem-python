'''from datetime import datetime
dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if dados['ctps'] != 0:
        dados['contratação'] = int(input('Ano de Contratação: '))
        dados['salario'] = float(input('Salário: R$ '))
        dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
print('-=' * 30)
for k, v in dados.items():
        print(f'  - {k} tem o valor {v}')'''

#Cadastro de jogador de futebol
dados = dict()
partidas = list()
dados['nome'] = str(input('Nome: '))
total = int(input(f'Quantas partidas {dados["nome"]} jogou? '))
for i in range(0, total):
    partidas.append(int(input(f'Quantos gols na partida {i+1}? ')))
dados['gols'] = partidas[:]
dados['total'] = sum(partidas)
print('-=' * 30)
for k, v in dados.items():
    print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {dados["nome"]} jogou {len(dados["gols"])} partidas.')
for i, v in enumerate(dados['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {dados["total"]} gols.')
