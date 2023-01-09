#choice e shuffle
'''from random import choice, shuffle
a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
sorteado = choice(lista)
print('O aluno sorteado foi {}'.format(sorteado))
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)'''

#Par ou ímpar
'''n = int(input('Digite um número inteiro qualquer: '))
if n%2 == 0:
    print('O número {} é PAR!'.format(n))
else:
    print('O número {} é ÍMPAR!'.format(n))'''

#custo da viagem
'''distancia = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {} Km.'.format(distancia))
if distancia <= 200:
    preco = distancia * 0.5
else:
    preco = distancia * 0.45
print('O preço da sua passagem será de R${:.2f}'.format(preco))'''

#Ano bissexto
'''from datetime import date
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO.'.format(ano))'''

#Maior e menor
'''a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))
c = int(input('Terceiro número: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print('O menor número é {}.'.format(menor))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior número é {}.'.format(maior))'''

#Grupo da Maioridade
from datetime import date
ano_atual = date.today().year
somaMenor = 0
somaMaior = 0
for a in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(a)))
    idade = ano_atual - ano
    if idade >= 18:
        somaMaior+=1
    else:
        somaMenor+=1
print('Ao todo tivemos {} pessoas MAIORES de idade e {} pessoas MENORES de idade.'.format(somaMaior, somaMenor))

