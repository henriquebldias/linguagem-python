valor1 = float(input('Primeiro valor: '))
valor2 = float(input('Segundo valor: '))
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual é a sua opção? '))
    if opcao == 1:
        print('A soma {} + {} é igual a {}.'.format(valor1, valor2, (valor1 + valor2)))
        print('-=-'*20)
    elif opcao == 2:
        print('A multiplicação {} x {} é igual a {}.'.format(valor1, valor2, (valor1 * valor2)))
        print('-=-' * 20)
    elif opcao == 3:
        maior = valor2
        if valor1 > valor2:
            maior = valor1
        print('O maior valor é {}.'.format(maior))
        print('-=-' * 20)
    elif opcao == 4:
        valor1 = float(input('Primeiro valor: '))
        valor2 = float(input('Segundo valor: '))
    elif opcao != 5:
        print('Opção inválida.')
print('Saiu.')