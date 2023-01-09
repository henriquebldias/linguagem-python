#Programa usando in
'''nome = str(input('Qual é o seu nome completo?')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))'''

#Programa primeira e última ocorrência de string
'''frase = str(input('Digite uma frase: ')).strip().lower()
print('A letra A aparece {} vezez na frase'.format(frase.count('a')))
print('A primeira letra A apareceu na posição {}'.format(frase.find('a')+1))
print('A última letra A apareceu na posição {}'.format(frase.rfind('a')+1))'''

'''#Programa análise de str
nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}.'.format(nome[0], nome[len(nome)-1]))'''

#Porcentagem
'''salario = float(input('Qual é o salário do funcionário? '))
if salario <= 1250:
    novo = salario * 1.15
else:
    novo = salario * 1.1
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo))'''

#Programa Alistamento Militar
'''ano_nascimento = int(input('Digite o ano de seu nascimento: '))
from datetime import date
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade == 18
    print('Você deve se alistar esse ano ao completar 18.')
elif idade < 18:
    print('Faltam {} ano(s) para se alistar.'.format(18 - idade))
else:
    print('Já se passaram {} ano(s) da época de seu alistamento.'.format(idade - 18))'''

#jokenpo
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('{:=^21}'.format(' JOKENPO! '))
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
if(jogador == 0 or jogador == 1 or jogador== 2):
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    print('-=-' *8)
    print('Computador jogou {}'.format(itens[computador]))
    print('Você jogou {}'.format(itens[jogador]))
    print('-=-' *8)
    if computador == 0:
        if jogador == 0:
            print('EMPATE!')
        elif jogador == 1:
            print('VOCÊ VENCEU!')
        else:
            print('COMPUTADOR VENCEU!')
    elif computador == 1:
        if jogador == 0:
            print('COMPUTADOR VENCEU!')
        elif jogador == 1:
            print('EMPATE!')
        else:
            print('VOCÊ VENCEU!')
    elif computador == 2:
        if jogador == 0:
            print('VOCÊ VENCEU!')
        elif jogador == 1:
            print('COMPUTADOR VENCEU!')
        else:
            print('EMPATE!')
else:
    print('JOGADA INVÁLIDA.')



