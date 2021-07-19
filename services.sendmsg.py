import requests
import models.roboController as roboCtrl
from main.roboUtils import *

def atualizaView():
    try:
        roboCtrl.instance().operContrl.wins = 0
        roboCtrl.instance().operContrl.hits = 0
        data = []
        for sinal in roboCtrl.instance().operContrl.agenda:
            item = [
             '{:03d}'.format(int(sinal.op_id)),
             sinal.programmedHour.strftime('%d/%m/%y'),
             sinal.programmedHour.strftime('%H:%M:%S'),
             sinal.pair,
             sinal.direction.upper(),
             sinal.expirationMode,
             sinal.situacao,
             '{:18.2f}'.format(float(sinal.lucro))]
            data.append(item)
            if float(sinal.lucro) > 0:
                roboCtrl.instance().operContrl.wins += 1
            else:
                if float(sinal.lucro) < 0:
                    roboCtrl.instance().operContrl.hits += 1
                elif 'win' in str(sinal.situacao).lower():
                    roboCtrl.instance().operContrl.wins += 1
            if 'loss' in str(sinal.situacao).lower():
                roboCtrl.instance().operContrl.hits += 1

        try:
            roboCtrl.instance().view.janela['-TABLE-'].update(values=data)
            roboCtrl.instance().view.janela.Refresh()
        except Exception as e:
            try:
                pass
            finally:
                e = None
                del e

        roboCtrl.instance().view.janela['placarW'].update(value=(roboCtrl.instance().operContrl.wins))
        roboCtrl.instance().view.janela['placarH'].update(value=(roboCtrl.instance().operContrl.hits))
        roboCtrl.instance().view.janela['assertividade'].update(value=(roboCtrl.instance().operContrl.getAssertividade()))
        roboCtrl.instance().view.janela['saldolucro'].update(value=(round(roboCtrl.instance().operContrl.saldo, 2)))
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e