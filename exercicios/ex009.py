#Analisador completo
'''cont = 0
soma = 0
maisVelho = 0
qtd_M_menor20 = 0
for i in range(1, 5):
    print('----- {}ª PESSOA -----'.format(i))
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ')
    cont += 1
    soma += idade
    if sexo == 'M':
        if idade > maisVelho:
            maisVelho = idade
            nomeMaisVelho = nome
    if sexo == 'F':
        if idade < 20:
            qtd_M_menor20 += 1

print('A média de idade do grupo é de {:.1f} anos.'.format(soma/cont))
print('O homem mais velho tem {} anos e se chama {}.'.format(maisVelho, nomeMaisVelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(qtd_M_menor20))'''''

#while
'''sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dados inválidos! Informe seu sexo [M/F]: ')).strip().upper()[0]
if sexo == 'M':
    print('Sexo masculino registrado com sucesso.')
else:
    print('Sexo feminino registrado com sucesso.')'''

#Adivinhação
from random import randint
computador = randint(0, 10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
jogador = int(input('Qual é seu palpite? '))
tentativas = 1
while jogador != computador:
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')
    jogador = int(input('Qual é seu palpite? '))
    tentativas += 1
print('Acertou com {} tentativas. Parabéns!'.format(tentativas))
