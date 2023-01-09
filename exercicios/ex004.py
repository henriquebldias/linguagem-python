'''string
frase = 'Curso em Vídeo Python'
frase[:15] pega da pos 0 até 14
frase[8:] pega da pos 8 até o fim
frase[4:8:2] pega da pos 4 até a 12 pulando de dois em dois 4 x 5 x 6 x 7 x
frase[9::3] mesma de cima indo até o fim
len(frase) -> comprimento
frase.count('o') conta quantas vezes tem a letra o
frase.count('o',0,13) conta qtd de o's de 0 a 12
frase.find('deo') vai dizer quando encontrar 'deo' retornando a pos da primeira letra
frase.find('Android') se não existe ele retorna -1
'Curso' in frase -> in diz se existe a palavra em frase retornando true ou false
frase.replace('Python', 'Android') troca a palavra Python por Android
frase.upper() põe em maiúscula
frase.lower() minúscula
frase.capitalize() só o primeiro maiúsulo
frase.title() palavra por palavra com a primeira letra maiúscula
frase.strip() remove espaços inúteis rstrip() remove da direita e lstrip() os da esquerda
frase.split() divide criando novas listas (por padrão é o espaço)
'-'.join(frase) junta todos usando um traço
'''

#imprimir o texto inteiro print('''aaufhijfbefuehfiejqoihfheiofuehuehufheuhu''') mesmo com quebra de linha

#Gerenciador de Pagamentos
print('{:=^40}'.format(' Loja X '))
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTO
 [ 1 ] à vista dinheiro/cheque
 [ 2 ] à vista cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão ''')
opcao = int(input('Qual é a opção? '))
if opcao == 1:
    total = preco - preco * 0.1
elif opcao == 2:
    total = preco - preco * 0.05
elif opcao == 3:
    total = preco
    parcela = total/2
    print('Sua compra será parcelada em 2x de R${:.2f}'.format(parcela))
elif opcao == 4:
    total = preco + preco * 0.2
    np = int(input('A compra será parcelada em quantas vezes no cartão?'))
    parcela = total/np
    print('Sua compra será parcelada em {}x de R${:.2f}'.format(np, parcela))
else:
    total = 0
    print('Opção inválida. Tente novamente.')
print('O total a pagar é R${:.2f}.'.format(total))
