#fatorial biblioteca math tem factorial()
'''n = int(input('Digite um número para descobrir seu fatorial: '))
fat = 1
print('Calculando o fatorial de {}!'.format(n))
for a in range(n, 0, -1):
    fat *= a
    print('{}'.format(a), end='')
    print(' x ' if a > 1 else ' = ', end='')
print('{}'.format(fat))'''

#PA com repetição
'''print('Gerador de PA')
print('-='*10)
primeiro = float(input('Primeiro termo: '))
razao = float(input('Razão da PA: '))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print('{:.1f} -> '.format(termo), end = '')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos a mais você quer mostrar? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))'''

#Fibonacci
'''print('-'*200)
print('Sequência de Fibonacci')
print('-'*200)
n = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
print('-'*200)
print('{} -> {}'.format(t1, t2), end = '')
count = 2
while count < n:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end = '')
    t1 = t2
    t2 = t3
    count += 1
print(' -> FIM')
print('-'*200)'''

#Jogo par ou ímpar
from random import randint
print('=-='*20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-='*20)
V = 0
while True:
    jogador = int(input('Digite um valor: '))
    computador = randint(0, 5)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PIÍ':
        tipo = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    print('Você jogou {} e o computador {}. Total de {}'.format(jogador, computador, total))
    print('DEU PAR' if total % 2 == 0 else 'DEU ÍMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            V += 1
        else:
            print('Você PERDEU!')
            break
    elif tipo == 'I' or tipo == 'Í':
        if total % 2 == 1:
            print('Você VENCEU!')
            V += 1
        else:
            print('Você PERDEU!')
            break
    print('Vamos jogar novamente...')
print('GAME OVER! Você venceu {} vezes.'.format(V))