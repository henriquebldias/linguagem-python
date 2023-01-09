import requests
import datetime
import json


chave = '3dee52229fa2e42658fd4510755bfa00'
cidade = 'Bangalore'
api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}'.format(cidade, chave)

# fazendo chamado da API usando requests

r = requests.get(api_link)

# convertendo os dados presentes na variável r em dicionário

dados = r.json()

print(dados)