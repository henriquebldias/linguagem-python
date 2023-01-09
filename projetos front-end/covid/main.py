from html.entities import codepoint2name
from ipaddress import collapse_addresses
from tkinter import *
from tkinter import ttk
from tkinter.tix import COLUMN
from turtle import width
from urllib import response

############## importando bibliotecas
from PIL import Image
import requests

import string
import json

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
janela.geometry('835x360')
janela.configure(background=co1)
janela.resizable(width=FALSE, height=FALSE)

app_nome_frame = Frame(janela, width=840, height=50, bg=co2, relief="flat")
app_nome_frame.grid(row=0, column=0, columnspan=3, sticky=NSEW)

mostrar_frame_infectados = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_infectados.grid(row=1, column=0, sticky=NW, pady=5, padx=5)

mostrar_frame_recuperados = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_recuperados.grid(row=1, column=1, sticky=NW, pady=5, padx=5)

mostrar_frame_mortes = Frame(janela, width=220, height=100, bg=co2, relief="flat")
mostrar_frame_mortes.grid(row=1, column=2, sticky=NW, pady=5, padx=5)

select_frame = Frame(janela, width=840, height=50, bg=co2, relief="flat")
select_frame.grid(row=2, column=0, columnspan=3, sticky='n', pady=10)

########################### criando labels para app_nome_frame
app_nome = Label(app_nome_frame, text="COVID-19", width=20, height=1, pady=20, relief="flat", anchor=CENTER, font=("Helvetica 25 bold"), bg=co2, fg=co4)
app_nome.grid(row=0, column=0, pady=5)

########### Chamando API

response = requests.get("https://covid19.mathdro.id/api")
info = response
info = json.loads(info.text)

print(info["confirmed"]["value"])
print(info["recovered"]["value"])
print(info["deaths"]["value"])
print(info["lastUpdate"]["value"])

########################### criando labels para mostrar_frame_infectados
label_infectados = Label(mostrar_frame_infectados, text="Infectados", width=20, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co4)
label_infectados.grid(row=0, column=0, pady=1, padx=13)

mostrar_infectados = Label(mostrar_frame_infectados, text="42222", width=12, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co4)
mostrar_infectados.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_infectados, text="Quarta-feira 22/06/2020", width=25, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co4)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_infectados, text="Total de casos ativos de covid-19", width=33, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co4)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_azul = Label(mostrar_frame_infectados, text="", width=19, height=1, pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co3, fg=co2)
mostrar_azul.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

########################### criando labels para mostrar_frame_recuperados
label_recuperados = Label(mostrar_frame_recuperados, text="Recuperados", width=20, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co4)
label_recuperados.grid(row=0, column=0, pady=1, padx=13)

mostrar_infectados = Label(mostrar_frame_recuperados, text="42222", width=12, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co4)
mostrar_infectados.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_recuperados, text="Quarta-feira 22/06/2020", width=25, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co4)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_recuperados, text="Total de casos recuperados de covid-19", width=33, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co4)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_verde = Label(mostrar_frame_recuperados, text="", width=19, height=1, pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co7, fg=co2)
mostrar_verde.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

########################### criando labels para mostrar_frame_mortes
label_mortes = Label(mostrar_frame_mortes, text="Mortes", width=20, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 15 bold"), bg=co2, fg=co4)
label_mortes.grid(row=0, column=0, pady=1, padx=13)

mostrar_infectados = Label(mostrar_frame_mortes, text="42222", width=12, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 25 bold"), bg=co2, fg=co4)
mostrar_infectados.grid(row=1, column=0, pady=1)

mostrar_info = Label(mostrar_frame_mortes, text="Quarta-feira 22/06/2020", width=25, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 11 bold"), bg=co2, fg=co4)
mostrar_info.grid(row=2, column=0, pady=1)

mostrar_info = Label(mostrar_frame_mortes, text="Total de casos de mortes de covid-19", width=33, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Courier 8 bold"), bg=co2, fg=co4)
mostrar_info.grid(row=3, column=0, pady=1, padx=13)

mostrar_vermelho = Label(mostrar_frame_mortes, text="", width=19, height=1, pady=1, padx=0, relief="flat", anchor=NW, font=("Courier 1 bold"), bg=co6, fg=co2)
mostrar_vermelho.grid(row=4, column=0, pady=0, padx=0, sticky=NSEW)

############################ criando caixa de seleção

label_pais = Label(select_frame, text="Selecione o país", width=13, height=1, pady=7, padx=0, relief="flat", anchor=NW, font=("Ivy 12 bold"), bg=co2, fg=co4)
label_pais.grid(row=0, column=0, pady=1, padx=13)

pais = ["Angola", "Brasil", "Índia", "Portugal", "Estados Unidos", "França", "Espanha"]

combo = ttk.Combobox(select_frame, width=15, font=("Ivy 8 bold"))
combo["values"] = (pais)
combo.grid(row=0, column=1, padx=0, pady=13)


janela.mainloop()
