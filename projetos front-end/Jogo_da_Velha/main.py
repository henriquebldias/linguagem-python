from contextlib import ContextDecorator
from tkinter import *
from tkinter import ttk

# cores -------------------------------

co1 = "#f0f3f5" # Cinza
co2 = "#feffff" # Branca
co3 = "#38576b" # Azul
co4 = "#1e1f1e" # Preto
co5 = "#6f9fbd" # Azul diferenciado
co6 = "#ef5350" # Vermelha
co7 = "#93cd95" # Verde
co8 = "#00ffff" # Ciano
co9 = "#00ff00" # Verde chamativo
co10 = "#ff0000" # Vermelho chamativo
co11 = "#FFAB40" # Laranja
co12 = "#3b3b3b" # Preto mais claro

# janela -----------------------------

janela = Tk()
janela.title("Jogo da Velha")
janela.geometry('260x400')
janela.configure(background=co4)
janela.resizable(width=FALSE, height=FALSE)

#-------------FRAMES------------------
frame_cima = Frame(janela, width=240, height=100, relief='raised', bg=co12)
frame_cima.grid(row=0, column=0, sticky=NW, padx=10, pady=10)

frame_baixo = Frame(janela, width=240, height=300, relief='flat', bg=co4)
frame_baixo.grid(row=1, column=0, sticky=NW)


# frame cima
app_x = Label(frame_cima, text='X', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co12, fg=co10)
app_x.place(x=25, y=10)

app_x = Label(frame_cima, text='Jogador 1', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co12, fg=co2)
app_x.place(x=17, y=70)

app_x_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co12, fg=co2)
app_x_pontos.place(x=80, y=20)

app_separador = Label(frame_cima, text=':', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co12, fg=co2)
app_separador.place(x=110, y=20)

app_o = Label(frame_cima, text='O', height=1, relief='flat', anchor='center', font=('Ivy 40 bold'), bg=co12, fg=co8)
app_o.place(x=170, y=10)

app_o = Label(frame_cima, text='Jogador 2', height=1, relief='flat', anchor='center', font=('Ivy 7 bold'), bg=co12, fg=co2)
app_o.place(x=165, y=70)

app_o_pontos = Label(frame_cima, text='0', height=1, relief='flat', anchor='center', font=('Ivy 30 bold'), bg=co12, fg=co2)
app_o_pontos.place(x=130, y=20)


# Lógica do programa
jogador_1 = "X"
jogador_2 = "O"

score_1 = 0
score_2 = 0

tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

jogando = 'X'
jogar = ''
contador = 0
contador_de_rodadas = 0


def iniciar_jogo():
    # para controlar o jogo
    def controlar(i):
        global jogando
        global contador
        global jogar
       

        # comparando o valor recebido

        if i == str(1):
            # verificando se a posição está vazia ou não
            if b_0['text'] =='':
                # verifica quem está jogando e define a cor do símbolo
                if jogando == 'X':
                    cor = co10
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcando aquela posição na tabela
                # com o valor do jogador atual

                b_0['fg'] = cor
                b_0['text'] = jogando
                tabela[0][0] = jogando

                # verificando quem está jogano para poder trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para a próxima rodada
                contador += 1

        if i == str(2):

            # verificando se a posição está vazia ou não
            if b_1['text'] =='':
                # verifica quem está jogando e define a cor do símbolo
                if jogando == 'X':
                    cor = co10
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcando aquela posição na tabela
                # com o valor do jogador atual

                b_1['fg'] = cor
                b_1['text'] = jogando
                tabela[0][1] = jogando

                # verificando quem está jogano para poder trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para a próxima rodada
                contador += 1
                   
        if i == str(3):

            # verificando se a posição está vazia ou não
            if b_2['text'] =='':
                # verifica quem está jogando e define a cor do símbolo
                if jogando == 'X':
                    cor = co10
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcando aquela posição na tabela
                # com o valor do jogador atual

                b_2['fg'] = cor
                b_2['text'] = jogando
                tabela[0][2] = jogando

                # verificando quem está jogano para poder trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para a próxima rodada
                contador += 1
                    
        if i == str(4):

            # verificando se a posição está vazia ou não
            if b_3['text'] =='':
                # verifica quem está jogando e define a cor do símbolo
                if jogando == 'X':
                    cor = co10
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcando aquela posição na tabela
                # com o valor do jogador atual

                b_3['fg'] = cor
                b_3['text'] = jogando
                tabela[1][0] = jogando

                # verificando quem está jogano para poder trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para a próxima rodada
                contador += 1             
    
        if i == str(5):

            # verificando se a posição está vazia ou não
            if b_4['text'] =='':
                # verifica quem está jogando e define a cor do símbolo
                if jogando == 'X':
                    cor = co10
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcando aquela posição na tabela
                # com o valor do jogador atual

                b_4['fg'] = cor
                b_4['text'] = jogando
                tabela[1][1] = jogando

                # verificando quem está jogano para poder trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para a próxima rodada
                contador += 1
    
        if i == str(6):

            # verificando se a posição está vazia ou não
            if b_5['text'] =='':
                # verifica quem está jogando e define a cor do símbolo
                if jogando == 'X':
                    cor = co10
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcando aquela posição na tabela
                # com o valor do jogador atual

                b_5['fg'] = cor
                b_5['text'] = jogando
                tabela[1][2] = jogando

                # verificando quem está jogano para poder trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para a próxima rodada
                contador += 1   
        
        if i == str(7):

            # verificando se a posição está vazia ou não
            if b_6['text'] =='':
                # verifica quem está jogando e define a cor do símbolo
                if jogando == 'X':
                    cor = co10
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcando aquela posição na tabela
                # com o valor do jogador atual

                b_6['fg'] = cor
                b_6['text'] = jogando
                tabela[2][0] = jogando

                # verificando quem está jogano para poder trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para a próxima rodada
                contador += 1
                 
        if i == str(8):

            # verificando se a posição está vazia ou não
            if b_7['text'] =='':
                # verifica quem está jogando e define a cor do símbolo
                if jogando == 'X':
                    cor = co10
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcando aquela posição na tabela
                # com o valor do jogador atual

                b_7['fg'] = cor
                b_7['text'] = jogando
                tabela[2][1] = jogando

                # verificando quem está jogano para poder trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para a próxima rodada
                contador += 1
            
        if i == str(9):

            # verificando se a posição está vazia ou não
            if b_8['text'] =='':
                # verifica quem está jogando e define a cor do símbolo
                if jogando == 'X':
                    cor = co10
                if jogando == 'O':
                    cor = co8

                # definindo a cor do texto do botão
                # e marcando aquela posição na tabela
                # com o valor do jogador atual

                b_8['fg'] = cor
                b_8['text'] = jogando
                tabela[2][2] = jogando

                # verificando quem está jogano para poder trocar de jogador
                if jogando == 'X':
                    jogando = 'O'
                    jogar = 'Jogador 1'
                else:
                    jogando = 'X'
                    jogar = 'Jogador 2'
                
                # incrementar o contador para a próxima rodada
                contador += 1
     
    
        # após o contador ser maior ou igual a 5, verifica se houve algum vencedor de acordo com os padrões seguintes dentro da tabela

        if contador >= 5:
            # linhas
            if tabela[0][0] == tabela[0][1] == tabela[0][2]!="":
                vencedor(jogando)
            elif tabela[1][0] == tabela[1][1] == tabela[1][2]!="":
                vencedor(jogando)
            elif tabela[2][0] == tabela[2][1] == tabela[2][2]!="":
                vencedor(jogando)

            # colunas
            if tabela[0][0] == tabela[1][0] == tabela[2][0]!="":
                vencedor(jogando)
            elif tabela[0][1] == tabela[1][1] == tabela[2][1]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][2] == tabela[2][2]!="":
                vencedor(jogando)

            # diagonais
            if tabela[0][0] == tabela[1][1] == tabela[2][2]!="":
                vencedor(jogando)
            elif tabela[0][2] == tabela[1][1] == tabela[2][0]!="":
                vencedor(jogando)
                        
            # empate
            if contador >= 9:
                vencedor('Foi empate')   
   
    # para decidir o vencedor
    def vencedor(i):
        global tabela
        global score_1
        global score_2
        global contador_de_rodadas

        # bloqueando os botoes
        b_0['state'] = 'disable'
        b_2['state'] = 'disable'
        b_1['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        app_vencedor = Label(frame_baixo, text='', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co12, fg=co11)
        app_vencedor.place(x=40, y=250) 

        if i == 'X':
            score_2 += 1
            app_vencedor['text'] = 'Jogador 2 venceu!'
            app_o_pontos['text'] = score_2

        if i == 'O':
            score_1 += 1
            app_vencedor['text'] = 'Jogador 1 venceu!'
            app_x_pontos['text'] = score_1

        if i == 'Foi empate':
            app_vencedor['text'] = 'Foi empate!'

        def start():
            # limpando os botões
            b_0['text'] = ''
            b_1['text'] = ''
            b_2['text'] = ''
            b_3['text'] = ''
            b_4['text'] = ''
            b_5['text'] = ''
            b_6['text'] = ''
            b_7['text'] = ''
            b_8['text'] = ''

            b_0['state'] = 'normal'
            b_2['state'] = 'normal'
            b_1['state'] = 'normal'
            b_3['state'] = 'normal'
            b_4['state'] = 'normal'
            b_5['state'] = 'normal'
            b_6['state'] = 'normal'
            b_7['state'] = 'normal'
            b_8['state'] = 'normal'

            # reinicia a tabela
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]

            app_vencedor.destroy()
            b_jogar.destroy()

        
        #Botão jogar
        b_jogar = Button(frame_baixo, command=start, text='Próxima rodada', height=1, font=('Ivy 10 bold'), overrelief=RIDGE, bg=co4, relief=RAISED, fg=co2)
        b_jogar.place(x=80, y=197)
        
        def game_over():
            b_jogar.destroy()
            app_vencedor.destroy()

            terminar()
        
        if contador_de_rodadas >= 2:
            game_over()
        else:
            contador_de_rodadas += 1
            tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
            contador = 0

    # para terminar o jogo
    def terminar():
        global tabela
        global contador_de_rodadas
        global score_1
        global score_2
        global contador

        tabela = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
        score_1 = 0
        score_2 = 0
        contador_de_rodadas = 0
        contador = 0

        b_0['state'] = 'disable'
        b_2['state'] = 'disable'
        b_1['state'] = 'disable'
        b_3['state'] = 'disable'
        b_4['state'] = 'disable'
        b_5['state'] = 'disable'
        b_6['state'] = 'disable'
        b_7['state'] = 'disable'
        b_8['state'] = 'disable'

        app_fim = Label(frame_baixo, text='Jogo Acabou', width=17, relief='flat', anchor='center', font=('Ivy 13 bold'), bg=co12, fg=co11)
        app_fim.place(x=25, y=90) 

        # jogar de novo
        def jogar_de_novo():
            app_x_pontos['text'] = '0'
            app_o_pontos['text'] = '0'
            app_fim.destroy()
            b_jogar.destroy()

            # chamando a função iniciar jogo
            iniciar_jogo

        # botao jogar de novo
        b_jogar = Button(frame_baixo, command=jogar_de_novo, text='Jogar', height=1, font=('Ivy 10 bold'), overrelief=RIDGE, bg=co4, relief=RAISED, fg=co2)
        b_jogar.place(x=80, y=197)

    # frame baixo
            
    #linhas verticais

    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co2)
    app_.place(x=90, y=15)

    app_ = Label(frame_baixo, text='', height=23, relief='flat', pady=5, anchor='center', font=('Ivy 5 bold'), bg=co2)
    app_.place(x=157, y=15)

    #linhas horizontais

    app_ = Label(frame_baixo, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co2)
    app_.place(x=30, y=63)

    app_ = Label(frame_baixo, text='', width=46, relief='flat', padx=2, pady=1, anchor='center', font=('Ivy 5 bold'), bg=co2)
    app_.place(x=30, y=127)

    #linha 0

    b_0 = Button(frame_baixo, command=lambda:controlar('1'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, bg=co4, relief=FLAT)
    b_0.place(x=30, y=15)

    b_1 = Button(frame_baixo, command=lambda:controlar('2'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, bg=co4, relief=FLAT)
    b_1.place(x=96, y=15)

    b_2 = Button(frame_baixo, command=lambda:controlar('3'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, bg=co4, relief=FLAT)
    b_2.place(x=163, y=15)

    #linha 1

    b_3 = Button(frame_baixo, command=lambda:controlar('4'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, bg=co4, relief=FLAT)
    b_3.place(x=30, y=75)

    b_4 = Button(frame_baixo, command=lambda:controlar('5'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, bg=co4, relief=FLAT)
    b_4.place(x=96, y=75)

    b_5 = Button(frame_baixo, command=lambda:controlar('6'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, bg=co4, relief=FLAT)
    b_5.place(x=163, y=75)


    #linha 2

    b_6 = Button(frame_baixo, command=lambda:controlar('7'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, bg=co4, relief=FLAT)
    b_6.place(x=30, y=135)

    b_7 = Button(frame_baixo, command=lambda:controlar('8'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, bg=co4, relief=FLAT)
    b_7.place(x=96, y=135)

    b_8 = Button(frame_baixo, command=lambda:controlar('9'), text='', width=3, height=1, font=('Ivy 20 bold'), overrelief=RIDGE, bg=co4, relief=FLAT)
    b_8.place(x=163, y=135)

#Botão jogar
b_jogar = Button(frame_baixo, command=iniciar_jogo, text='Jogar', width=10, height=1, font=('Ivy 10 bold'), overrelief=RIDGE, bg=co4, relief=RAISED, fg=co2)
b_jogar.place(x=85, y=197)

janela.mainloop()
#2:34:00