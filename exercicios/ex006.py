'''from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' *21)
print('Vou pensar em um número entre 0 e 5. Advinhe qual é o número...')
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('Você acertou! Parabéns!')
else:
    print('Você errou! Eu pensei no número {}.'.format(computador))

print('-=-' * 21)'''

#Radar eletrônico
'''velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    print('Multado! Você excedeu o limite permitido de velocidade igual a 80 km/h')
    multa = (velocidade - 80) * 7
    print('O valor da multa a ser pago é R$ {:.2f}!'.format(multa))'''

#Conversor de bases
n = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
o = int(input('Sua opção: '))
if o == 1:
    print('{} convertido para BINÁRIO é {}.'.format(n, bin(n)[2:]))
elif o == 2:
    print('{} convertido para OCTAL é {}.'.format(n, oct(n)[2:]))
elif o == 3:
    print('{} convertido para HEXADECIMAL é {}.'.format(n, hex(n)[2:]))
else:
    print('Opção inválida.')



