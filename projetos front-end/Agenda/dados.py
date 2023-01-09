import csv

def adicionar_dados(i):
    with open('data.csv', 'a+', newline='') as file:
        escrever = csv.writer(file)
        escrever.writerow(i)

def listar_dados():
    dados = []
    with open('data.csv', 'r') as file:
        ler_csv = csv.reader(file)     
        for linha in ler_csv:
            dados.append(linha)
    return dados

def remover_dados(i):

    def adicionar_nova_lista(j):
        with open('data.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)
        listar_dados()

    nova_lista = []
    cpf_2 = i
    with open('data.csv', 'r') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == cpf_2:
                    nova_lista.remove(linha)
    
    adicionar_nova_lista(nova_lista)

def atualizar_dados(i):
    def adicionar_nova_lista(j):
        with open('data.csv', 'w', newline='') as file:
            escrever = csv.writer(file)
            escrever.writerows(j)

    nova_lista = []
    cpf_busca = i[0]
    with open('data.csv', 'r') as file:
        ler_csv = csv.reader(file)
        for linha in ler_csv:
            nova_lista.append(linha)
            for campo in linha:
                if campo == cpf_busca:
                    nome = i[1]
                    cpf = i[2]
                    sexo = i[3]
                    tel = i[4]
                    email = i[5]
                    
                    dados = [nome, cpf, sexo, tel, email]

                    index = nova_lista.index(linha)
                    nova_lista[index] = dados
    
    adicionar_nova_lista(nova_lista)

def buscar_dados(i):
    dados = []
    cpf = i

    with open('data.csv', 'r') as file:
        ler_csv = csv.reader(file)     
        for linha in ler_csv:
            for campo in linha:
                if campo == cpf:
                    dados.append(linha)

    return dados


