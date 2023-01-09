import imp
from platform import release
from tkinter import *
import tkinter
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
janela.title("")
janela.geometry('300x180')
janela.configure(background=co4)
janela.resizable(width=FALSE, height=FALSE)

# variáveis globais 
global tempo
global rodar
global contador
global limitador
limitador = 59

#--------------Funções--------------#

tempo = "00:00:00"
rodar = False
contador = -5

def iniciar():

    global tempo
    global contador
    global limitador

    if rodar:
        # antes do cronômetro começar
        if contador <= -1:
            inicio = 'Começando em ' +str(contador)
            label_tempo['text'] = inicio
            label_tempo['font'] = 'Arial 10'
        # rodando o cronômetro
        else:
            label_tempo['font'] = 'Times 10 bold'

            temporaria = str(tempo)
            h, m, s = map(int, temporaria.split(':'))
            h = int(h)
            m = int(m)
            s = int(contador)

            if s >= limitador:
                contador = 0
                m += 1

            s = str(0) +str(s)
            m = str(0) +str(m)
            h = str(0) +str(h)

            # atualizando os valores atuais
            temporaria = str(h[-2:]) + ":" + str(m[-2:]) + ":" + str(s[2:])
            label_tempo['text'] = temporaria
            tempo = temporaria

        label_tempo.after(1000, iniciar)
        contador += 1

#inicia a função iniciar
def start():
    global rodar
    rodar = True
    iniciar()

#---------------Label-------------#
label_app = Label(janela, text='Cronômetro', font=('Arial 10'), bg=co4, fg=co2)
label_app.place(x=20, y=5)

label_tempo = Label(janela, text=tempo, font=('Times 50 bold'), bg=co4, fg=co8)
label_tempo.place(x=20, y=25)

#----------------Botões------------#
b_iniciar = Button(janela, command=start, text='Iniciar', width=10, height=2, bg=co4, fg=co2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
b_iniciar.place(x=20, y=130)

b_pausar = Button(janela, text='Pausar', width=10, height=2, bg=co4, fg=co2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
b_pausar.place(x=105, y=130)

b_reiniciar = Button(janela, text='Reiniciar', width=10, height=2, bg=co4, fg=co2, font=('Ivy 8 bold'), relief='raised', overrelief='ridge')
b_reiniciar.place(x=190, y=130)


janela.mainloop()