import json, requests
from requests.auth import HTTPBasicAuth
from datetime import datetime
from models.roboController import *
import base64

class ListaSinais:

    def __init__(self):
        self.host = HOST_NAME
        self.servicelista = 'SE1/jobsplaylist'
        self.servicearq = 'SE1/downloadlist'
        self.lista = []

    def getLista(self, idafiliado, tipolista):
        self.lista = []
        try:
            dados = {'afiliado':idafiliado,  'tipo':tipolista}
            resp = requests.get((self.host + self.servicelista), params=dados, auth=(HTTPBasicAuth('xxx', '123')))
            if resp.status_code == 200:
                self.lista = resp.json()
        except:
            pass

    def getArquivo(self, id):
        data = None
        try:
            dados = {'id': id}
            resp = requests.get((self.host + self.servicearq), params=dados, auth=(HTTPBasicAuth('xxx', '123')))
            if resp.status_code == 200:
                data = base64.decodestring(resp.content)
        except:
            pass

        return data