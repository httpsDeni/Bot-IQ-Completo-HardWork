import os, json
from flask import Flask, request
from flask_classful import FlaskView, route
import services.scheduleservice as Agenda
from services import loadlist
from services.utils import *
import models.roboController as roboCtrl
from main.roboUtils import *
os.environ['WERKZEUG_RUN_MAIN'] = 'true'
appWeb = Flask(__name__)

def conectarWeb(porta=7770):
    appWeb.run(host='127.0.0.1', port=porta)


def desconectarWeb():
    try:
        func = request.environ.get('werkzeug.server.shutdown')
        if func is None:
            raise RuntimeError('Not running with the Werkzeug Server')
        func()
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e


def carregar(dados):
    try:
        dados = str(dados).split(';')
        datahora = dados[0]
        ativo = dados[1]
        acao = dados[2]
        duracao = dados[3]
        afiliado = int(dados[4])
        indicador = int(dados[5])
        if afiliado > 0:
            if roboCtrl.instance().robo.Lic.idafiliado != afiliado and not roboCtrl.instance().robo.Lic.demo:
                LogSys.save(Idioma.traducao('Sinal enviado pelo MT4, não é válido para este robô. Cod.') + str(afiliado))
            else:
                qtdlista, lista = loadlist.geraSinalMT4(2, datahora, ativo, acao, duracao, roboCtrl.instance().robo.ent_valor1, roboCtrl.instance().robo.ent_gale1, roboCtrl.instance().robo.ent_gale2)
                if qtdlista > 0:
                    Agenda.P(lista)
    except Exception as e:
        try:
            LogSys.save(str(e))
        finally:
            e = None
            del e


class viewAppWeb(FlaskView):

    def sinal(self, dados):
        if roboCtrl.instance().robo.iniciado:
            dados = Cripto64(dados, True)
            carregar(dados)
        return ('', 200)

    def sinalv2(self, dadosr):
        try:
            dados = dadosr.strip('\\r\\n')
            dados = dados.replace('\\r\\n', '')
            dados = dados + '=' * (-len(dados) % 4)
            dados = Cripto64(dados, True)
            if roboCtrl.instance().robo.iniciado:
                dados = json.loads(dados)
                if type(dados) is list:
                    for item in dados:
                        carregar(item['sinal'])

                else:
                    carregar(dados['sinal'])
            else:
                LogSys.save('Robo Desligado - Sinal recebido: {}', dados)
        except Exception as e:
            try:
                LogSys.save('==> {}', str(e))
            finally:
                e = None
                del e

        return ('', 200)


viewAppWeb.register(appWeb, route_base='/')