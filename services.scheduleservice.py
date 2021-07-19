import time
from datetime import datetime, timedelta
import models.OperationProgrammed as OpProgramAdd
from models.HorarioOperacao import HorarioOpera
import models.roboController as roboCtrl
from connection.RetryConnection import *
import services.preorder as F
import services.buyservice as G
import services.sendmsg as HL
from main.roboUtils import Idioma, LogSys

def searchList(pValue, mylist):
    return pValue in mylist


def C(operations):
    FT = '%H:%M:%S'
    FD = '%d/%m/%y %H:%M:%S'
    lista = []
    roboCtrl.instance().operContrl.agenda = OpProgramAdd.G(operations, roboCtrl.instance().robo.delay)
    roboCtrl.instance().robo.schedMy.clear()
    roboCtrl.instance().robo.schedMyList = []
    for sinal in roboCtrl.instance().operContrl.agenda:
        if sinal.programmedHour >= datetime.now():
            dhexpira = sinal.expirationDate - timedelta(seconds=35)
            job = roboCtrl.instance().robo.schedMy.every().days.at(sinal.programmedHour.strftime(FT)).do(G().dooperation, sinal).tag('agendaID' + str(sinal.op_id))
            roboCtrl.instance().robo.schedMyList.append(job)
            LogSys.save('ID {}: {} | {} | {} | {}M', sinal.op_id, sinal.programmedHour.strftime(FD), sinal.pair, sinal.direction.upper(), sinal.expirationMode)
            job = roboCtrl.instance().robo.schedMy.every().days.at(sinal.pre_order.strftime(FT)).do(F.D, roboCtrl.instance().robo.manterConta, roboCtrl.instance().robo.tendusar, roboCtrl.instance().robo.tendvelas, roboCtrl.instance().robo.tendemasma, roboCtrl.instance().robo.priorid, sinal).tag('agendaPreID' + str(sinal.op_id))
            roboCtrl.instance().robo.schedMyList.append(job)
            try:
                lista.index(sinal.programmedHour.strftime(FT))
            except:
                lista.append(sinal.programmedHour.strftime(FT))
                job = roboCtrl.instance().robo.schedMy.every().days.at(dhexpira.strftime(FT)).do(VerifConnection).tag('agendaCnxID' + str(sinal.op_id))
                roboCtrl.instance().robo.schedMyList.append(job)

        else:
            sinal.situacao = Idioma.traducao('Cancelado')
            roboCtrl.instance().operContrl.agenda[(int(sinal.op_id) - 1)].situacao = sinal.situacao


def P(operations):
    FT = '%H:%M:%S'
    FD = '%d/%m/%y %H:%M:%S'
    ultimo_sinal = None
    lista = []
    for sinal in roboCtrl.instance().operContrl.agenda:
        pksinal = sinal.hourOrig.strftime(FT)
        if not roboCtrl.instance().robo.usarsoros:
            if roboCtrl.instance().robo.entfixamt4:
                pksinal = str(sinal.hourOrig.strftime(FT)) + str(sinal.pair)
        lista.append(pksinal)
        if sinal.situacao != Idioma.traducao('Cancelado'):
            if sinal.situacao != Idioma.traducao('Fechado'):
                if 'Win' not in sinal.situacao:
                    if 'Payout' not in sinal.situacao:
                        if 'Contra' not in sinal.situacao:
                            if 'Expiração' not in sinal.situacao:
                                if 'Notícia' not in sinal.situacao:
                                    ultimo_sinal = sinal

    newID = len(lista)
    delaymin = 5
    if roboCtrl.instance().robo.delay > 0:
        delaymin = roboCtrl.instance().robo.delay
    agenda = OpProgramAdd.G(operations, roboCtrl.instance().robo.delay)
    for sinal in agenda:
        dhagora = datetime.now().replace(microsecond=0)
        dhantes = sinal.hourOrig - timedelta(seconds=40)
        dhentradamax = sinal.hourOrig + timedelta(seconds=(roboCtrl.instance().robo.maxdelaymt4))
        if sinal.hourOrig - timedelta(seconds=delaymin) <= dhagora and sinal.expirationDate > dhagora:
            if verificarHorarioOperacao(datetime.now()):
                pksinal = sinal.hourOrig.strftime(FT)
                if not roboCtrl.instance().robo.usarsoros:
                    if roboCtrl.instance().robo.entfixamt4:
                        pksinal = str(sinal.hourOrig.strftime(FT)) + str(sinal.pair)
                if not searchList(pksinal, lista):
                    newID += 1
                    sinal.op_id = str(newID)
                    lista.append(pksinal)
                    if dhentradamax >= dhagora or roboCtrl.instance().robo.maxdelaymt4 == 0:
                        if verificarSobreposto(sinal, ultimo_sinal):
                            roboCtrl.instance().operContrl.agenda.append(sinal)
                            LogSys.save('ID {}: {} | {} | {} | {}M', sinal.op_id, sinal.programmedHour.strftime(FD), sinal.pair, sinal.direction.upper(), sinal.expirationMode)
                            F.D(roboCtrl.instance().robo.manterConta, False, False, False, roboCtrl.instance().robo.priorid, sinal)
                            G().dooperation(sinal)
                        else:
                            sinal.situacao = Idioma.traducao('Cancelado')
                            roboCtrl.instance().operContrl.agenda.append(sinal)
                            LogSys.save('ID {}: {} | {} | {} | {}M | {}', sinal.op_id, sinal.programmedHour.strftime(FD), sinal.pair, sinal.direction.upper(), sinal.expirationMode, Idioma.traducao('Cancelado'))
                    else:
                        sinal.situacao = Idioma.traducao('Cancelado')
                        roboCtrl.instance().operContrl.agenda.append(sinal)
                        LogSys.save('ID {}: {} Max {} | {} | {} | {}M | {}', sinal.op_id, sinal.hourOrig, dhentradamax, sinal.pair, sinal.direction.upper(), sinal.expirationMode, Idioma.traducao('Expirou tempo de entrada'))
                else:
                    LogSys.save('Duplicidade de sinal no mesmo horário')
            else:
                sinal.situacao = Idioma.traducao('Cancelado')
                LogSys.save('ID {}: {} Max {} | {} | {} | {}M | {}', sinal.op_id, sinal.hourOrig.strftime(FD), dhentradamax.strftime(FD), sinal.pair, sinal.direction.upper(), sinal.expirationMode, Idioma.traducao('Fora do horário de operação'))
        else:
            if verificarHorarioOperacao(sinal.programmedHour) and sinal.programmedHour >= dhagora:
                pksinal = sinal.hourOrig.strftime(FT)
                if not roboCtrl.instance().robo.usarsoros:
                    if roboCtrl.instance().robo.entfixamt4:
                        pksinal = str(sinal.hourOrig.strftime(FT)) + str(sinal.pair)
                if not searchList(pksinal, lista):
                    if dhagora <= dhantes:
                        newID += 1
                        sinal.op_id = str(newID)
                        lista.append(pksinal)
                        if verificarSobreposto(sinal, ultimo_sinal):
                            dhexpira = sinal.expirationDate - timedelta(seconds=35)
                            if roboCtrl.instance().robo.origemsinal == 2:
                                sinal.programmedHour = sinal.programmedHour - timedelta(seconds=2)
                            job = roboCtrl.instance().robo.schedMy.every().days.at(sinal.programmedHour.strftime(FT)).do(G().dooperation, sinal).tag('agendaID' + str(sinal.op_id))
                            roboCtrl.instance().robo.schedMyList.append(job)
                            roboCtrl.instance().operContrl.agenda.append(sinal)
                            LogSys.save('ID {}: {} | {} | {} | {}M', sinal.op_id, sinal.programmedHour.strftime(FD), sinal.pair, sinal.direction.upper(), sinal.expirationMode)
                            job = roboCtrl.instance().robo.schedMy.every().days.at(sinal.pre_order.strftime(FT)).do(F.D, roboCtrl.instance().robo.manterConta, roboCtrl.instance().robo.tendusar, roboCtrl.instance().robo.tendvelas, roboCtrl.instance().robo.tendemasma, roboCtrl.instance().robo.priorid, sinal).tag('agendaPreID' + str(sinal.op_id))
                            roboCtrl.instance().robo.schedMyList.append(job)
                            job = roboCtrl.instance().robo.schedMy.every().days.at(dhexpira.strftime(FT)).do(VerifConnection).tag('agendaCnxID' + str(sinal.op_id))
                            roboCtrl.instance().robo.schedMyList.append(job)
                        else:
                            sinal.situacao = Idioma.traducao('Cancelado')
                            roboCtrl.instance().operContrl.agenda.append(sinal)
                            LogSys.save('ID {}: {} | {} | {} | {}M | {}', sinal.op_id, sinal.programmedHour.strftime(FD), sinal.pair, sinal.direction.upper(), sinal.expirationMode, Idioma.traducao('Cancelado'))
                    else:
                        LogSys.save('ID {}: {} Min p/Agenda {} | {} | {} | {}M | {}', sinal.op_id, sinal.hourOrig.strftime(FD), dhantes.strftime(FD), sinal.pair, sinal.direction.upper(), sinal.expirationMode, Idioma.traducao('Expirou tempo de entrada'))
                else:
                    LogSys.save('Duplicidade de sinal no mesmo horário')
            else:
                LogSys.save('ID {}: {} Max {} | {} | {} | {}M | {}', sinal.op_id, sinal.hourOrig.strftime(FD), dhentradamax.strftime(FD), sinal.pair, sinal.direction.upper(), sinal.expirationMode, Idioma.traducao('Fora do horário de operação'))

    roboCtrl.instance().robo.AtualizaGridAgenda()


def verificarSobreposto(operation, ultsinal):
    ret = True
    if roboCtrl.instance().robo.usarsoros:
        if ultsinal != None:
            dhInic = ultsinal.hourOrig
            if roboCtrl.instance().robo.qtdgales < 1:
                dhTerm = ultsinal.expirationDate + timedelta(seconds=15)
            elif roboCtrl.instance().robo.qtdgales < 2:
                dhTerm = ultsinal.expirationGale1 + timedelta(seconds=15)
            else:
                dhTerm = ultsinal.expirationGale2 + timedelta(seconds=15)
            if operation.programmedHour >= dhInic:
                if operation.programmedHour <= dhTerm:
                    if ultsinal.op_id != operation.op_id:
                        ret = False
    return ret


def verificarHorarioOperacao(dthrsinal):
    ret = True
    if len(roboCtrl.instance().robo.horariosOpera) > 0:
        ret = False
        for hora in roboCtrl.instance().robo.horariosOpera:
            if dthrsinal >= hora.getDateTimeInicio():
                if dthrsinal <= hora.getDateTimeTermino():
                    ret = True
                    break

    return ret


def cancel(id):
    try:
        for sinal in roboCtrl.instance().operContrl.agenda:
            if not sinal.situacao == Idioma.traducao('Aguardando'):
                if sinal.situacao == Idioma.traducao('Agendado'):
                    pass
            cancelId(sinal.op_id, False)

        HL.atualizaView()
        return True
    except Exception as e:
        try:
            LogSys.save(str(e))
            return False
        finally:
            e = None
            del e


def cancelId(id, atualTela: bool):
    try:
        roboCtrl.instance().robo.schedMy.clear('agendaPreID' + str(id))
    except:
        pass

    try:
        roboCtrl.instance().robo.schedMy.clear('agendaCnxID' + str(id))
    except:
        pass

    try:
        roboCtrl.instance().robo.schedMy.clear('agendaID' + str(id))
        sitAceitas = [Idioma.traducao('Aguardando'), Idioma.traducao('Agendado')]
        roboCtrl.instance().operContrl.cancelAgendaId(id, Idioma.traducao('Cancelado'), sitAceitas)
        if atualTela:
            HL.atualizaView()
        return True
    except Exception as e:
        try:
            LogSys.save(str(e))
            return False
        finally:
            e = None
            del e