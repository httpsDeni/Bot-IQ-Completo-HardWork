import json, requests
from requests.auth import HTTPBasicAuth
from datetime import datetime, timedelta
import models.roboController as roboCtrl
from models.roboController import *
from services.utils import *
from main.roboUtils import *

class oLicenca:

    def __init__(self):
        self.status = -1
        self.idtipo = None
        self.tiponome = None
        self.datainic = None
        self.dataterm = None
        self.dataservidor = None
        self.chave = None
        self.idpacote = 0
        self.idafiliado = 0
        self.idtipolista = 0
        self.demo = False
        self.prime = False


class Licenca:

    def __init__(self):
        self.host = HOST_NAME
        self.service = 'SE1/validalicenca'
        self.Lic = oLicenca()
        self.valida = False
        self.mensagem = ''
        self.resposta = ''

    def get(self, registro, userid, idafiliado, sovalidar, origemsinal):
        self.valida = False
        self.mensagem = ''
        self.resposta = ''
        try:
            registro = Cripto64(registro, False)
            registro = str(registro).encode('utf-8')
            dados = {'registro':registro,  'userid':userid,  'sovalidar':sovalidar,  'afiliado':idafiliado}
            resp = requests.get((self.host + self.service), params=dados, auth=(HTTPBasicAuth('xxx', '123')))
            if resp.status_code != 200:
                self.mensagem = Idioma.traducao('Erro... Não houve comunição com servidor para validar sua licença. Código') + ' ' + str(resp.status_code)
            else:
                resp = Cripto64(resp.content, True)
                data = json.loads(resp)
                ret = False
                msg = ''
                for key, value in data[0].items():
                    if key.upper() == 'STATUS':
                        self.Lic.status = int(value)
                    else:
                        if key.upper() == 'MSG':
                            self.mensagem = value
                        else:
                            if key.upper() == 'DEMO':
                                self.Lic.demo = True if int(value) == 1 else False
                            else:
                                if key.upper() == 'PRIME':
                                    self.Lic.prime = True if int(value) == 1 else False
                                else:
                                    if key.upper() == 'IDTIPO':
                                        self.Lic.idtipo = int(value)
                                    else:
                                        if key.upper() == 'TIPO':
                                            self.Lic.tiponome = value
                                        else:
                                            if key.upper() == 'IDPACOTE':
                                                if value:
                                                    self.Lic.idpacote = value
                                            else:
                                                if key.upper() == 'IDAFILIADO':
                                                    if value:
                                                        self.Lic.idafiliado = value
                                                else:
                                                    if key.upper() == 'IDTIPOLISTA':
                                                        if value:
                                                            self.Lic.idtipolista = value
                                                    else:
                                                        if key.upper() == 'DATAINIC':
                                                            self.Lic.datainic = datetime.strptime(value, '%d/%m/%Y')
                                                        else:
                                                            if key.upper() == 'DATATERM':
                                                                self.Lic.dataterm = datetime.strptime(value, '%d/%m/%Y')
                                                            else:
                                                                if key.upper() == 'DATAAGORA':
                                                                    self.Lic.dataservidor = datetime.strptime(value, '%d/%m/%Y')
                                                                else:
                                                                    if key.upper() == 'CHAVE':
                                                                        self.Lic.chave = value

                if self.Lic.status > 0:
                    if self.Lic.dataterm < self.Lic.dataservidor:
                        self.Lic.status = 0
                        self.mensagem = Idioma.traducao('Licença expirou dia {}').format(self.Lic.dataterm.strftime('%d/%m/%Y'))
                    else:
                        if self.Lic.idafiliado != idafiliado:
                            if idafiliado > 0 and not self.Lic.demo:
                                self.Lic.status = 0
                                self.mensagem = Idioma.traducao('Sua licença não é valida para este robô.') + '\nCod. ' + str(idafiliado)
                            elif origemsinal == 1 and roboCtrl.instance().robo.prime:
                                self.Lic.status = self.Lic.prime or self.Lic.demo or 0
                                self.mensagem = Idioma.traducao('Este robô prime, só aceita licença prime.')
                            else:
                                pass
                        self.valida = True
                        self.resposta = Idioma.traducao('Licença: {} até {}').format(self.Lic.datainic.strftime('%d/%m/%Y'), self.Lic.dataterm.strftime('%d/%m/%Y'))
                        if self.Lic.dataterm - timedelta(days=5) <= self.Lic.dataservidor:
                            self.mensagem = Idioma.traducao('Sua licença vai expirar dia {}\nNão esqueça de renová-la!').format(self.Lic.dataterm.strftime('%d/%m/%Y'))
                else:
                    self.Lic.status = 0
                    if self.mensagem == '':
                        self.mensagem = Idioma.traducao('Licença não existe ou está vencida.')
        except Exception as e:
            try:
                LogSys.show(str(e))
                self.mensagem = Idioma.traducao('Erro... Não houve comunição com servidor.')
            finally:
                e = None
                del e