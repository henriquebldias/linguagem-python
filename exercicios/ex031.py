def teste(b):
    global a #Usa o a global. Não cria outra.
    a = 8
    b += 4
    c = 2
    print(f'A dentro vale {a}')
    print(f'B dentro vale {b}')
    print(f'C dentro vale {c}')

a = 5
teste(a)
print(f'A fora vale {a}')

def somar(a=0, b=0, c=0):
    s = a + b + c
    return s


resp = somar(10, 9, 8)
print(f'A soma é {resp}.')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

f1 = fatorial(6)
f2 = fatorial(5)
f3 = fatorial(7)
print(f'''Fatorial de 5 é {f2}
Fatorial de 6 é {f1}
Fatorial de 7 é {f3}''')