from cgi import print_form
from tkinter import *
from tkinter import ttk
import random

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
co13 = "#00bfa5" # Verde bom

# janela -----------------------------

janela = Tk()
janela.title("")
janela.geometry('350x280')
janela.configure(background=co4)
janela.resizable(width=FALSE, height=FALSE)


##################################################
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=2, ipadx=280)

frame_top = Frame(janela, width=350, height=30, bg=co1, pady=0, padx=0, relief="flat")
frame_top.grid(row=1, column=0, sticky=NW)
frame_corpo = Frame(janela, width=350, height=280, bg=co4, pady=0, padx=0, relief="flat")
frame_corpo.grid(row=2, column=0, sticky=NW)

style = ttk.Style(janela)
style.theme_use("clam")

# configurando frame top
app_nome = Label(frame_top, text= "ADVINHE O NÚMERO", anchor='center', font=('verdana 14 bold'), bg=co1, fg=co13)
app_nome.place(x=55, y=0)

# função iniciar jogo
tentativas = 5
pontuacao = 0

def iniciar_jogo():
    l_regra_1['text'] = ''
    l_regra_2['text'] = ''
    l_regra_3['text'] = ''

    numeros = random.sample(range(1,10), 8)
    resposta = random.choice(numeros)

    def estado_valor(v):
        numeros = random.sample(range(1,10), 8)
        resposta = [random.choice(numeros)]

        global tentativas
        global pontuacao
        
        for i in resposta:
            if v == i:
                tentativas += 2
                pontuacao += 10
                l_tentativas['text'] = 'Tentativas: ' + str(tentativas)
                l_pontos['text'] = 'Pontuação: ' + str(pontuacao)
            else:
                tentativas -= 1
                l_tentativas['text'] = 'Tentativas: ' + str(tentativas)

                #desabilitando os botões
                if tentativas <= 0:
                    b1['state'] = 'disable'
                    b2['state'] = 'disable'
                    b3['state'] = 'disable'
                    b4['state'] = 'disable'
                    b5['state'] = 'disable'
                    b6['state'] = 'disable'
                    b7['state'] = 'disable'
                    b8['state'] = 'disable'

                    b1['text'] = ''
                    b2['text'] = ''
                    b3['text'] = ''
                    b4['text'] = ''
                    b5['text'] = ''
                    b6['text'] = ''
                    b7['text'] = ''
                    b8['text'] = ''

                    #chamar a função gameover
                    game_over()
                else:
                    pass
    
    
    b1 = Button(frame_corpo, command=lambda:estado_valor(numeros[0]), text= numeros[0], width=5, height=2, font=('Ivy 15 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
    b1.place(x=40, y=70)
    b2 = Button(frame_corpo, command=lambda:estado_valor(numeros[1]), text= numeros[1], width=5, height=2, font=('Ivy 15 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
    b2.place(x=108, y=70)
    b3 = Button(frame_corpo, command=lambda:estado_valor(numeros[2]), text= numeros[2], width=5, height=2, font=('Ivy 15 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
    b3.place(x=176, y=70)
    b4 = Button(frame_corpo, command=lambda:estado_valor(numeros[3]), text= numeros[3], width=5, height=2, font=('Ivy 15 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
    b4.place(x=244, y=70)
    b5 = Button(frame_corpo, command=lambda:estado_valor(numeros[4]), text= numeros[4], width=5, height=2, font=('Ivy 15 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
    b5.place(x=40, y=133)
    b6 = Button(frame_corpo, command=lambda:estado_valor(numeros[5]), text= numeros[5], width=5, height=2, font=('Ivy 15 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
    b6.place(x=108, y=133)
    b7 = Button(frame_corpo, command=lambda:estado_valor(numeros[6]), text= numeros[6], width=5, height=2, font=('Ivy 15 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
    b7.place(x=176, y=133)
    b8 = Button(frame_corpo, command=lambda:estado_valor(numeros[7]), text= numeros[7], width=5, height=2, font=('Ivy 15 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
    b8.place(x=244, y=133)


def game_over():
    global tentativas
    global pontuacao

    l_pontuacao = Label(frame_corpo, text= "Pontuação Final: " + str(pontuacao), anchor='center', relief='raised', font=('Ivy 15 bold'), bg=co4, fg=co9)
    l_pontuacao.place(x=80, y=90)

    l_jogo = Label(frame_corpo, text= "GAME OVER", anchor='center', relief='raised', font=('Ivy 15 bold'), bg=co4, fg=co10)
    l_jogo.place(x=110, y=120)  

    tentativas = 5
    pontuacao = 0

    l_tentativas['text'] = 'Tentativas: ' + str(tentativas)
    l_pontos['text'] = 'Pontuação: ' + str(pontuacao)

    b_jogar = Button(frame_corpo, command=iniciar_jogo, text= "Jogar", width=17, anchor='center', font=('Ivy 10 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
    b_jogar.place(x=100, y=150)


# configurando frame corpo
l_pontos = Label(frame_corpo, text= "Pontuação: 0", anchor='center', font=('Ivy 11 bold'), bg=co4, fg=co1)
l_pontos.place(x=40, y=30)


l_tentativas = Label(frame_corpo, text= "Tentativas: 5", anchor='center', font=('Ivy 11 bold'), bg=co4, fg=co1)
l_tentativas.place(x=205, y=30)


l_linha = Label(frame_corpo, width=90, anchor='center', font=('Ivy 4 bold'), bg=co9, fg=co1)
l_linha.place(x=39, y=59)

l_regra_1 = Label(frame_corpo, text= "Tente advinhar o número para pontuar", anchor='center', font=('Ivy 8 bold'), bg=co4, fg=co1)
l_regra_1.place(x=40, y=80)

l_regra_2 = Label(frame_corpo, text= "Se você acertar, ganhará mais duas chances", anchor='center', font=('Ivy 8 bold'), bg=co4, fg=co1)
l_regra_2.place(x=40, y=110)

l_regra_3 = Label(frame_corpo, text= "Se você errar, suas chances serão reduzidas", anchor='center', font=('Ivy 8 bold'), bg=co4, fg=co1)
l_regra_3.place(x=40, y=140)

b_jogar = Button(frame_corpo, command=iniciar_jogo, text= "Jogar", width=33, anchor='center', font=('Ivy 10 bold'), bg=co2, fg=co4, relief=RAISED, overrelief=RIDGE)
b_jogar.place(x=40, y=170)











janela.mainloop()