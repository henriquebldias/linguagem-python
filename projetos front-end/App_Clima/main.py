from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


# cores -------------------------------

co1 = "#f0f3f5" # Cinza
co2 = "#feffff" # Branca
co3 = "#38576b" # Azul
co4 = "#403d3d" # Letra
co5 = "#6f9fbd" # Azul diferenciado
co6 = "#ef5350" # Vermelha
co7 = "#93cd95" # Verde
co8 = "#00ffff" # Ciano
co9 = "#00ff00" # Verde chamativo
co10 = "#ff0000" # Vermelho chamativo

# fundos
fundo_dia = "#6cc4cc"
fundo_noite = "#484f60"
fundo_tarde = "#bfb86d"
fundo = fundo_dia


# janela -----------------------------

janela = Tk()
janela.title('')
janela.geometry('320x350')
janela.configure(bg=fundo)

ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=157)

# criar frames
frame_top = Frame(janela, width=320, height=50, bg= co2, pady=0, padx=0)
frame_top.grid(row=1, column=0) 

frame_corpo = Frame(janela, width=320, height=300, bg= fundo, pady=12, padx=0)
frame_corpo.grid(row=2, column=0, sticky=NW) 

# estilo
estilo = ttk.Style(janela)
estilo.theme_use('clam')

# configurar frame top

e_local = Entry(frame_top, width=20, justify='left', font=("", 14), highlightthickness=1, relief='solid')
e_local.place(x=15, y=10)

b_ver = Button(frame_top, text='Ver clima', bg=co2, fg=co3, font=('Ivy 9 bold'), relief='raised', overrelief=RIDGE)
b_ver.place(x=250, y=10)

# configura frame corpo

l_cidade = Label(frame_corpo, text='Goiânia - Brasil', anchor='center', bg=fundo, fg=co2, font=('Arial 14'))
l_cidade.place(x=10, y=4)

l_data = Label(frame_corpo, text='09 03 2022 | 10:50:00 AM', anchor='center', bg=fundo, fg=co2, font=('Arial 10'))
l_data.place(x=10, y=54)

l_umidade_num = Label(frame_corpo, text='84', anchor='center', bg=fundo, fg=co2, font=('Arial 45'))
l_umidade_num.place(x=10, y=100)

l_percentual = Label(frame_corpo, text='%', anchor='center', bg=fundo, fg=co2, font=('Arial 10'))
l_percentual.place(x=85, y=110)

l_umidade = Label(frame_corpo, text='Umidade', anchor='center', bg=fundo, fg=co2, font=('Arial 10'))
l_umidade.place(x=85, y=140)

l_pressao = Label(frame_corpo, text='Pressão: 1000', anchor='center', bg=fundo, fg=co2, font=('Arial 10'))
l_pressao.place(x=10, y=184)

l_velocidade = Label(frame_corpo, text='Velocidade do vento: 1000', anchor='center', bg=fundo, fg=co2, font=('Arial 10'))
l_velocidade.place(x=10, y=212)

imagem = Image.open('imagens/sol_dia.png')
imagem = imagem.resize((130, 130))
imagem = ImageTk.PhotoImage(imagem)

l_icon = Label(frame_corpo, image=imagem, bg=fundo)
l_icon.place(x=160, y=50)

l_descricao = Label(frame_corpo, text='Nublado', anchor='center', bg=fundo, fg=co2, font=('Arial 10'))
l_descricao.place(x=200, y=190)

janela.mainloop()