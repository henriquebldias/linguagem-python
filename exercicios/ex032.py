'''def voto(anoNasc):
    from datetime import datetime
    i = datetime.now().year - anoNasc
    if i < 16:
        return f'Com {i} anos: NÃO VOTA.'
    elif  16<= i <18 or i > 70:
        return f'Com {i} anos: VOTO OPCIONAL.'
    else:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'


ano = int(input('Em que ano você nasceu? '))
print(voto(ano))'''

#Função para fatorial
'''def fatorial(n, show = False):
    f = 1
    print('-' * n*4)
    for i in range(n, 0, -1):
        if show:
            print(i, end='')
            if i > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= i
    return f



num = int(input('Digite um valor para calcular seu fatorial: '))
print(fatorial(num, show=True))'''

#Ficha de jogador
'''def ficha(nome='<desconhecido>', gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


print('-' * 40)
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n.strip() == '':
    ficha(gols = g)
else:
    ficha(n, g)'''

#Validando entrada de dados em Python
def leiaInt(msg):
    num = str(input(msg))
    while num.isnumeric() == False:
        print('\033[0;31;0mERRO! Digite um número inteiro válido.\033[m')
        num = str(input(msg))
    return num


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
