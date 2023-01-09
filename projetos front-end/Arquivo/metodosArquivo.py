#'r' Leitura 
#'w' Escrita. Substitui o conteúdo do arquivo existente
#'x' Escrita. Retorna um erro caso o arquivo já exista
#'a' Escrita. Insere os novos dados no final do arquivo
#'b' Modo binário
#'t' Modo texto (padrão)
#'+' Atualizar. Tanto leitura quanto escrita

'''file = open('teste.txt', 'a')
-------------------------------------
file.write('Isso é um teste! \n') # recebe uma string por vez
-------------------------------------
frases = list()
frases.append('Linha 1 \n')
frases.append('Linha 2 \n')
frases.append('Linha 3 \n')
file.writelines(frases) #recebe uma lista, tupla, dicionário
-------------------------------------
file = open('teste.txt', 'r')
print(file.readline(16)) # lê a quantidade N de caracteres da primeira linha passada como parâmetro
print(file.readlines()) # lê todas as linhas do arquivo
file.close()'''



def arquivoExiste(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação da agenda!')
    else:
        print(f'Agenda {nome_arquivo} criada com sucesso!')


def escreverArquivo(nome_arquivo, i):
    try:
        a = open(nome_arquivo, 'at')
    except:
        print('Houve um ERRO na abertura da agenda!')
    else:
        try:
            a.write(f'{i}\n')
        except:
            print('Houve um ERRO na hora de escrever os dados!')
        else:
            print('Atualizado!')
            a.close()


def lerArquivo(nome_arquivo):
    try:
        a = open(nome_arquivo, 'rt')
    except:
        print('ERRO ao abrir a agenda!')
    else:
        print(a.read())
        a.close()


