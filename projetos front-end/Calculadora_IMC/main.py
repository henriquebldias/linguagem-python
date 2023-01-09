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
janela.title("Calculadora de IMC")
janela.geometry('295x230')
janela.configure(background=co2)
janela.resizable(width=FALSE, height=FALSE)

#--------------- FRAMES -------------#

frame_cima = Frame(janela, width=295, height=50, pady=0, padx=0, relief=FLAT, bg=co2)
frame_cima.grid(row=0, column=0, sticky=NSEW)

frame_baixo = Frame(janela, width=295, height=180, pady=0, padx=0, relief=FLAT, bg=co2)
frame_baixo.grid(row=1, column=0, sticky=NSEW)


#----------------Label---------------#
# frame cima
l_nome = Label(frame_cima, text="Calculadora de IMC", width=23, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 16 bold'), bg=co2, fg=co3)
l_nome.place(x=0, y=0)

l_linha = Label(frame_cima, text="", width=400, height=1, padx=0, relief='flat', anchor='center', font=('Ivy 1 bold'), bg=co3, fg=co1)
l_linha.place(x=0, y=47)

def calcular():

    peso = float(e_peso.get())
    altura = float(e_altura.get())
    imc = peso / altura**2
    resultado = imc

    if resultado < 18.5:
        l_texto['text'] = 'Seu IMC é: Abaixo do peso'
    elif resultado >= 18.5 and resultado < 25:
        l_texto['text'] = 'Seu IMC é: Normal'
    elif resultado >= 25 and resultado < 30:
        l_texto['text'] = 'Seu IMC é: Sobrepeso'
    else:
        l_texto['text'] = 'Seu IMC é: Obesidade'

    l_resultado['text'] = "{:.{}f}".format(resultado, 2)

#frame baixo
l_peso = Label(frame_baixo, text="Insira seu peso", height=1, padx=0, relief='flat', anchor=NW, font=('Ivy 10 bold'), bg=co2, fg=co3)
l_peso.grid(row=0, column=0, sticky=NSEW, pady=10, padx=3)

e_peso = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_peso.grid(row=0, column=1, sticky=NSEW, pady=10, padx=3)

l_altura = Label(frame_baixo, text="Insira sua altura", height=1, padx=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co2, fg=co3)
l_altura.grid(row=1, column=0, sticky=NSEW, pady=10, padx=3)

e_altura = Entry(frame_baixo, width=5, relief='solid', font=('Ivy 10 bold'), justify='center')
e_altura.grid(row=1, column=1, sticky=NSEW, pady=10, padx=3)

l_resultado = Label(frame_baixo, text="---", width=5, height=1, padx=6, pady=12, relief='flat', anchor='center', font=('Ivy 24 bold'), bg=co3, fg=co2)
l_resultado.place(x=175, y=10)

l_texto = Label(frame_baixo, text="", width=37, height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 10 bold'), bg=co2, fg=co3)
l_texto.place(x=0, y=95)

b_calcular = Button(frame_baixo, command=calcular, text="Calcular", width=34, height=1, overrelief='solid', relief='raised', anchor='center', font=('Ivy 10 bold'), bg=co3, fg=co2)
b_calcular.grid(row=4, column=0, sticky=NSEW, pady=60, padx=5, columnspan=30)




janela.mainloop()