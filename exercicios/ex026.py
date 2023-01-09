'''nome = input('Nome: ')
media = float(input(f'Média de {nome}: '))
if media < 6:
    situacao = 'Reprovado'
else:
    situacao = 'Aprovado'
print('-=' * 30)
aluno = {'nome': nome,
        'média': media,
         'situação': situacao
        }
print(f'- nome é igual a {aluno["nome"]}')
print(f'- média é igual a {aluno["média"]}')
print(f'- situação é igual a {aluno["situação"]}')'''

#Jogo de Dados em Python
from time import sleep
from random import randint
from operator import itemgetter
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)
        }
ranking = list()
print('Valores sorteados: ')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
print('-=' * 30)
print('  == RANKING DOS JOGADORES ==')
ranking = sorted(jogo.items(), key = itemgetter(1), reverse = True)
for i, v in enumerate(ranking):
    print(f'   {i+1}ª lugar: {v[0]} com {v[1]}.')
    sleep(1)