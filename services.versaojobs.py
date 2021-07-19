import json, requests
from requests.auth import HTTPBasicAuth
from models.roboController import *
from main.roboUtils import *

def getVersaoAtual():
    host = HOST_NAME
    service = 'SE1/getversaoatual'
    mensagem = ''
    versao = ''
    try:
        dados = {'tipo': '4'}
        resp = requests.get((host + service), params=dados, auth=(HTTPBasicAuth('jobs', '123')))
        if resp.status_code != 200:
            mensagem = Idioma.traducao('Erro... Não houve comunição com servidor.')
        else:
            data = resp.json()
            for key, value in data[0].items():
                if key.upper() == 'VERSAOATUAL':
                    versao = value

    except:
        mensagem = Idioma.traducao('Erro... Não houve comunição com servidor.')

    return (versao, mensagem)