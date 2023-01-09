from tkinter import *
from tkinter import ttk
from turtle import width

# importar tkcalendar
from tkcalendar import Calendar, DateEntry 
# importar dateutil
from dateutil.relativedelta import relativedelta 

# importar datetime
from datetime import date

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
janela.title("Calculadora de Idade")
janela.geometry('310x400')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

#--------------- FRAMES -------------#

frame_cima = Frame(janela, width=310, height=140, pady=0, padx=0, relief=FLAT, bg=co4)
frame_cima.grid(row=0, column=0)

frame_baixo = Frame(janela, width=310, height=300, pady=0, padx=0, relief=FLAT, bg=co12)
frame_baixo.grid(row=1, column=0)

#----------------Label---------------#
# frame cima
l_calculadora = Label(frame_cima, text="CALCULADORA", width=25, height=1, padx=3, relief='flat', anchor='center', font=('Ivy 15 bold'), bg=co4, fg=co2)
l_calculadora.place(x=0, y=30)

l_idade = Label(frame_cima, text="DE IDADE", width=11, height=1, padx=0, relief='flat', anchor='center', font=('Arial 35 bold'), bg=co4, fg=co11)
l_idade.place(x=0, y=70)

# função calcular idade
def calcular_idade():
    inicial = cal_1.get()
    final = cal_2.get()

    # serapando os valores
    mes_1, dia_1, ano_1 = [ int(f) for f in inicial.split('/')]
    #convertendo para formato datetime
    data_inicial = date(ano_1, mes_1, dia_1)

     # serapando os valores
    mes_2, dia_2, ano_2 = [ int(f) for f in final.split('/')]
    #convertendo para formato datetime
    data_nascimento = date(ano_2, mes_2, dia_2)

    anos = relativedelta(data_inicial, data_nascimento).years
    meses = relativedelta(data_inicial, data_nascimento).months
    dias = relativedelta(data_inicial, data_nascimento).days

    l_app_anos['text'] = anos
    l_app_meses['text'] = meses
    l_app_dias['text'] = dias



#frame baixo
l_data_inicial = Label(frame_baixo, text="Data inicial", height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivy 11'), bg=co12, fg=co2)
l_data_inicial.place(x=40, y=30)

cal_1 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=co2, boderwidth=2, date_pattern='mm/dd/y', y=2022)
cal_1.place(x=180, y=30)

l_data_nascimento = Label(frame_baixo, text="Data de nascimento", height=1, padx=0, pady=0, relief='flat', anchor=NW, font=('Ivy 11'), bg=co12, fg=co2)
l_data_nascimento.place(x=40, y=70)

cal_2 = DateEntry(frame_baixo, width=13, bg='darkblue', fg=co2, boderwidth=2, date_pattern='mm/dd/y', y=2022)
cal_2.place(x=180, y=70)

l_app_anos = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=co12, fg=co2)
l_app_anos.place(x=60, y=135)

l_app_anos_nome = Label(frame_baixo, text="Anos", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=co12, fg=co2)
l_app_anos_nome.place(x=60, y=175)

l_app_meses = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=co12, fg=co2)
l_app_meses.place(x=140, y=135)

l_app_meses_nome = Label(frame_baixo, text="Meses", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=co12, fg=co2)
l_app_meses_nome.place(x=140, y=175)

l_app_dias = Label(frame_baixo, text="--", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 25 bold'), bg=co12, fg=co2)
l_app_dias.place(x=220, y=135)

l_app_dias_nome = Label(frame_baixo, text="Dias", height=1, padx=0, pady=0, relief='flat', anchor='center', font=('Ivy 11 bold'), bg=co12, fg=co2)
l_app_dias_nome.place(x=220, y=175)

#------------Criar botão calcular------------#
b_calcular = Button(frame_baixo, command=calcular_idade, text="Calcular", width=20, height=1, relief='raised', overrelief='ridge', font=('Ivy 10 bold'), bg=co12, fg=co2)
b_calcular.place(x=70, y=225)


janela.mainloop()
