#Analisando e gerando Dicionários
def notas(*n, sit = False):
    '''
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit:valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    '''
    dados = dict()
    dados['total'] = len(n)
    soma = 0
    for i in range(0, len(n)): #soma -> sum(n); maior -> max(n); menor -> min(n)
        soma += n[i]
        if i == 0:
            maior = menor = n[i]
        elif maior < n[i]:
            maior = n[i]
        elif menor > n[i]:
            menor = n[i]
    dados['maior'] = maior
    dados['menor'] = menor
    dados['média'] = soma / dados['total']
    if sit:
        if dados['média'] >= 6:
            dados['situação'] = 'APROVADO'
        else:
            dados['situação'] = 'REPROVADO'
    return dados

print(':-:' * 25)
print(notas(7.0, 8.5, 10, 6.5, sit=True))

print(':-:' * 25)