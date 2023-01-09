'''palavra = ('Luffy','Zoro', 'Nami', 'Usopp', 'Sanji', 'Robin', 'Chopper', 'Franky', 'Brook', 'Jimbe')
for p in palavra:
    print('\nNa palavra {} temos '.format(p.upper()), end='')
    for letra in p:
        if letra.lower() in 'áãâaeéêíiôóõoúu':
            print(letra.lower(), end = ' ')'''

#LISTA []
lanche = ['arroz', 'feijão', 'carne', 'salada', 'suco']
print(lanche)
#adicionar elementos
lanche.append('macarrão') #add no final
print(lanche)
lanche.insert(0, 'batata') #add na posição movendo os elementos para frente
print(lanche)
del lanche[3] #remove da posição
print(lanche)
lanche.pop(2) #remove da posição
print(lanche)
lanche.remove('arroz')
print(lanche) #remove o elemento e reorganiza

numeros = [8, 7, 2, 4, 1, 10]
numeros.sort()
print(numeros)
numeros.sort(reverse=True)
print(numeros)
numeros[2] = 11
print(numeros)
numeros.append(3)
print(numeros)