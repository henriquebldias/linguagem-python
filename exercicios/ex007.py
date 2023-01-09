#Código ANSI para cores
#print('\033[1;31;43mOlá, Mundo!\033[m')
'''nome = 'Henrique'
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format('\033[4;34m', nome, '\033[m'))

cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!'.format(cores['amarelo'], nome, cores['limpa']))'''

#elif
'''nome = str(input('Qual é o seu nome? '))
if nome == 'Henrique':
    print('Tá!')
elif nome == 'Ana' or nome == 'Mateus' or nome == 'Gustavo':
    print('Ok!')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Show')
else:
    print('É!')
print('Tenha um bom dia, {}'.format(nome))'''

#Aprovando empréstimo

'''casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))
prestacao = casa / (anos * 12)
minimo = salario * 0.3
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end = '')
print(' a prestação será de R${:.2f}'.format(prestacao))
if prestacao <= minimo:
    print('Empréstimo pode ser CONCEDIDO')
else:
    print('Empréstimo NEGADO')'''

#IMC
'''peso = float(input('Qual é o seu peso? (Kg)'))
altura = float(input('Qual é a sua altura? (m)'))
imc = peso/(altura**2)
print('O IMC dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do peso normal.')
elif imc >= 18.5 and imc <25:
    print('Seu peso é IDEAL.')
elif imc >= 25 and imc < 30:
    print('Você está com SOBREPESO.')
elif imc >=30 and imc <40:
    print('Você está em estado de OBESIDADE.')
else:
    print('Você está em estado de OBESIDADE MÓRBIDA, cuidado!')'''

#Palíndromo
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}.'.format(junto, inverso))
if inverso == junto:
    print('Temos um palíndromo!')
else:
    print('A frase não é um palíndromo.')
