import models.roboController as roboCtrl
from models.ThreadOperacion import *
import services.scheduleservice as Agenda
from main.roboUtils import *

def externalFunction():
    if roboCtrl.instance().robo.origemsinal == 1 and roboCtrl.instance().robo.prime:
        roboCtrl.instance().robo.IniciarAgendamentosSocket()
    elif roboCtrl.instance().robo.origemsinal == 2:
        roboCtrl.instance().robo.IniciarAgendamentosServer()
    else:
        roboCtrl.instance().robo.IniciarAgendamentos()


def cancelSinal(item):
    i = 0
    for sinal in roboCtrl.instance().operContrl.agenda:
        if i == item:
            Agenda.cancelId(sinal.op_id, True)
            msg = 'ID:{0} {1} {2} Cancelado Sobreposto'.format(sinal.op_id, sinal.pair, sinal.programmedHour.strftime('%H:%M:%S'))
            LogSys(msg, True)
            break
        else:
            i += 1


def btn_Iniciar(event):
    ZeraPlacarTotal()
    threadedApp = ThreadOper(target=externalFunction)
    roboCtrl.instance().add_listThread = threadedApp
    appStarted = True
    if roboCtrl.instance().robo.Conectar(roboCtrl.instance().robo.afiliadocfg):
        Habilitar(True)
        if not threadedApp.is_alive():
            threadedApp.start()
        return True
    return False


def btn_Parar(event):
    if Agenda.cancel(0):
        appStarted = False
        roboCtrl.instance().robo.PararTudo()
        for th in roboCtrl.instance().add_listThread:
            if th.isAlive():
                th.stop()

        if event == '-Parar-':
            LogSys.send(Idioma.traducao('Agendamentos cancelados com sucesso!'))
            Habilitar(False)