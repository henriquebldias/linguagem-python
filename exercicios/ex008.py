'''for c in range(1, 6): #Imprime até o penúltimo
    print(c)

for a in range(6, 0, -1): #-1 faz contar de trás para frente
    print(a)

for b in range(0, 7, 2):#Imprime de 0 a 6 pulando de 2 em 2
    print(b)'''

#Contagem regressiva
'''from time import sleep
for d in range(10, -1, -1):
    print(d)
    sleep(1)
print('BUM! BUM! POOOW!')'''

#Condição de existência de triângulos
'''print('-='*19)
print('Condição de existência de triângulos')
print('-='*19)
a = float(input('Primeiro segmento (digite 0 para sair): '))
while(a != 0):
    b = float(input('Segundo segmento: '))
    c = float(input('Terceiro segmento: '))
    if c < a + b and b < a + c and a < b + c:
        print('Esses segmentos PODEM FORMAR um triângulo.')
    else:
        print('Esses segmentos NÃO PODEM FORMAR um triângulo.')
    print('-=' * 19)
    a = float(input('Primeiro segmento (digite 0 para sair): '))
print('Fim do programa.')'''

#Contagem de pares
'''for n in range(0, 51, 2):
    print(n, end = ' ')'''

#Soma de ímpares múltiplos de três
'''print('Múltiplos de 3 entre 1 e 500')
soma = 0
i = 0
for n in range(1, 501, 2):
    if n % 3 == 0:
        soma+= n
        i+= 1
print('A soma de todos os {} valores solicitados é {}.'.format(i, soma))'''

#Tabuada
'''n = int(input('Digite um número para ver sua tabuada: '))
for a in range(1, 11):
    print('{} x {} = {}'.format(n, a, (n * a)))'''

#Soma dos pares
'''soma = 0
for n in range(1, 7):
    a = int(input('Digite um valor: '))
    if a % 2 == 0:
        soma+= a
print('Soma dos valores pares: {}'.format(soma))'''

#Maior e menor da sequência
maior = float(input('Peso da 1ª pessoa: '))
menor = maior
for i in range(2, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(i)))
    if peso > maior:
        maior = peso
    elif peso < menor:
        menor = peso
print('O maior peso lido foi de {:.1f}Kg'.format(maior))
print('O menor peso lido foi de {:.1f}Kg'.format(menor))
