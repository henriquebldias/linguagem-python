#Método is
A = input('Digite algo: ')
print('O tipo primitivo desse valor é',type(A))
print('Só tem espaços?', A.isspace())
print('É um número?', A.isnumeric())
print('É alfabético?', A.isalpha())
print('É alfanumérico?', A.isalnum())
print('Está só em maiúsculas?', A.isupper())
print('Está só em minúsculas?', A.islower())
print('Está capitalizada?', A.istitle())

#operadores aritméticos (+, -, *, /, **, // divisão inteira, %)
#Para fazer contas é preciso colocar o tipo da variável antes
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
soma = n1 + n2
sub = n1 - n2
mult = n1 * n2
div = n1 / n2
pot = n1 ** n2
div_int = n1 // n2
rest = n1 % n2
print('Resultados')
print('Soma: {}'.format(soma))
print('Subtração: {}'.format(sub))
print('Multiplicação: {}'.format(mult))
print('Divisão: {:.2f}'.format(div))
print('Potência: {}'.format(pot))
print('Parte inteira da divisão: {}'.format(div_int))
print('Resto da divisão: {}'.format(rest))
#Quebrar linha \n e manter end='' obs:end=' >>> '
#Calcular raiz quadrada é só elevar ao 1/2

n = int(input('Digite um número: '))
print('O antecessor de {} é {} e o sucessor é {}'.format(n, (n-1), (n+1)))