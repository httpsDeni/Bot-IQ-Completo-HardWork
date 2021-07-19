import time, timeit
from datetime import datetime, date, timedelta
import connection.APIConnection as A
from connection.RetryConnection import *
import models.Balance as C
from services.ativosopen import AtivosAbertos
from services.tendencia import *
from services.tendenciaTablib import *
from main.roboUtils import *

def buscaPayout(ativo, duracao, priorid):
    duracao = int(duracao)
    tenta = 0
    data = '0'
    payoutDig = 0
    payoutBin = 0
    if priorid != 4:
        try:
            data = A.instance().connection.get_digital_payout(ativo)
        except:
            try:
                A.instance().connection.subscribe_strike_list(ativo, duracao)
                while 1:
                    data = A.instance().connection.get_digital_current_profit(ativo, duracao)
                    if data:
                        break
                    else:
                        time.sleep(1)
                        tenta += 1
                    if tenta >= 10:
                        break

                A.instance().connection.unsubscribe_strike_list(ativo, duracao)
            except Exception as e:
                try:
                    LogSys.save('Erro Busca Payout Digital: {} = {}'.format(str(e), data))
                finally:
                    e = None
                    del e

        try:
            payoutDig = int(data)
        except:
            payoutDig = 0

    if priorid != 3:
        try:
            data = A.instance().connection.get_all_profit()
            try:
                payout_tur = int(data[ativo]['turbo'] * 100)
            except:
                payout_tur = 0

            try:
                payout_bin = int(data[ativo]['binary'] * 100)
            except:
                payout_bin = 0

            if duracao >= 15:
                if payout_bin > 0:
                    payoutBin = payout_bin
                else:
                    payoutBin = payout_tur
            elif payout_tur > 0:
                payoutBin = payout_tur
            else:
                payoutBin = payout_bin
        except Exception as e:
            try:
                LogSys.save('Erro Busca Payout Binaria: {} = {}'.format(str(e), data))
            finally:
                e = None
                del e

        return (
         payoutDig, payoutBin)


def ativoAberto(ativo, prioriDigital):
    aberto = False
    tipo = 'D'
    if prioriDigital == 3:
        tipos = [
         'digital']
    elif prioriDigital == 4:
        tipos = [
         'turbo', 'binary']
    elif prioriDigital:
        tipos = [
         'digital', 'turbo', 'binary']
    else:
        tipos = [
         'turbo', 'binary', 'digital']
    par = roboCtrl.instance().robo.ativosabertos
    if par == []:
        par = A.instance().connection.get_all_open_time()
        roboCtrl.instance().robo.ativosabertos = par
    for tpnome in tipos:
        if not aberto:
            for paridade in par[tpnome]:
                if paridade == ativo:
                    if par[tpnome][paridade]['open'] == True:
                        aberto = True
                        break

        if aberto:
            if tpnome == 'digital':
                tipo = 'D'
            else:
                tipo = 'B'
            break

    return (
     tipo, aberto)


def D(change_acc, viewTrend, qtdCandleTrend, trendEmaSma, priorid, operation):
    E = '0'
    if int(date.today().day) == int(operation.day):
        if VerifConnection():
            if change_acc:
                A.instance().connection.change_balance(A.instance().acc_type)
            if operation.expirationMode > 15:
                if priorid == 3:
                    priorid = 4
            Pdig, Pbin = buscaPayout(operation.pair, operation.expirationMode, priorid)
            if int(Pdig + Pbin) > 0:
                LogSys.save('{} | {}M | Payout Digital: {} | Binary: {}', operation.pair, operation.expirationMode, Pdig, Pbin)
            prioriDigital = 1
            if operation.expirationMode > 15:
                prioriDigital = 0
            elif int(Pbin) > int(Pdig) and priorid == 0:
                prioriDigital = 0
            elif priorid == 1:
                prioriDigital = 1
            elif priorid == 2:
                prioriDigital = 0
            if priorid == 3:
                prioriDigital = 3
                TipoAtivo = 'Digital'
                Tp = 'D'
            if priorid == 4:
                prioriDigital = 4
                TipoAtivo = 'Binarias'
                Tp = 'B'
            if prioriDigital == 1 or prioriDigital == 3:
                operation.payout = Pdig
            else:
                operation.payout = Pbin
            if priorid < 3:
                TipoAtivo = 'Digital'
                AtAberto = Idioma.traducao('Fechado')
                Tp, Ab = ativoAberto(operation.pair, prioriDigital)
                if Ab:
                    operation.typepair = Tp
                    AtAberto = Idioma.traducao('Aberto')
                if Tp == 'B':
                    TipoAtivo = 'Binarias'
                if prioriDigital == 1:
                    if Tp == 'B':
                        operation.payout = Pbin
                elif prioriDigital == 0:
                    if Tp == 'D':
                        operation.payout = Pdig
                LogSys.save('{} | {} | {}', operation.pair, TipoAtivo, AtAberto)
            else:
                Ab = True
                operation.typepair = Tp
            if not Ab or viewTrend:
                try:
                    if trendEmaSma:
                        qvelas = 100
                        velas = getVelas(operation.pair, operation.expirationMode, qvelas)
                        operation.trend, sq = Ema5Ema20(velas)
                        if operation.trend != '':
                            LogSys.save('{} | Tendência: {} | {}', operation.pair, operation.trend, sq)
                    else:
                        operation.trend, sq, perccall, percput = tendenciaCandles(operation.pair, operation.expirationMode, qtdCandleTrend)
                        if operation.trend != '':
                            LogSys.save('{} | Tendência: {} | {} | call: %{} put: %{}', operation.pair, operation.trend, sq, perccall, percput)
                        else:
                            LogSys.save('{} | Qtd: {} velas: {} | call: %{} put: %{}', operation.pair, qtdCandleTrend, sq, perccall, percput)
                except:
                    LogSys.show('{} | {}M | Erro na busca dos candles para a tendência.', operation.pair, operation.expirationMode)

        else:
            LogSys.send('{} | {}M | {}', operation.pair, operation.expirationMode, Idioma.traducao('Problema na conexão, verifique sua internet.'))