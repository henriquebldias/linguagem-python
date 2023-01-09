from cgitb import text
from tkinter.ttk import *
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from dados import *


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

# janela -----------------------------

janela = Tk()
janela.title("")
janela.geometry('600x500')
janela.configure(background=co2)
janela.resizable(width=FALSE, height=FALSE)

# estilo -----------------------------

style = Style(janela)
style.theme_use("clam")

#--------------- FRAMES -------------#

frame_cima = Frame(janela, width=600, height=50, bg=co3, relief="flat")
frame_cima.grid(row=0, column=0, pady=1, padx=0, sticky=NSEW)

frame_baixo = Frame(janela, width=600, height=180, bg=co1, relief="flat")
frame_baixo.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frame_tabela = Frame(janela, width=600, height=248, bg=co2, relief="flat")
frame_tabela.grid(row=2, column=0,columnspan=2, pady=1, padx=10, sticky=NSEW)


# configura frame_cima

l_nome = Label(frame_cima, text='AGENDA', anchor=NE, font=('arial 20 bold'), bg=co3, fg=co2)
l_nome.place(x=5, y=5)

l_linha = Label(frame_cima, text='', width=1000, anchor=NE, font=('arial 1'), bg=co2, fg=co1)
l_linha.place(x=0, y=47)


global tree
# configura frame tabela

def mostrar_dados():
    global tree
    # create a treeview with dual scrollbars
    dados_h = ['Nome', 'cpf', 'Sexo', 'Telefone', 'email']

    dados = listar_dados()

    tree = ttk.Treeview(frame_tabela, selectmode="extended", columns=dados_h, show="headings")

    # vertical scrollbar
    vsb = ttk.Scrollbar(frame_tabela, orient="vertical", command=tree.yview)
    # horizontal scrollbar
    hsb = ttk.Scrollbar(frame_tabela, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    # tree cabeçalho
    tree.heading(0, text='Nome', anchor=NW)
    tree.heading(1, text='CPF', anchor=NW)
    tree.heading(2, text='Sexo', anchor=NW)
    tree.heading(3, text='Telefone', anchor=NW)
    tree.heading(4, text='Email', anchor=NW)

    # tree corpo
    tree.column(0, width=170, anchor='nw')
    tree.column(1, width=100, anchor='nw')
    tree.column(2, width=50, anchor='nw')
    tree.column(3, width=120, anchor='nw')
    tree.column(4, width=130, anchor='nw')

    for item in dados:
        tree.insert('', 'end', values=item)

def inserir():
    nome = e_nome.get()
    cpf = e_cpf.get()
    sexo = c_sexo.get()
    telefone = e_telefone.get()
    email = e_email.get()

    dados = [nome, cpf, sexo, telefone, email]

    if nome == '' or cpf == '' or sexo == '' or telefone == '' or email == '':
        messagebox.showwarning('Dados', 'Por favor, preencha todos os campos.')
    else:
        adicionar_dados(dados)
        messagebox.showinfo('Dados', 'Dados adicionados com sucesso!')

        e_nome.delete(0, 'end')
        e_cpf.delete(0, 'end')
        c_sexo.delete(0, 'end')
        e_telefone.delete(0, 'end')
        e_email.delete(0, 'end')

        mostrar_dados()


def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        nome = tree_lista[0]
        cpf = tree_lista[1]
        sexo = tree_lista[2]
        telefone = str(tree_lista[3])
        email = tree_lista[4]

        e_nome.insert(0,nome)
        e_cpf.insert(0,cpf)
        c_sexo.insert(0,sexo)
        e_telefone.insert(0,telefone)
        e_email.insert(0,email)

        def confirmar():
            nome = e_nome.get()
            cpf = e_cpf.get()
            sexo = c_sexo.get()
            telefone_novo = e_telefone.get()
            email = e_email.get()

            dados = [telefone, nome, cpf, sexo, telefone_novo, email]

            atualizar_dados(dados)

            messagebox.showinfo('Dados', 'Os dados formam atualizados com sucesso!')

            e_nome.delete(0, 'end')
            e_cpf.delete(0, 'end')
            c_sexo.delete(0, 'end')
            e_telefone.delete(0, 'end')
            e_email.delete(0, 'end')

            b_confirmar.destroy()

            mostrar_dados()

        b_confirmar = Button(frame_baixo, command=confirmar, text='Confirmar', width=10, font=('Ivy 8 bold'), bg=co7, fg=co4, relief=RAISED, overrelief=RIDGE)
        b_confirmar.place(x=290, y=50)
    except:
        messagebox.showwarning('Dados', 'Por favor, selecione uma informação na tabela.')

def remover():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        cpf = str(tree_lista[1])
        remover_dados(cpf)

        messagebox.showinfo('Dados', 'Os dados formam deletados com sucesso!')

        for widget in frame_tabela.winfo_children():
            widget.destroy()
        
        mostrar_dados()

    except:
        messagebox.showwarning('Dados', 'Por favor, selecione uma informação na tabela.')

def buscar():
    cpf = e_buscar.get()

    dados = buscar_dados(cpf)

    tree.delete(*tree.get_children())

    for item in dados:
        tree.insert('', 'end', values=item)

    e_buscar.delete(0, 'end')


# configura frame_baixo

l_nome = Label(frame_baixo, text='Nome *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_nome.place(x=10, y=20)
e_nome = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
e_nome.place(x=80, y=20)

l_cpf = Label(frame_baixo, text='CPF *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_cpf.place(x=10, y=50)
e_cpf = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
e_cpf.place(x=80, y=50)

l_sexo = Label(frame_baixo, text='Sexo *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_sexo.place(x=10, y=80)
c_sexo = Combobox(frame_baixo, width=27)
c_sexo['value'] = ('', 'F', 'M')
c_sexo.place(x=80, y=80)

l_telefone = Label(frame_baixo, text='Telefone *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_telefone.place(x=10, y=110)
e_telefone = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
e_telefone.place(x=80, y=110)

l_email = Label(frame_baixo, text='Email  *', anchor=NW, font=('Ivy 10'), bg=co1, fg=co4)
l_email.place(x=10, y=140)
e_email = Entry(frame_baixo, width=25, justify='left', font=('', 10), highlightthickness=1)
e_email.place(x=80, y=140)


b_buscar = Button(frame_baixo, command=buscar, text='Buscar', font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_buscar.place(x=290, y=20)
e_buscar = Entry(frame_baixo, width=25, justify='left', font=('', 11), highlightthickness=1)
e_buscar.place(x=347, y=21)

b_listar = Button(frame_baixo, command=mostrar_dados, text='Listar dados', width=10, font=('Ivy 8 bold'), bg=co1, fg=co4, relief=RAISED, overrelief=RIDGE)
b_listar.place(x=290, y=50)

b_adicionar = Button(frame_baixo, command=inserir, text='Adicionar', width=10, font=('Ivy 8 bold'), bg=co5, fg=co4, relief=RAISED, overrelief=RIDGE)
b_adicionar.place(x=472, y=50)

b_atualizar = Button(frame_baixo, command=atualizar, text='Atualizar', width=10, font=('Ivy 8 bold'), bg=co7, fg=co4, relief=RAISED, overrelief=RIDGE)
b_atualizar.place(x=472, y=80)

b_deletar = Button(frame_baixo, command=remover, text='Deletar', width=10, font=('Ivy 8 bold'), bg=co6, fg=co4, relief=RAISED, overrelief=RIDGE)
b_deletar.place(x=472, y=110)


janela.mainloop()