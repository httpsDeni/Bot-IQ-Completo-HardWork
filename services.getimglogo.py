import json, requests, base64
from requests.auth import HTTPBasicAuth
from models.roboController import *

class LogoImg:

    def __init__(self, nomearq='logo.png'):
        self.host = HOST_NAME
        self.service = 'SE1/loadimgjplay'
        self.imagembase64 = ''
        self.imagem = nomearq
        self.get()

    def get(self):
        try:
            resp = requests.get((self.host + self.service), auth=(HTTPBasicAuth('xxx', '123')))
            if resp.status_code == 200:
                data = resp.json()
                self.imagembase64 = data['Imagem']
        except:
            pass