import time
from datetime import datetime
import base64, json, os, configparser, PySimpleGUI as sg, schedule as B
from pathlib import Path
import log.path as R
import models.Balance as C
import models.sorosgale as sorosgale
from models.ThreadOperacion import *
from models.HorarioOperacao import HorarioOpera
from services import loadlist
from services.ativosopen import AtivosAbertos
import services.scheduleservice as Agenda
import services.servermt4 as serverWeb
from services.downloadlista import ListaSinais
from services.licencajobs import Licenca, oLicenca
from services.serversocket import *
import connection.APIConnection as API
import connection.RetryConnection as O
from connection.RetryConnection import *
import connection.CreateAPIConnection as N
from main.roboUtils import *
LIMITE_DIF = 3

class Robo:

    def __init__(self, versaoapp):
        self.pathexe = os.getcwd()
        self.arqConfig = 'Config.ini'
        self.arqLista = 'lista.txt'
        self.arqInit = ''
        self.lista = []
        self.listaMT4 = []
        self.lang = 'pt-br'
        self.prime = False
        self.touros2 = False
        self.versaoapp = versaoapp
        self.View = None
        self.iniciado = False
        self.avisarLicenca = True
        self.pesqAtivos = AtivosAbertos()
        self.ativosabertos = None
        self.ativos = None
        self.difHorarioIQ = 0
        self.imgbase64 = ''
        self.afiliadocfg = 0
        self.telegramTOKENAviso = ''
        self.serverWebAtivo = 0
        self.Lic = oLicenca()
        self.wslista = ListaSinais()
        self.srvSocket = None
        self.botTG = None
        self.schedMy = B
        self.schedMyList = []
        self.defaultConfig()
        LogConfig()
        self.PararTudo()

    def defaultConfig(self):
        self.senha = ''
        self.email = ''
        self.contareal = False
        self.usarsoros = False
        self.entfixamt4 = False
        self.gerenciar = 0
        self.prestop = True
        self.esperarIQ = False
        self.origemsinal = 0
        self.maxdelaymt4 = 0
        self.naonoticia = True
        self.notminantes = 0
        self.notminapos = 0
        self.ent_tipo = 'P'
        self.priorid = 0
        self.delay = 0
        self.ent_valor1 = 0
        self.ent_gale1 = 0
        self.ent_gale2 = 0
        self.qtdgales = 0
        self.valorinicial = 0
        self.percent = 0
        self.payoutmin = 80
        self.modelo = 'C'
        self.tipovalsoros = 'P'
        self.valorentsoros = 0
        self.nivelsoros = 0
        self.tipostop = 'P'
        self.stopgain = 1
        self.stoploss = 1
        self.tendusar = False
        self.tendemasma = False
        self.tendvelas = 20
        self.touros2 = False
        self.telegranusar = False
        self.telegranchatid = 0
        self.telegrantoken = ''
        self.percwinpos = 0
        self.ultrapassoustopwin = False
        self.manterConta = True
        self.cicloval10 = 0
        self.cicloval11 = 0
        self.cicloval12 = 0
        self.cicloval20 = 0
        self.cicloval21 = 0
        self.cicloval22 = 0
        self.cicloval30 = 0
        self.cicloval31 = 0
        self.cicloval32 = 0
        self.listahoraoperacao = []
        self.horariosOpera = []

    def loadConfig(self):
        if not os.path.isfile(self.arqConfig):
            LogSys.send(Idioma.traducao('Arquivo não localizado na pasta.') + ' ' + self.arqConfig)
            self.saveConfig()
            return []
        config = configparser.RawConfigParser()
        config.read(self.arqConfig)
        return config

    def setConfig(self, config):
        try:
            self.email = config['login']['email']
            self.contareal = config['login'].getboolean('contareal', False)
        except:
            self.email = ''
            self.contareal = False

        try:
            self.lang = config['idioma']['lang']
        except:
            self.lang = 'pt-br'

        try:
            self.gerenciar = int(config['config'].getfloat('gerenciar', 0))
            self.prestop = config['config'].getboolean('prestop', False)
            self.esperarIQ = config['config'].getboolean('esperarIQ', False)
            self.delay = int(config['config'].getfloat('delay', 0))
            self.naonoticia = config['config'].getboolean('naonoticia', False)
            self.touros2 = config['config'].getboolean('touros2', False)
            self.notminantes = int(config['config'].getfloat('notminantes', 10))
            self.notminapos = int(config['config'].getfloat('notminapos', 30))
            self.priorid = int(config['config'].getfloat('priorid', 0))
            self.maxdelaymt4 = int(config['config'].getfloat('maxdelaymt4', 0))
            self.entfixamt4 = config['config'].getboolean('entfixamt4', False)
            self.origemsinal = int(config['config'].getfloat('origemsinal', 0))
        except:
            self.gerenciar = 0
            self.prestop = True
            self.esperarIQ = False
            self.delay = 0
            self.naonoticia = True
            self.touros2 = False
            self.notminantes = 0
            self.notminapos = 0
            self.priorid = 0
            self.maxdelaymt4 = 0
            self.entfixamt4 = False
            self.origemsinal = 0

        try:
            self.valorinicial = config['inicio'].getfloat('valorinicial', 0.0)
            self.payoutmin = int(config['inicio'].getfloat('payoutmin', 80))
            self.qtdgales = int(config['inicio'].getfloat('qtdgales', 0))
            if config['inicio'].getboolean('tipostop', True):
                self.tipostop = 'P'
            else:
                self.tipostop = 'V'
            self.stopgain = config['inicio'].getfloat('stopgain', 1.0)
            self.stoploss = config['inicio'].getfloat('stoploss', 1.0)
            self.percwinpos = 0
        except:
            self.valorinicial = 0
            self.payoutmin = 80
            self.qtdgales = 0
            self.tipostop = 'P'
            self.stopgain = 1
            self.stoploss = 1
            self.percwinpos = 0

        try:
            if config['entradafixa'].getboolean('percentual', True):
                self.ent_tipo = 'P'
            else:
                self.ent_tipo = 'V'
            self.ent_valor1 = config['entradafixa'].getfloat('valor1')
            self.ent_gale1 = config['entradafixa'].getfloat('gale1')
            self.ent_gale2 = config['entradafixa'].getfloat('gale2')
        except:
            self.ent_tipo = 'P'
            self.ent_valor1 = 0
            self.ent_gale1 = 0
            self.ent_gale2 = 0

        try:
            self.percent = config['soros'].getfloat('percent')
            if config['soros'].getint('modelo') == 0:
                self.modelo = 'A'
            elif config['soros'].getint('modelo') == 1:
                self.modelo = 'M'
            else:
                self.modelo = 'C'
        except:
            self.percent = 0
            self.modelo = 'C'

        try:
            if config['soros'].getboolean('tipovalsoros', True):
                self.tipovalsoros = 'P'
            else:
                self.tipovalsoros = 'V'
            self.valorentsoros = config['soros'].getfloat('valorentsoros')
            self.nivelsoros = config['soros'].getfloat('nivelsoros')
        except:
            self.tipovalsoros = 'P'
            self.valorentsoros = 0
            self.nivelsoros = 0

        try:
            self.cicloval10 = config['ciclos'].getfloat('cicloval10')
            self.cicloval11 = config['ciclos'].getfloat('cicloval11')
            self.cicloval12 = config['ciclos'].getfloat('cicloval12')
            self.cicloval20 = config['ciclos'].getfloat('cicloval20')
            self.cicloval21 = config['ciclos'].getfloat('cicloval21')
            self.cicloval22 = config['ciclos'].getfloat('cicloval22')
            self.cicloval30 = config['ciclos'].getfloat('cicloval30')
            self.cicloval31 = config['ciclos'].getfloat('cicloval31')
            self.cicloval32 = config['ciclos'].getfloat('cicloval32')
        except:
            self.cicloval10 = 0
            self.cicloval11 = 0
            self.cicloval12 = 0
            self.cicloval20 = 0
            self.cicloval21 = 0
            self.cicloval22 = 0
            self.cicloval30 = 0
            self.cicloval31 = 0
            self.cicloval32 = 0

        try:
            self.tendusar = config['tendencia'].getboolean('tendusar', False)
            self.tendvelas = int(config['tendencia'].getfloat('tendvelas', 0))
            self.tendemasma = config['tendencia'].getboolean('tendemasma', False)
        except:
            self.tendusar = False
            self.tendemasma = False
            self.tendvelas = 20

        try:
            self.telegranusar = config['telegran'].getboolean('telegranusar', False)
            self.telegranchatid = int(config['telegran'].getfloat('telegranchatid', 0))
            self.telegrantoken = config['telegran']['telegrantoken']
        except:
            self.telegranusar = False
            self.telegranchatid = 0
            self.telegrantoken = ''

        try:
            self.listahoraoperacao = []
            self.horariosOpera = []
            itens = int(config['horariosoperacao'].getfloat('itens', 0))
            for idx in range(1, itens + 1):
                itemhr = config['horariosoperacao'][('hora' + str(idx))]
                ho = HorarioOpera()
                ho.importTxt(itemhr)
                self.horariosOpera.append(ho)
                self.listahoraoperacao.append(itemhr)

        except:
            self.horariosOpera = []

        Idioma.setlang(self.lang)

    def saveConfig(self):
        conf = configparser.RawConfigParser()
        conf.read(self.arqConfig)
        secao = 'idioma'
        if not conf.has_section(secao):
            conf.add_section(secao)
        conf.set(secao, 'lang', self.lang)
        secao = 'config'
        if not conf.has_section(secao):
            conf.add_section(secao)
        conf.set(secao, 'gerenciar', str(self.gerenciar))
        conf.set(secao, 'prestop', str(self.prestop))
        conf.set(secao, 'esperarIQ', str(self.esperarIQ))
        conf.set(secao, 'naonoticia', str(self.naonoticia))
        conf.set(secao, 'touros2', str(self.touros2))
        conf.set(secao, 'notminantes', str(self.notminantes))
        conf.set(secao, 'notminapos', str(self.notminapos))
        conf.set(secao, 'delay', str(self.delay))
        conf.set(secao, 'priorid', str(self.priorid))
        conf.set(secao, 'maxdelaymt4', str(self.maxdelaymt4))
        conf.set(secao, 'entfixamt4', str(self.entfixamt4))
        conf.set(secao, 'origemsinal', str(self.origemsinal))
        secao = 'inicio'
        if not conf.has_section(secao):
            conf.add_section(secao)
        conf.set(secao, 'valorinicial', str(self.valorinicial))
        conf.set(secao, 'payoutmin', str(self.payoutmin))
        conf.set(secao, 'qtdgales', str(self.qtdgales))
        if self.tipostop == 'P':
            conf.set(secao, 'tipostop', str(True))
        else:
            conf.set(secao, 'tipostop', str(False))
        conf.set(secao, 'stopgain', str(self.stopgain))
        conf.set(secao, 'stoploss', str(self.stoploss))
        secao = 'entradafixa'
        if not conf.has_section(secao):
            conf.add_section(secao)
        if self.ent_tipo == 'P':
            conf.set(secao, 'percentual', str(True))
        else:
            conf.set(secao, 'percentual', str(False))
        conf.set(secao, 'valor1', str(self.ent_valor1))
        conf.set(secao, 'gale1', str(self.ent_gale1))
        conf.set(secao, 'gale2', str(self.ent_gale2))
        secao = 'soros'
        if not conf.has_section(secao):
            conf.add_section(secao)
        conf.set(secao, 'percent', str(self.percent))
        if self.modelo == 'A':
            conf.set(secao, 'modelo', '0')
        elif self.modelo == 'M':
            conf.set(secao, 'modelo', '1')
        else:
            conf.set(secao, 'modelo', '2')
        if self.tipovalsoros == 'P':
            conf.set(secao, 'tipovalsoros', str(True))
        else:
            conf.set(secao, 'tipovalsoros', str(False))
        conf.set(secao, 'valorentsoros', str(self.valorentsoros))
        conf.set(secao, 'nivelsoros', str(self.nivelsoros))
        secao = 'ciclos'
        if not conf.has_section(secao):
            conf.add_section(secao)
        conf.set(secao, 'cicloval10', str(self.cicloval10))
        conf.set(secao, 'cicloval11', str(self.cicloval11))
        conf.set(secao, 'cicloval12', str(self.cicloval12))
        conf.set(secao, 'cicloval20', str(self.cicloval20))
        conf.set(secao, 'cicloval21', str(self.cicloval21))
        conf.set(secao, 'cicloval22', str(self.cicloval22))
        conf.set(secao, 'cicloval30', str(self.cicloval30))
        conf.set(secao, 'cicloval31', str(self.cicloval31))
        conf.set(secao, 'cicloval32', str(self.cicloval32))
        secao = 'tendencia'
        if not conf.has_section(secao):
            conf.add_section(secao)
        conf.set(secao, 'tendusar', str(self.tendusar))
        conf.set(secao, 'tendvelas', str(self.tendvelas))
        conf.set(secao, 'tendemasma', str(self.tendemasma))
        conf.write(open(self.arqConfig, 'w'))
        secao = 'telegran'
        if not conf.has_section(secao):
            conf.add_section(secao)
        conf.set(secao, 'telegranusar', str(self.telegranusar))
        conf.set(secao, 'telegranchatid', str(self.telegranchatid))
        conf.set(secao, 'telegrantoken', str(self.telegrantoken))
        conf.write(open(self.arqConfig, 'w'))
        if str(self.telegrantoken).strip() == '':
            if roboCtrl.instance().robo.botTG:
                try:
                    roboCtrl.instance().robo.botTG.stop_bot()
                    roboCtrl.instance().robo.botTG = None
                except:
                    roboCtrl.instance().robo.botTG = None

                idx = 0
                secao = 'horariosoperacao'
                if not conf.has_section(secao):
                    conf.add_section(secao)
            conf.set(secao, 'itens', str(len(self.listahoraoperacao)))
            for itemhr in self.listahoraoperacao:
                idx += 1
                conf.set(secao, 'hora' + str(idx), itemhr)

        conf.write(open(self.arqConfig, 'w'))

    def saveConfigTP(self, email, contareal):
        conf = configparser.RawConfigParser()
        conf.read(self.arqConfig)
        secao = 'login'
        if not conf.has_section(secao):
            conf.add_section(secao)
        conf.set(secao, 'email', email)
        conf.set(secao, 'contareal', str(contareal))
        conf.write(open(self.arqConfig, 'w'))

    def loadLista(self):
        if not os.path.isfile(self.arqLista):
            LogSys.send(Idioma.traducao('Arquivo não localizado na pasta.') + ' ' + self.arqLista)
            self.lista = []
            return 0
        self.lista = []
        qtdlista, self.lista = loadlist.geralista(self.arqLista, self.ent_valor1, self.ent_gale1, self.ent_gale2, self.usarsoros)
        return qtdlista

    def loadListaMT4(self):
        if not os.path.isfile(self.arqLista):
            LogSys.send(Idioma.traducao('Arquivo não localizado na pasta.') + ' ' + self.arqLista)
            self.listaMT4 = []
            return 0
        qtdlista = 0
        self.listaMT4 = []
        if self.ativosabertos:
            qtdlista, self.listaMT4 = loadlist.geralistaMT4(self.arqLista, self.ent_valor1, self.ent_gale1, self.ent_gale2)
        return qtdlista

    def clear_schedMy(self):
        for job in self.schedMyList:
            self.schedMy.cancel_job(job)

        self.schedMy = []
        self.schedMy.clear()
        self.schedMy = None
        self.schedMy = B

    def VerificarLicenca(self, idafiliado, userid, sovalidar='0'):
        ValidaLicenca = Licenca()
        ValidaLicenca.get(self.email, userid, idafiliado, sovalidar, self.origemsinal)
        self.Lic = ValidaLicenca.Lic
        roboCtrl.instance().view.janela['-licenca-'].update(value=(ValidaLicenca.resposta))
        roboCtrl.instance().view.janela.Refresh()
        valido = True
        if not ValidaLicenca.valida:
            valido = False
            if self.botTG:
                LogSys.send(ValidaLicenca.mensagem)
            else:
                sg.popup_error((Idioma.traducao('Atenção')), (ValidaLicenca.mensagem), no_titlebar=True,
                  keep_on_top=True,
                  text_color='black',
                  background_color='#DFDDDD')
        else:
            pass
        if not ValidaLicenca.mensagem != '' or self.avisarLicenca:
            if not self.Lic.demo:
                self.avisarLicenca = False
                if self.botTG:
                    LogSys.send(ValidaLicenca.mensagem)
                else:
                    sg.popup_ok((Idioma.traducao('Atenção')), (ValidaLicenca.mensagem), no_titlebar=True,
                      keep_on_top=True,
                      text_color='black',
                      background_color='#DFDDDD')
            return valido

    def Conectar(self, idafiliado):
        T = str(base64.b64encode(self.email.encode()))
        self.arqInit = str(R.logs_path) + '/' + T + '_init.conf'
        if os.path.exists(self.arqInit):
            os.remove(self.arqInit)
        if self.contareal:
            self.tipoconta = 'REAL'
        else:
            self.tipoconta = 'PRACTICE'
        if self.ent_tipo == 'P':
            self.ent_valor1 = round(self.valorinicial * self.ent_valor1 / 100, 2)
            self.ent_gale1 = round(self.valorinicial * self.ent_gale1 / 100, 2)
            self.ent_gale2 = round(self.valorinicial * self.ent_gale2 / 100, 2)
        if self.gerenciar == 0:
            if self.qtdgales < 1:
                self.ent_gale1 = 0
            if self.qtdgales < 2:
                self.ent_gale2 = 0
        elif self.gerenciar == 1:
            self.ent_valor1 = round(self.valorinicial * self.percent / 100, 2)
            self.ent_gale1 = 0
            self.ent_gale2 = 0
            if self.qtdgales > 0:
                self.ent_gale1 = 2
            if self.qtdgales > 1:
                self.ent_gale2 = 2
        elif self.gerenciar == 2:
            if self.tipovalsoros == 'P':
                self.ent_valor1 = round(self.valorinicial * self.valorentsoros / 100, 2)
            else:
                self.ent_valor1 = round(self.valorentsoros, 2)
            self.ent_gale1 = 0
            self.ent_gale2 = 0
            if self.qtdgales > 0:
                self.ent_gale1 = 2
            if self.qtdgales > 1:
                self.ent_gale2 = 2
        elif self.gerenciar == 3:
            self.ent_valor1 = round(self.cicloval10, 2)
            self.ent_gale1 = 0
            self.ent_gale2 = 0
            if self.qtdgales > 0:
                self.ent_gale1 = 2
            if self.qtdgales > 1:
                self.ent_gale2 = 2
        if self.gerenciar == 0:
            self.usarsoros = False
        else:
            self.usarsoros = True
        if not self.prime:
            self.entfixamt4 = False
        LogSys.send(Idioma.traducao('Aguarde, conectando a IQ...'))
        self.View.janela.Refresh()
        N.createapiconnection(self.email, self.senha, self.tipoconta)
        conect = API.instance().connection
        if conect:
            if self.VerificarLicenca(idafiliado, API.instance().userID, '0'):
                C.instance().actual_balance = 0
                C.instance().actual_balance2 = 0
                if self.tipostop == 'P':
                    X = self.stopgain / 100
                    Z = self.stoploss / 100
                    C.instance().win_limit = self.valorinicial * X
                    C.instance().stop_limit = self.valorinicial * Z * -1
                else:
                    C.instance().win_limit = self.stopgain
                    C.instance().stop_limit = self.stoploss * -1
                LogSys.addMsg('Versão: ' + self.versaoapp)
                LogSys.addMsg(Idioma.traducao('Tipo de conta:') + ' {}', self.tipoconta)
                if self.origemsinal == 1:
                    LogSys.addMsg(Idioma.traducao('Origem Sinais') + ': MetaTrader')
                elif self.origemsinal == 2:
                    LogSys.addMsg(Idioma.traducao('Origem Sinais') + ': ' + Idioma.traducao('Servidor Sinais'))
                if self.origemsinal > 0:
                    if self.maxdelaymt4 > 0:
                        LogSys.addMsg('Máx. delay {}', self.maxdelaymt4)
                LogSys.addMsg(Idioma.traducao('Parâmetros iniciais:'))
                LogSys.addMsg(Idioma.traducao('Valor inicial: $') + '{}', round(self.valorinicial, 2))
                LogSys.addMsg(Idioma.traducao('Quantidade de gales:') + ' {}', self.qtdgales)
                LogSys.addMsg(Idioma.traducao('Payout mínimo:') + ' {}', self.payoutmin)
                if self.prestop:
                    LogSys.addMsg(Idioma.traducao('Pré-Stop Loss: Ligado'))
                if self.esperarIQ:
                    LogSys.addMsg(Idioma.traducao('Resultado Resp. IQ'))
                else:
                    LogSys.addMsg(Idioma.traducao('Resultado por Taxas'))
                LogSys.addMsg('Delay: {}', self.delay)
                if self.priorid == 0:
                    LogSys.addMsg(Idioma.traducao('Prioridade') + ': ' + Idioma.traducao('Maior Payout'))
                elif self.priorid == 1:
                    LogSys.addMsg(Idioma.traducao('Prioridade') + ': ' + Idioma.traducao('Digital'))
                elif self.priorid == 2:
                    LogSys.addMsg(Idioma.traducao('Prioridade') + ': ' + Idioma.traducao('Binárias'))
                elif self.priorid == 3:
                    LogSys.addMsg(Idioma.traducao('Prioridade') + ': ' + Idioma.traducao('Somente Digital'))
                elif self.priorid == 4:
                    LogSys.addMsg(Idioma.traducao('Prioridade') + ': ' + Idioma.traducao('Somente Binárias'))
                if self.naonoticia:
                    LogSys.addMsg(Idioma.traducao('Não operar em notícia'))
                if self.touros2:
                    LogSys.addMsg(Idioma.traducao('Incluir Notícias 2 Touros'))
                if self.tendusar:
                    if self.tendemasma:
                        LogSys.addMsg(Idioma.traducao('Não Operar Contra') + ': ' + Idioma.traducao('Usar EMA5 + EMA20'))
                    else:
                        LogSys.addMsg(Idioma.traducao('Não Operar Contra') + ': ' + Idioma.traducao('Quant. Velas') + ': {}', self.tendvelas)
                if self.telegranusar:
                    LogSys.addMsg('Telegran: ' + Idioma.traducao(Idioma.traducao('Autorizo o envio dos resultados')))
                if len(self.listahoraoperacao) > 0:
                    LogSys.addMsg(Idioma.traducao('Horários de Operação') + ':')
                    for itemhr in self.listahoraoperacao:
                        LogSys.addMsg(itemhr)

                if self.gerenciar == 0:
                    LogSys.addMsg(Idioma.traducao('Entradas fixas:'))
                    LogSys.addMsg(Idioma.traducao('Entrada: $') + '{}', round(self.ent_valor1, 2))
                    if self.ent_gale1 > 0:
                        LogSys.addMsg(Idioma.traducao('Gale 1: $') + '{}', round(self.ent_gale1, 2))
                    if self.ent_gale2 > 0:
                        LogSys.addMsg(Idioma.traducao('Gale 2: $') + '{}', round(self.ent_gale2, 2))
                elif self.gerenciar == 1:
                    LogSys.addMsg('SorosGale:')
                    if self.modelo == 'A':
                        LogSys.addMsg(Idioma.traducao('Modelo: Agressivo'))
                    elif self.modelo == 'M':
                        LogSys.addMsg(Idioma.traducao('Modelo: Moderado'))
                    else:
                        LogSys.addMsg(Idioma.traducao('Modelo: Conservador'))
                    LogSys.addMsg(Idioma.traducao('1ª entrada: %') + '{} | ' + Idioma.traducao('Valor: $') + '{}', self.percent, round(self.ent_valor1, 2))
                elif self.gerenciar == 2:
                    LogSys.addMsg('Soros: Nível {}', self.nivelsoros)
                    if self.tipovalsoros == 'P':
                        LogSys.addMsg(Idioma.traducao('1ª entrada: %') + '{} | ' + Idioma.traducao('Valor: $') + '{}', self.valorentsoros, round(self.ent_valor1, 2))
                    else:
                        LogSys.addMsg(Idioma.traducao('1ª entrada: $') + '{}', round(self.ent_valor1, 2))
                elif self.gerenciar == 3:
                    if self.qtdgales > 0:
                        LogSys.addMsg(Idioma.traducao('Ciclos') + ' -> ' + Idioma.traducao('Gale'))
                        LogSys.addMsg(Idioma.traducao('Ciclo') + ' 1 | ' + Idioma.traducao('Entrada') + ' ${} ' + Idioma.traducao('Gale') + '1 ${} ' + Idioma.traducao('Gale') + '2 ${}', round(self.cicloval10, 2), round(self.cicloval11, 2), round(self.cicloval12, 2))
                        LogSys.addMsg(Idioma.traducao('Ciclo') + ' 2 | ' + Idioma.traducao('Entrada') + ' ${} ' + Idioma.traducao('Gale') + '1 ${} ' + Idioma.traducao('Gale') + '2 ${}', round(self.cicloval20, 2), round(self.cicloval21, 2), round(self.cicloval22, 2))
                        LogSys.addMsg(Idioma.traducao('Ciclo') + ' 3 | ' + Idioma.traducao('Entrada') + ' ${} ' + Idioma.traducao('Gale') + '1 ${} ' + Idioma.traducao('Gale') + '2 ${}', round(self.cicloval30, 2), round(self.cicloval31, 2), round(self.cicloval32, 2))
                    else:
                        LogSys.addMsg(Idioma.traducao('Ciclos'))
                        LogSys.addMsg(Idioma.traducao('Ciclo') + ' 1 | ' + Idioma.traducao('Entrada') + ' (1) ${} | (2) ${} | (3) ${}', round(self.cicloval10, 2), round(self.cicloval11, 2), round(self.cicloval12, 2))
                        LogSys.addMsg(Idioma.traducao('Ciclo') + ' 2 | ' + Idioma.traducao('Entrada') + ' (4) ${} | (5) ${} | (6) ${}', round(self.cicloval20, 2), round(self.cicloval21, 2), round(self.cicloval22, 2))
                        LogSys.addMsg(Idioma.traducao('Ciclo') + ' 3 | ' + Idioma.traducao('Entrada') + ' (7) ${} | (8) ${} | (9) ${}', round(self.cicloval30, 2), round(self.cicloval31, 2), round(self.cicloval32, 2))
                LogSys.addMsg('WIN %{} - ' + Idioma.traducao('Parar de operar quando atingir: $') + '{}', self.stopgain, round(C.instance().win_limit, 2))
                LogSys.addMsg('LOSS %{} - ' + Idioma.traducao('Parar de operar quando atingir: $') + '{}', self.stoploss, round(C.instance().stop_limit, 2))
                LogSys.sendMsg()
                self.View.janela['valorinic'].update(value=(round(self.valorinicial, 2)))
                self.View.janela['saldoatual'].update(value=(C.instance().balance))
                self.View.janela['stopgainp'].update(value=(self.stopgain))
                self.View.janela['stopgainv'].update(value=(round(C.instance().win_limit, 2)))
                self.View.janela['stoplossp'].update(value=(self.stoploss))
                self.View.janela['stoplossv'].update(value=(round(C.instance().stop_limit, 2)))
                self.View.janela.Refresh()
                if self.gerenciar == 0:
                    C.instance().sorosgale.config_ini(0, self.percent, self.modelo, 1, 'P')
                elif self.gerenciar == 1:
                    C.instance().sorosgale.config_ini(self.valorinicial, self.percent, self.modelo, 1, 'P')
                elif self.gerenciar == 2:
                    if self.tipovalsoros == 'P':
                        C.instance().sorosgale.config_ini(self.valorinicial, self.valorentsoros, 'S', self.nivelsoros, 'P')
                    else:
                        C.instance().sorosgale.config_ini(self.valorentsoros, 0, 'S', self.nivelsoros, 'V')
                elif self.gerenciar == 3:
                    C.instance().sorosgale.config_ini(self.cicloval10, 0, 'L' + str(self.qtdgales))
                    C.instance().sorosgale.config_ciclos(self.cicloval10, self.cicloval11, self.cicloval12, self.cicloval20, self.cicloval21, self.cicloval22, self.cicloval30, self.cicloval31, self.cicloval32)
                return True
        return False

    def AtualizaGridAgenda(self):
        try:
            data = []
            for sinal in roboCtrl.instance().operContrl.agenda:
                item = ['{:03d}'.format(int(sinal.op_id)),
                 sinal.programmedHour.strftime('%d/%m/%y'),
                 sinal.programmedHour.strftime('%H:%M:%S'),
                 sinal.pair,
                 sinal.direction.upper(),
                 sinal.expirationMode,
                 sinal.situacao,
                 '{:18.2f}'.format(float(sinal.lucro))]
                data.append(item)

            roboCtrl.instance().view.janela['-TABLE-'].update(values=data)
            roboCtrl.instance().view.janela.Refresh()
        except:
            pass

    def PararTudo(self):
        self.iniciado = False
        self.pesqAtivos.stop_ativos()
        roboCtrl.instance().clear_operacoes
        self.clear_schedMy()
        self.serverWebAtivo = 0
        if self.srvSocket:
            self.srvSocket.sel.close()
            self.srvSocket.srvsocket.close()
            self.srvSocket = None

    def VerificaDifHorario(self):
        self.difHorarioIQ = 0
        O().verify_connection()
        if abs(self.difHorarioIQ) <= LIMITE_DIF:
            return True
        return False

    def IniciarAgendamentos(self):
        if self.loadLista() == 0:
            LogSys.send(Idioma.traducao('Lista vazia ou com dia/horário expirados.'))
            return
        self.iniciado = True
        if self.VerificaDifHorario():
            Agenda.C(self.lista)
            self.AtualizaGridAgenda()
            LogSys.send(Idioma.traducao('Agendamento realizado com sucesso!'))
            self.ExecutaAgendamento()
        else:
            self.iniciado = False
            LogSys.send(Idioma.traducao('Diferença de horário do seu pc com a IQ, está muito alta!') + ' Limite={}', LIMITE_DIF)

    def IniciarAgendamentosMT4(self):
        self.iniciado = True
        if self.VerificaDifHorario():
            roboCtrl.instance().operContrl.agenda = []
            self.AtualizaGridAgenda()
            LogSys.send(Idioma.traducao('Aguardando sinais do MetaTrader!'))
            self.ExecutaAgendamentoMT4()
        else:
            self.iniciado = False
            LogSys.send(Idioma.traducao('Diferença de horário do seu pc com a IQ, está muito alta!') + ' Limite={}', LIMITE_DIF)

    def IniciarAgendamentosServer(self):
        self.iniciado = True
        if self.VerificaDifHorario():
            roboCtrl.instance().operContrl.agenda = []
            self.AtualizaGridAgenda()
            LogSys.send(Idioma.traducao('Aguardando sinais do servidor!'))
            self.ExecutaAgendamentoServer()
        else:
            self.iniciado = False
            LogSys.send(Idioma.traducao('Diferença de horário do seu pc com a IQ, está muito alta!') + ' Limite={}', LIMITE_DIF)

    def IniciarAgendamentosSocket(self):
        self.iniciado = True
        if self.VerificaDifHorario():
            roboCtrl.instance().operContrl.agenda = []
            self.AtualizaGridAgenda()
            LogSys.send(Idioma.traducao('Aguardando sinais do MetaTrader!'))
            T10 = ThreadOper(target=(self.ExecutaAgendamentoSocket))
            roboCtrl.instance().add_listThread = T10
            T10.start()
        else:
            self.iniciado = False
            LogSys.send(Idioma.traducao('Diferença de horário do seu pc com a IQ, está muito alta!') + ' Limite={}', LIMITE_DIF)

    def ExecutaAgendamento(self):
        self.pesqAtivos.start_ativos()
        roboCtrl.instance().clear_operacoes
        while self.iniciado:
            self.schedMy.run_pending()
            time.sleep(1)

    def ExecutaSegundoPlano(self):
        ThrAgenda = ThreadOper(target=(self.AgendaSegundoPlano))
        roboCtrl.instance().add_listThread = ThrAgenda
        ThrAgenda.start()

    def AgendaSegundoPlano(self):
        while self.iniciado:
            self.schedMy.run_pending()
            time.sleep(1)

    def ExecutaAgendamentoMT4(self):
        O().verify_connection()
        self.pesqAtivos.start_ativos()
        if self.serverWebAtivo == 0:
            self.ExecutaSegundoPlano()
            self.serverWebAtivo = 1
            serverWeb.conectarWeb()

    def ExecutaAgendamentoServer(self):
        O().verify_connection()
        self.pesqAtivos.start_ativos()
        if self.serverWebAtivo == 0:
            self.ExecutaSegundoPlano()
            self.serverWebAtivo = 1
            serverWeb.conectarWeb(7780)

    def createSocket(self):
        if self.srvSocket:
            self.srvSocket.sel.close()
            self.srvSocket.srvsocket.close()
            self.srvSocket = None
        self.srvSocket = serverSocket('127.0.0.1', 7720)

    def ExecutaAgendamentoSocket(self):
        O().verify_connection()
        self.pesqAtivos.start_ativos()
        self.ExecutaSegundoPlano()
        self.createSocket()
        while self.iniciado:
            try:
                eventsel = self.srvSocket.sel.select(timeout=None)
                for key, mask in eventsel:
                    sock = key.fileobj
                    if key.data is None:
                        self.srvSocket.accept_wrapper(key.fileobj)
                    else:
                        self.srvSocket.service_connection(key, mask)

            except Exception as e:
                try:
                    LogSys.show('{}', str(e))
                    try:
                        if sock:
                            self.srvSocket.sel.unregister(sock)
                            sock.close()
                    except:
                        pass

                    if self.iniciado:
                        self.createSocket()
                finally:
                    e = None
                    del e