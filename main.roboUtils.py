from datetime import datetime
import PySimpleGUI as sg
import models.roboController as roboCtrl
from models.HorarioOperacao import HorarioOpera
from services.noticias import *
from models.Traducao import *
from log.logger import *
Idioma = Traduzir()
LogSys = LogConfig()

def LeConfig():
    roboCtrl.instance().view.janela['email'].update(roboCtrl.instance().robo.email)
    if roboCtrl.instance().robo.contareal:
        roboCtrl.instance().view.janela['contatipo'].update(value=(Idioma.traducao('Real')))
    else:
        roboCtrl.instance().view.janela['contatipo'].update(value=(Idioma.traducao('Treinamento')))
    if roboCtrl.instance().robo.lang == 'ing':
        roboCtrl.instance().view.janela['opclang'].update(value='Inglês')
    elif roboCtrl.instance().robo.lang == 'esp':
        roboCtrl.instance().view.janela['opclang'].update(value='Espanhol')
    else:
        roboCtrl.instance().view.janela['opclang'].update(value='Pt-BR')
    if roboCtrl.instance().robo.gerenciar == 0:
        roboCtrl.instance().view.janela['gerenciar'].update(value=(Idioma.traducao('Entradas Fixas')))
    elif roboCtrl.instance().robo.gerenciar == 1:
        roboCtrl.instance().view.janela['gerenciar'].update(value='SorosGale')
    elif roboCtrl.instance().robo.gerenciar == 2:
        roboCtrl.instance().view.janela['gerenciar'].update(value='Soros')
    elif roboCtrl.instance().robo.gerenciar == 3:
        roboCtrl.instance().view.janela['gerenciar'].update(value=(Idioma.traducao('Ciclos')))
    roboCtrl.instance().view.janela['prestop'].update(value=(roboCtrl.instance().robo.prestop))
    roboCtrl.instance().view.janela['entfixamt4'].update(value=(roboCtrl.instance().robo.entfixamt4))
    if roboCtrl.instance().robo.esperarIQ:
        roboCtrl.instance().view.janela['esperarIQ'].update(value=(Idioma.traducao('Resultado Resp. IQ')))
    else:
        roboCtrl.instance().view.janela['esperarIQ'].update(value=(Idioma.traducao('Resultado por Taxas')))
    roboCtrl.instance().view.janela['naonoticia'].update(value=(roboCtrl.instance().robo.naonoticia))
    roboCtrl.instance().view.janela['touros2'].update(value=(roboCtrl.instance().robo.touros2))
    roboCtrl.instance().view.janela['notminantes'].update(value=(roboCtrl.instance().robo.notminantes))
    roboCtrl.instance().view.janela['notminapos'].update(value=(roboCtrl.instance().robo.notminapos))
    roboCtrl.instance().view.janela['delay'].update(value=(roboCtrl.instance().robo.delay))
    if roboCtrl.instance().robo.priorid == 0:
        roboCtrl.instance().view.janela['priorid'].update(value=(Idioma.traducao('Maior Payout')))
    elif roboCtrl.instance().robo.priorid == 1:
        roboCtrl.instance().view.janela['priorid'].update(value=(Idioma.traducao('Digital')))
    elif roboCtrl.instance().robo.priorid == 2:
        roboCtrl.instance().view.janela['priorid'].update(value=(Idioma.traducao('Binárias')))
    elif roboCtrl.instance().robo.priorid == 3:
        roboCtrl.instance().view.janela['priorid'].update(value=(Idioma.traducao('Somente Digital')))
    elif roboCtrl.instance().robo.priorid == 4:
        roboCtrl.instance().view.janela['priorid'].update(value=(Idioma.traducao('Somente Binárias')))
    if roboCtrl.instance().robo.prime:
        if roboCtrl.instance().robo.origemsinal == 0:
            roboCtrl.instance().view.janela['origemsinal'].update(value=(Idioma.traducao('Lista de Sinais')))
        elif roboCtrl.instance().robo.origemsinal == 1:
            roboCtrl.instance().view.janela['origemsinal'].update(value='MetaTrader')
        else:
            roboCtrl.instance().view.janela['origemsinal'].update(value=(Idioma.traducao('Servidor Sinais')))
    elif roboCtrl.instance().robo.origemsinal == 0:
        roboCtrl.instance().view.janela['origemsinal44'].update(value=(Idioma.traducao('Lista de Sinais')))
    else:
        roboCtrl.instance().view.janela['origemsinal44'].update(value=(Idioma.traducao('Servidor Sinais')))
    roboCtrl.instance().view.janela['maxdelaymt4'].update(value=(roboCtrl.instance().robo.maxdelaymt4))
    roboCtrl.instance().view.janela['maxdelaymt44'].update(value=(roboCtrl.instance().robo.maxdelaymt4))
    roboCtrl.instance().view.janela['tendusar'].update(value=(roboCtrl.instance().robo.tendusar))
    roboCtrl.instance().view.janela['tendvelas'].update(value=(roboCtrl.instance().robo.tendvelas))
    if roboCtrl.instance().robo.tendemasma:
        roboCtrl.instance().view.janela['tendqtdvela'].update(value=False)
    else:
        roboCtrl.instance().view.janela['tendqtdvela'].update(value=True)
    roboCtrl.instance().view.janela['tendemasma'].update(value=(roboCtrl.instance().robo.tendemasma))
    roboCtrl.instance().view.janela['telegranusar'].update(value=(roboCtrl.instance().robo.telegranusar))
    roboCtrl.instance().view.janela['telegranchatid'].update(value=(roboCtrl.instance().robo.telegranchatid))
    roboCtrl.instance().view.janela['telegrantoken'].update(roboCtrl.instance().robo.telegrantoken)
    roboCtrl.instance().view.janela['valinic'].update(value=(roboCtrl.instance().robo.valorinicial))
    roboCtrl.instance().view.janela['payout'].update(value=(roboCtrl.instance().robo.payoutmin))
    roboCtrl.instance().view.janela['qtdgale'].update(value=(roboCtrl.instance().robo.qtdgales))
    if roboCtrl.instance().robo.ent_tipo == 'P':
        roboCtrl.instance().view.janela['percent'].update(value=(Idioma.traducao('Percentual')))
    else:
        roboCtrl.instance().view.janela['percent'].update(value=(Idioma.traducao('Valor')))
    roboCtrl.instance().view.janela['valor1'].update(value=(roboCtrl.instance().robo.ent_valor1))
    roboCtrl.instance().view.janela['gale1'].update(value=(roboCtrl.instance().robo.ent_gale1))
    roboCtrl.instance().view.janela['gale2'].update(value=(roboCtrl.instance().robo.ent_gale2))
    roboCtrl.instance().view.janela['percentsoros'].update(value=(roboCtrl.instance().robo.percent))
    if roboCtrl.instance().robo.modelo == 'A':
        roboCtrl.instance().view.janela['modelo'].update(value=(Idioma.traducao('Agressivo')))
    elif roboCtrl.instance().robo.modelo == 'M':
        roboCtrl.instance().view.janela['modelo'].update(value=(Idioma.traducao('Moderado')))
    elif roboCtrl.instance().robo.modelo == 'C':
        roboCtrl.instance().view.janela['modelo'].update(value=(Idioma.traducao('Conservador')))
    if roboCtrl.instance().robo.tipostop == 'P':
        roboCtrl.instance().view.janela['tipostop'].update(value=(Idioma.traducao('Percentual')))
    else:
        roboCtrl.instance().view.janela['tipostop'].update(value=(Idioma.traducao('Valor')))
    if roboCtrl.instance().robo.tipovalsoros == 'P':
        roboCtrl.instance().view.janela['tipovalsoros'].update(value=(Idioma.traducao('Percentual')))
    else:
        roboCtrl.instance().view.janela['tipovalsoros'].update(value=(Idioma.traducao('Valor')))
    roboCtrl.instance().view.janela['valorentsoros'].update(value=(roboCtrl.instance().robo.valorentsoros))
    roboCtrl.instance().view.janela['nivelsoros'].update(value=(roboCtrl.instance().robo.nivelsoros))
    roboCtrl.instance().view.janela['stopgain'].update(value=(roboCtrl.instance().robo.stopgain))
    roboCtrl.instance().view.janela['stoploss'].update(value=(roboCtrl.instance().robo.stoploss))
    roboCtrl.instance().view.janela['cicloval10'].update(value=(roboCtrl.instance().robo.cicloval10))
    roboCtrl.instance().view.janela['cicloval11'].update(value=(roboCtrl.instance().robo.cicloval11))
    roboCtrl.instance().view.janela['cicloval12'].update(value=(roboCtrl.instance().robo.cicloval12))
    roboCtrl.instance().view.janela['cicloval20'].update(value=(roboCtrl.instance().robo.cicloval20))
    roboCtrl.instance().view.janela['cicloval21'].update(value=(roboCtrl.instance().robo.cicloval21))
    roboCtrl.instance().view.janela['cicloval22'].update(value=(roboCtrl.instance().robo.cicloval22))
    roboCtrl.instance().view.janela['cicloval30'].update(value=(roboCtrl.instance().robo.cicloval30))
    roboCtrl.instance().view.janela['cicloval31'].update(value=(roboCtrl.instance().robo.cicloval31))
    roboCtrl.instance().view.janela['cicloval32'].update(value=(roboCtrl.instance().robo.cicloval32))
    roboCtrl.instance().view.janela['-LISTAHORAOPERA-'].update(values=(roboCtrl.instance().robo.listahoraoperacao))
    roboCtrl.instance().view.janela.refresh()
    ZeraPlacarTotal()
    roboCtrl.instance().view.janela['-Parar-'].update(disabled=True)
    getNoticias()
    roboCtrl.instance().view.janela.Refresh()


def ZeraPlacarTotal():
    roboCtrl.instance().operContrl.zerar()
    roboCtrl.instance().view.janela['saldoatual'].update(value=0.0)
    roboCtrl.instance().view.janela['stopgainp'].update(value=0)
    roboCtrl.instance().view.janela['stopgainv'].update(value=0.0)
    roboCtrl.instance().view.janela['stoplossp'].update(value=0)
    roboCtrl.instance().view.janela['stoplossv'].update(value=0.0)
    roboCtrl.instance().view.janela['valorinic'].update(value=0.0)
    roboCtrl.instance().view.janela['placarW'].update(value=0)
    roboCtrl.instance().view.janela['placarH'].update(value=0)
    roboCtrl.instance().view.janela['assertividade'].update(value=0.0)
    roboCtrl.instance().view.janela['saldolucro'].update(value=0.0)
    roboCtrl.instance().view.janela.Refresh()


def tratarFloat(value: str):
    try:
        return round(float(value), 2)
    except:
        return 0


def GravaConfig(values):
    if values['opclang'] == 'Inglês':
        roboCtrl.instance().robo.lang = 'ing'
    elif values['opclang'] == 'Espanhol':
        roboCtrl.instance().robo.lang = 'esp'
    else:
        roboCtrl.instance().robo.lang = 'pt-br'
    if values['gerenciar'] == Idioma.traducao('Entradas Fixas'):
        roboCtrl.instance().robo.gerenciar = 0
    elif values['gerenciar'] == 'SorosGale':
        roboCtrl.instance().robo.gerenciar = 1
    elif values['gerenciar'] == 'Soros':
        roboCtrl.instance().robo.gerenciar = 2
    elif values['gerenciar'] == Idioma.traducao('Ciclos'):
        roboCtrl.instance().robo.gerenciar = 3
    if values['prestop'] == True:
        roboCtrl.instance().robo.prestop = True
    else:
        roboCtrl.instance().robo.prestop = False
    if values['entfixamt4'] == True:
        roboCtrl.instance().robo.entfixamt4 = True
    else:
        roboCtrl.instance().robo.entfixamt4 = False
    if values['esperarIQ'] == Idioma.traducao('Resultado por Taxas'):
        roboCtrl.instance().robo.esperarIQ = False
    elif values['esperarIQ'] == Idioma.traducao('Resultado Resp. IQ'):
        roboCtrl.instance().robo.esperarIQ = True
    if roboCtrl.instance().robo.prime:
        if values['origemsinal'] == Idioma.traducao('Servidor Sinais'):
            roboCtrl.instance().robo.origemsinal = 2
        elif values['origemsinal'] == 'MetaTrader' and roboCtrl.instance().robo.prime:
            roboCtrl.instance().robo.origemsinal = 1
        else:
            roboCtrl.instance().robo.origemsinal = 0
        roboCtrl.instance().robo.maxdelaymt4 = int(tratarFloat(values['maxdelaymt4']))
    else:
        if values['origemsinal44'] == Idioma.traducao('Servidor Sinais'):
            roboCtrl.instance().robo.origemsinal = 2
        else:
            roboCtrl.instance().robo.origemsinal = 0
        roboCtrl.instance().robo.maxdelaymt4 = int(tratarFloat(values['maxdelaymt44']))
    if values['naonoticia'] == True:
        roboCtrl.instance().robo.naonoticia = True
    else:
        roboCtrl.instance().robo.naonoticia = False
    touros2_alterado = False
    if roboCtrl.instance().robo.touros2 != values['touros2']:
        touros2_alterado = True
    if values['touros2'] == True:
        roboCtrl.instance().robo.touros2 = True
    else:
        roboCtrl.instance().robo.touros2 = False
    roboCtrl.instance().robo.notminantes = int(tratarFloat(values['notminantes']))
    roboCtrl.instance().robo.notminapos = int(tratarFloat(values['notminapos']))
    roboCtrl.instance().robo.delay = int(tratarFloat(values['delay']))
    if values['priorid'] == Idioma.traducao('Maior Payout'):
        roboCtrl.instance().robo.priorid = 0
    elif values['priorid'] == Idioma.traducao('Digital'):
        roboCtrl.instance().robo.priorid = 1
    elif values['priorid'] == Idioma.traducao('Binárias'):
        roboCtrl.instance().robo.priorid = 2
    elif values['priorid'] == Idioma.traducao('Somente Digital'):
        roboCtrl.instance().robo.priorid = 3
    elif values['priorid'] == Idioma.traducao('Somente Binárias'):
        roboCtrl.instance().robo.priorid = 4
    if values['tendusar'] == True:
        roboCtrl.instance().robo.tendusar = True
    else:
        roboCtrl.instance().robo.tendusar = False
    roboCtrl.instance().robo.tendvelas = int(tratarFloat(values['tendvelas']))
    if values['tendemasma'] == True:
        roboCtrl.instance().robo.tendemasma = True
    else:
        roboCtrl.instance().robo.tendemasma = False
    if values['telegranusar'] == True:
        if int(tratarFloat(values['telegranchatid'])) == 0:
            raise Exception(Idioma.traducao('Chat_ID do telegran inválido.'))
    if values['telegrantoken'] != '':
        if values['telegranusar'] == False or (int(tratarFloat(values['telegranchatid'])) == 0):
            raise Exception(Idioma.traducao('Selecione o Autorizo o envio dos resultados e informe o Chat_ID.'))
        if values['telegranusar'] == True:
            roboCtrl.instance().robo.telegranusar = True
        else:
            roboCtrl.instance().robo.telegranusar = False
        roboCtrl.instance().robo.telegranchatid = int(tratarFloat(values['telegranchatid']))
        roboCtrl.instance().robo.telegrantoken = values['telegrantoken']
        if tratarFloat(values['valinic']) == 0:
            raise Exception(Idioma.traducao('Saldo Inicial não pode ser zero.'))
        if tratarFloat(values['payout']) == 0:
            raise Exception(Idioma.traducao('Payout não pode ser zero.'))
        if roboCtrl.instance().robo.gerenciar == 0:
            if int(tratarFloat(values['qtdgale'])) > 0:
                if tratarFloat(values['gale1']) == 0:
                    raise Exception(Idioma.traducao('Entradas Fixas, o valor do gale {0} não pode ser zero.'.format(1)))
        if roboCtrl.instance().robo.gerenciar == 0:
            if int(tratarFloat(values['qtdgale'])) > 1:
                if tratarFloat(values['gale2']) == 0:
                    raise Exception(Idioma.traducao('Entradas Fixas, o valor do gale {0} não pode ser zero.'.format(2)))
        roboCtrl.instance().robo.valorinicial = tratarFloat(values['valinic'])
        roboCtrl.instance().robo.payoutmin = int(tratarFloat(values['payout']))
        roboCtrl.instance().robo.qtdgales = int(tratarFloat(values['qtdgale']))
        if values['percent'] == Idioma.traducao('Percentual'):
            roboCtrl.instance().robo.ent_tipo = 'P'
        else:
            roboCtrl.instance().robo.ent_tipo = 'V'
        roboCtrl.instance().robo.ent_valor1 = tratarFloat(values['valor1'])
        roboCtrl.instance().robo.ent_gale1 = tratarFloat(values['gale1'])
        roboCtrl.instance().robo.ent_gale2 = tratarFloat(values['gale2'])
        if roboCtrl.instance().robo.gerenciar == 1:
            if tratarFloat(values['percentsoros']) == 0:
                raise Exception('SorosGale, ' + Idioma.traducao('o valor da 1ª Entrada % não pode ser zero.'))
        roboCtrl.instance().robo.percent = tratarFloat(values['percentsoros'])
        if values['modelo'] == Idioma.traducao('Agressivo'):
            roboCtrl.instance().robo.modelo = 'A'
        elif values['modelo'] == Idioma.traducao('Moderado'):
            roboCtrl.instance().robo.modelo = 'M'
        if values['modelo'] == Idioma.traducao('Conservador'):
            roboCtrl.instance().robo.modelo = 'C'
        if values['tipostop'] == Idioma.traducao('Percentual'):
            roboCtrl.instance().robo.tipostop = 'P'
        else:
            roboCtrl.instance().robo.tipostop = 'V'
        if roboCtrl.instance().robo.gerenciar == 2:
            if tratarFloat(values['valorentsoros']) == 0:
                raise Exception('Soros, ' + Idioma.traducao('o valor da 1ª Entrada $ não pode ser zero.'))
        if roboCtrl.instance().robo.gerenciar == 2:
            if tratarFloat(values['valorentsoros']) == 0:
                raise Exception('Soros, ' + Idioma.traducao('o valor do Nível não pode ser zero.'))
        if values['tipovalsoros'] == Idioma.traducao('Percentual'):
            roboCtrl.instance().robo.tipovalsoros = 'P'
        else:
            roboCtrl.instance().robo.tipovalsoros = 'V'
        roboCtrl.instance().robo.valorentsoros = tratarFloat(values['valorentsoros'])
        roboCtrl.instance().robo.nivelsoros = int(tratarFloat(values['nivelsoros']))
        if roboCtrl.instance().robo.gerenciar == 3:
            if tratarFloat(values['cicloval10']) + tratarFloat(values['cicloval11']) + tratarFloat(values['cicloval12']) + tratarFloat(values['cicloval20']) + tratarFloat(values['cicloval21']) + tratarFloat(values['cicloval22']) + tratarFloat(values['cicloval30']) + tratarFloat(values['cicloval31']) + tratarFloat(values['cicloval32']) == 0:
                raise Exception(Idioma.traducao('Ciclos, nenhum valor foi digitado.'))
    if roboCtrl.instance().robo.gerenciar == 3:
        if roboCtrl.instance().robo.qtdgales == 0:
            if not (tratarFloat(values['cicloval10']) == 0 and tratarFloat(values['cicloval11']) > 0):
                if not (tratarFloat(values['cicloval11']) == 0 and tratarFloat(values['cicloval12']) > 0):
                    if not tratarFloat(values['cicloval12']) == 0 or tratarFloat(values['cicloval20']) > 0:
                        raise Exception(Idioma.traducao('Ciclos, valor do ciclo 1 inválido.'))
                    if not (tratarFloat(values['cicloval20']) == 0 and tratarFloat(values['cicloval21']) > 0):
                        if not (tratarFloat(values['cicloval21']) == 0 and tratarFloat(values['cicloval22']) > 0):
                            if not tratarFloat(values['cicloval22']) == 0 or tratarFloat(values['cicloval30']) > 0:
                                raise Exception(Idioma.traducao('Ciclos, valor do ciclo 2 inválido.'))
                            if tratarFloat(values['cicloval30']) == 0 and not tratarFloat(values['cicloval31']) > 0:
                                if not tratarFloat(values['cicloval31']) == 0 or tratarFloat(values['cicloval32']) > 0:
                                    raise Exception(Idioma.traducao('Ciclos, valor do ciclo 3 inválido.'))
                            if roboCtrl.instance().robo.gerenciar == 3:
                                if roboCtrl.instance().robo.qtdgales == 1:
                                    if not (tratarFloat(values['cicloval10']) > 0 and tratarFloat(values['cicloval11']) == 0):
                                        if tratarFloat(values['cicloval10']) == 0 and tratarFloat(values['cicloval11']) > 0 or tratarFloat(values['cicloval12']) > 0:
                                            raise Exception(Idioma.traducao('Ciclos, valor do ciclo 1 inválido.'))
                                        if not (tratarFloat(values['cicloval20']) > 0 and tratarFloat(values['cicloval21']) == 0):
                                            if tratarFloat(values['cicloval20']) == 0 and tratarFloat(values['cicloval21']) > 0 or tratarFloat(values['cicloval22']) > 0:
                                                raise Exception(Idioma.traducao('Ciclos, valor do ciclo 2 inválido.'))
                                            if not (tratarFloat(values['cicloval30']) > 0 and tratarFloat(values['cicloval31']) == 0):
                                                if tratarFloat(values['cicloval30']) == 0 and tratarFloat(values['cicloval31']) > 0 or tratarFloat(values['cicloval32']) > 0:
                                                    raise Exception(Idioma.traducao('Ciclos, valor do ciclo 3 inválido.'))
    if roboCtrl.instance().robo.gerenciar == 3:
        if roboCtrl.instance().robo.qtdgales == 2:
            if tratarFloat(values['cicloval10']) > 0:
                if tratarFloat(values['cicloval11']) == 0 or (tratarFloat(values['cicloval12']) == 0):
                    raise Exception(Idioma.traducao('Ciclos, valor do ciclo 1 inválido.'))
                if tratarFloat(values['cicloval20']) > 0:
                    if tratarFloat(values['cicloval21']) == 0 or (tratarFloat(values['cicloval22']) == 0):
                        raise Exception(Idioma.traducao('Ciclos, valor do ciclo 2 inválido.'))
                    if tratarFloat(values['cicloval30']) > 0:
                        if tratarFloat(values['cicloval31']) == 0 or (tratarFloat(values['cicloval32']) == 0):
                            raise Exception(Idioma.traducao('Ciclos, valor do ciclo 3 inválido.'))
                        roboCtrl.instance().robo.cicloval10 = tratarFloat(values['cicloval10'])
                        roboCtrl.instance().robo.cicloval11 = tratarFloat(values['cicloval11'])
                        roboCtrl.instance().robo.cicloval12 = tratarFloat(values['cicloval12'])
                        roboCtrl.instance().robo.cicloval20 = tratarFloat(values['cicloval20'])
                        roboCtrl.instance().robo.cicloval21 = tratarFloat(values['cicloval21'])
                        roboCtrl.instance().robo.cicloval22 = tratarFloat(values['cicloval22'])
                        roboCtrl.instance().robo.cicloval30 = tratarFloat(values['cicloval30'])
                        roboCtrl.instance().robo.cicloval31 = tratarFloat(values['cicloval31'])
                        roboCtrl.instance().robo.cicloval32 = tratarFloat(values['cicloval32'])
                        if tratarFloat(values['stopgain']) == 0:
                            raise Exception(Idioma.traducao('Valor do Stop Gain não pode ser zero.'))
                        if tratarFloat(values['stoploss']) == 0:
                            raise Exception(Idioma.traducao('Valor do Stop Loss não pode ser zero.'))
                        if tratarFloat(values['stoploss']) > 100:
                            if roboCtrl.instance().robo.tipostop == 'P':
                                raise Exception(Idioma.traducao('Valor do Stop Loss não pode ser maior do que 100%.'))
                    if tratarFloat(values['stoploss']) > tratarFloat(values['valinic']):
                        if roboCtrl.instance().robo.tipostop == 'V':
                            raise Exception(Idioma.traducao('Valor do Stop Loss não pode ser maior do que o Saldo Inicial.'))
                roboCtrl.instance().robo.stopgain = tratarFloat(values['stopgain'])
                roboCtrl.instance().robo.stoploss = tratarFloat(values['stoploss'])
                roboCtrl.instance().robo.horariosOpera = []
                for itemhr in roboCtrl.instance().robo.listahoraoperacao:
                    ho = HorarioOpera()
                    ho.importTxt(itemhr)
                    roboCtrl.instance().robo.horariosOpera.append(ho)

            roboCtrl.instance().robo.saveConfig()
            cf = roboCtrl.instance().robo.loadConfig()
            roboCtrl.instance().robo.setConfig(cf)
            if touros2_alterado:
                getNoticias()
        return True


def GravaConfigTP(email, contatipo):
    contareal = False
    if contatipo == Idioma.traducao('Real'):
        contareal = True
    roboCtrl.instance().robo.saveConfigTP(email, contareal)
    cf = roboCtrl.instance().robo.loadConfig()
    roboCtrl.instance().robo.setConfig(cf)


def validarEditsNumeros(editname: str, values):
    try:
        if len(values[editname]):
            if values[editname][(-1)] not in '0123456789.':
                roboCtrl.instance().view.janela[editname].update(values[editname][:-1])
    except:
        pass


def AddHorarioOperacaoMT(values):
    try:
        if type(values['hrinicmt']) == str:
            values['hrinicmt'] = 0
        if type(values['mininicmt']) == str:
            values['mininicmt'] = 0
        if type(values['hrtermmt']) == str:
            values['hrtermmt'] = 0
        if type(values['mintermmt']) == str:
            values['mintermmt'] = 0
        horario = '{:02d}'.format(values['hrinicmt']) + ':' + '{:02d}'.format(values['mininicmt']) + ':00'
        try:
            validtime1 = datetime.strptime(horario, '%H:%M:%S')
        except:
            return (
             False, Idioma.traducao('Horário de início inválido'))
        else:
            horario = '{:02d}'.format(values['hrtermmt']) + ':' + '{:02d}'.format(values['mintermmt']) + ':00'
            try:
                validtime2 = datetime.strptime(horario, '%H:%M:%S')
            except:
                return (
                 False, Idioma.traducao('Horário de término inválido'))
            else:
                ret, msg = AddHorarioOperacao(validtime1, validtime2)

        return (
         ret, msg)
    except Exception as e:
        try:
            return (
             False, str(e))
        finally:
            e = None
            del e


def AddHorarioOperacao(validtime1: datetime, validtime2: datetime):
    try:
        if validtime1 >= validtime2:
            return (False, Idioma.traducao('Horário de início inválido. Não pode ser superior/igual ao Horário de Término.'))
        try:
            item = validtime1.strftime('%H:%M') + '  -  ' + validtime2.strftime('%H:%M')
            roboCtrl.instance().robo.listahoraoperacao.index(item)
        except:
            roboCtrl.instance().robo.listahoraoperacao.append(item)
            roboCtrl.instance().view.janela['-LISTAHORAOPERA-'].update(values=(roboCtrl.instance().robo.listahoraoperacao))
            roboCtrl.instance().view.janela.refresh()

        return (True, '')
    except Exception as e:
        try:
            return (
             False, str(e))
        finally:
            e = None
            del e


def DelHorarioOperacaoMT(values):
    if values['-LISTAHORAOPERA-']:
        cancelitem = sg.popup_yes_no((Idioma.traducao('Excluir o horário selecionado ?')), no_titlebar=True,
          keep_on_top=True,
          text_color='black',
          background_color='#DFDDDD')
        if cancelitem == 'Yes':
            try:
                item = values['-LISTAHORAOPERA-'][0]
                roboCtrl.instance().robo.listahoraoperacao.remove(item)
                roboCtrl.instance().view.janela['-LISTAHORAOPERA-'].update(values=(roboCtrl.instance().robo.listahoraoperacao))
                roboCtrl.instance().view.janela.refresh()
            except Exception as e:
                try:
                    pass
                finally:
                    e = None
                    del e


def Habilitar(iniciado: bool):
    roboCtrl.instance().view.janela['-Iniciar-'].update(disabled=iniciado)
    roboCtrl.instance().view.janela['-Parar-'].update(disabled=(not iniciado))
    roboCtrl.instance().view.janela['-Gravar-'].update(disabled=iniciado)
    roboCtrl.instance().view.janela['-Download-'].update(disabled=iniciado)
    roboCtrl.instance().view.janela['-abrirlista-'].update(disabled=iniciado)
    roboCtrl.instance().view.janela['email'].update(disabled=iniciado)
    roboCtrl.instance().view.janela['senha'].update(disabled=iniciado)
    roboCtrl.instance().view.janela['contatipo'].update(disabled=iniciado)
    roboCtrl.instance().view.janela['senha'].update(disabled=iniciado)
    roboCtrl.instance().view.janela['contatipo'].update(disabled=iniciado)
    roboCtrl.instance().view.janela['-AddHrOper-'].update(disabled=iniciado)
    roboCtrl.instance().view.janela['-DelHrOper-'].update(disabled=iniciado)