'''try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#except Exception as erro:
except (ValueError, TypeError):
#print(f'Problema encontrado foi {erro.__class__}')
    print('ERRO! Houve um problema com os tipos de dados digitados.')
except ZeroDivisionError:
    print('ERRO! Não é possível dividir por ZERO.')
except KeyboardInterrupt:
    print('ERRO! O usuário não informou os dados.')
else:
    print(f'O resultado é {r:.1f}')
finally:
    print('Volte sempre! Muito obrigado!')'''

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        except(KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('ERRO: por favor, digite um número real válido.')
            continue
        except(KeyboardInterrupt):
            print('\nEntrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


n1 = leiaInt('Digite um valor inteiro: ')
n2 = leiaFloat('Digite um valor real: ')
print(f'O valor inteiro digitado foi {n1} e o real foi {n2}')