import json, time
from datetime import date
import models.Balance as BL
import models.roboController as roboCtrl
from models.ThreadOperacion import *
import connection.APIConnection as ApiCon
import services.buycontroller as E
import services.scheduleservice as Agenda
import services.preorder as Pre
import services.sendmsg as HL
import services.telegran as TL
from services.noticias import *
from iqoptionapi.expiration import *
from main.roboUtils import *
import emoji
S = None
R = ','
Q = '.'
P = float
H = True
K = ''
C = int
G = False
F = str
MsgQueda = 'ID:{} ' + Idioma.traducao('Queda de Internet durante a Operacao')

class O:
    SECOND_RESULT = 2
    VELAPEQUENA = 9

    def enviarMsgTelegran(self, msg, titulo):
        if int(roboCtrl.instance().operContrl.wins) + int(roboCtrl.instance().operContrl.hits) > 0:
            msgTotal = ('{} ' + Idioma.traducao('Parcial:') + '\n{} WIN: {} {} LOSS: {} ( {}% )\n{} <b>' + Idioma.traducao('Lucro atual: $') + '{}</b>').format(emoji.emojize(':checkered_flag:', use_aliases=True), emoji.emojize(':white_check_mark:', use_aliases=True), roboCtrl.instance().operContrl.wins, emoji.emojize(':no_entry:', use_aliases=True), roboCtrl.instance().operContrl.hits, roboCtrl.instance().operContrl.getAssertividade(), emoji.emojize(':moneybag:', use_aliases=True), round(roboCtrl.instance().operContrl.saldo, 2))
            TL.enviarMsg(roboCtrl.instance().robo.telegranchatid, titulo + '\n' + msg + '\n' + msgTotal)

    def enviarMsgTL(self, msg, titulo):
        if roboCtrl.instance().robo.iniciado:
            T5 = ThreadOper(target=(self.enviarMsgTelegran), args=(msg, titulo))
            roboCtrl.instance().add_listThread = T5
            T5.start()

    def atualView(self):
        time.sleep(2)
        HL.atualizaView()

    def atualizarTela(self):
        T1 = ThreadOper(target=(self.atualView))
        roboCtrl.instance().add_listThread = T1
        T1.start()

    def dooperation(self, operation):
        T2 = ThreadOper(target=(self.start_operation), args=(operation,))
        roboCtrl.instance().add_listThread = T2
        T2.start()

    def docancelProxSinal(self, operation, gale=0):
        T3 = ThreadOper(target=(self.cancelProxSinal), args=(operation, gale))
        roboCtrl.instance().add_listThread = T3
        T3.start()

    def doresultIQ(self, operation, id, gale, chktaxa, wintaxa):
        T4 = ThreadOper(target=(self.resultIQ), args=(operation, id, gale, chktaxa, wintaxa))
        roboCtrl.instance().add_listThread = T4
        T4.start()

    def tamanhoVela(self, vopen, vclose):
        pequena = False
        try:
            vopent = str(vopen).split('.')[0]
            vopenv = str(vopen).split('.')[1]
            vclosev = str(vclose).split('.')[1]
            if int(vopent) > 99:
                vclosev = '{:<04d}'.format(int(vclosev[:4]))
                vopenv = '{:<04d}'.format(int(vopenv[:4]))
            else:
                vclosev = '{:<06d}'.format(int(vclosev))
                vopenv = '{:<06d}'.format(int(vopenv))
            vopenv = int(vopenv)
            vclosev = int(vclosev)
            vdifer = abs(vopenv - vclosev)
            if vdifer < self.VELAPEQUENA:
                pequena = True
        except:
            pequena = False

        return pequena

    def esperarResultTaxa(self, gale: int):
        vResultTaxa = not roboCtrl.instance().robo.esperarIQ
        if roboCtrl.instance().robo.gerenciar > 0:
            if not roboCtrl.instance().robo.esperarIQ:
                if roboCtrl.instance().robo.qtdgales == gale:
                    vResultTaxa = False
            return vResultTaxa

    def mostrar_saldo(self):
        LogSys.save('Stop Gain: {} | Stop Loss: {} | ' + Idioma.traducao('Lucro atual: $') + '{}', round(BL.instance().win_limit, 2), round(BL.instance().stop_limit, 2), round(BL.instance().actual_balance, 2))
        print((Idioma.traducao('Lucro atual: $') + '{}').format(round(BL.instance().actual_balance, 2)))

    def stop_operation(self, operation, valorProxEntrada: float):
        if self.finish_operation(operation, valorProxEntrada):
            if Agenda.cancel(0):
                roboCtrl.instance().robo.PararTudo()
            return True
        return False

    def finish_operation(self, operation, valorProxEntrada: float):
        B = operation
        tituloTL = emoji.emojize(':bangbang:', use_aliases=True) + ' <b>' + Idioma.traducao('Alerta:') + '</b>'
        if round(BL.instance().actual_balance2, 2) <= round(BL.instance().stop_limit, 2):
            LogSys.show('ID:{} [STOP LOSS] ' + Idioma.traducao('Lucro atual: $') + '{}', B.op_id, round(BL.instance().actual_balance2, 2))
            msgTL = ('{}{} {} <b>STOP LOSS</b>\n{}' + Idioma.traducao('Lucro atual: $') + '{}').format(emoji.emojize(':id:', use_aliases=True), B.op_id, emoji.emojize(':x:', use_aliases=True), emoji.emojize(':moneybag:', use_aliases=True), round(BL.instance().actual_balance, 2))
            self.enviarMsgTL(msgTL, tituloTL)
            return True
        if round(BL.instance().actual_balance2, 2) - round(valorProxEntrada, 2) <= round(BL.instance().stop_limit, 2):
            if round(BL.instance().actual_balance2, 2) != 0:
                if roboCtrl.instance().robo.prestop:
                    LogSys.show('ID:{} [PRE-STOP LOSS] ' + Idioma.traducao('Entrada: $') + '{} ' + Idioma.traducao('Lucro previsto: $') + '{}', B.op_id, valorProxEntrada, round(BL.instance().actual_balance2 - valorProxEntrada, 2))
                    msgTL = ('{}{} {} <b>PRE-STOP LOSS</b>\n{}' + Idioma.traducao('Entrada: $') + '{} ' + Idioma.traducao('Lucro previsto: $') + '{}').format(emoji.emojize(':id:', use_aliases=True), B.op_id, emoji.emojize(':warning:', use_aliases=True), emoji.emojize(':moneybag:', use_aliases=True), valorProxEntrada, round(BL.instance().actual_balance2 - valorProxEntrada, 2))
                    self.enviarMsgTL(msgTL, tituloTL)
                    return True
        if round(BL.instance().actual_balance, 2) <= round(BL.instance().stop_limit, 2):
            LogSys.show('ID:{} [STOP LOSS] ' + Idioma.traducao('Lucro atual: $') + '{}', B.op_id, round(BL.instance().actual_balance, 2))
            msgTL = ('{}{} {} <b>STOP LOSS</b>\n{}' + Idioma.traducao('Lucro atual: $') + '{}').format(emoji.emojize(':id:', use_aliases=True), B.op_id, emoji.emojize(':x:', use_aliases=True), emoji.emojize(':moneybag:', use_aliases=True), round(BL.instance().actual_balance, 2))
            self.enviarMsgTL(msgTL, tituloTL)
            return True
        if round(BL.instance().actual_balance, 2) - round(valorProxEntrada, 2) <= round(BL.instance().stop_limit, 2):
            if round(BL.instance().actual_balance, 2) != 0:
                if roboCtrl.instance().robo.prestop:
                    LogSys.show('ID:{} [PRE-STOP LOSS] ' + Idioma.traducao('Entrada: $') + '{} ' + Idioma.traducao('Lucro previsto: $') + '{}', B.op_id, valorProxEntrada, round(BL.instance().actual_balance - valorProxEntrada, 2))
                    msgTL = ('{}{} {} <b>PRE-STOP LOSS</b>\n{}' + Idioma.traducao('Entrada: $') + '{} ' + Idioma.traducao('Lucro previsto: $') + '{}').format(emoji.emojize(':id:', use_aliases=True), B.op_id, emoji.emojize(':warning:', use_aliases=True), emoji.emojize(':moneybag:', use_aliases=True), valorProxEntrada, round(BL.instance().actual_balance2 - valorProxEntrada, 2))
                    self.enviarMsgTL(msgTL, tituloTL)
                    return True
        if round(BL.instance().actual_balance, 2) >= round(BL.instance().win_limit, 2):
            LogSys.show('ID:{} [STOP GAIN] ' + Idioma.traducao('Lucro atual: $') + '{}', B.op_id, round(BL.instance().actual_balance, 2))
            msgTL = ('{}{} {} <b>STOP GAIN</b>\n{}' + Idioma.traducao('Lucro atual: $') + '{}\n{}').format(emoji.emojize(':id:', use_aliases=True), B.op_id, emoji.emojize(':white_check_mark:', use_aliases=True), emoji.emojize(':moneybag:', use_aliases=True), round(BL.instance().actual_balance, 2), emoji.emojize(':rocket:', use_aliases=True) + emoji.emojize(':rocket:', use_aliases=True) + ' ' + Idioma.traducao('Parabéns') + ' ' + emoji.emojize(':rocket:', use_aliases=True) + emoji.emojize(':rocket:', use_aliases=True))
            self.enviarMsgTL(msgTL, tituloTL)
            if roboCtrl.instance().robo.percwinpos > 0:
                if not roboCtrl.instance().robo.ultrapassoustopwin:
                    self.atualizaNovosValoresPosStopWin()
                    return False
                return True
        else:
            return False

    def start_operation(self, operation):
        H = '0'
        B = operation
        dhmax = B.programmedHour + timedelta(seconds=20)
        if C(date.today().day) == C(B.day) and datetime.now() >= B.programmedHour and datetime.now() <= dhmax or roboCtrl.instance().robo.origemsinal > 0:
            if int(B.payout) < int(roboCtrl.instance().robo.payoutmin):
                if int(B.payout) > 0:
                    if int(B.payout) == 0:
                        LogSys.show('ID:{} ' + Idioma.traducao('Expiração Indisponível') + ' ' + Idioma.traducao('Payout inferior:') + ' {} ' + Idioma.traducao('atual:') + ' {}', B.op_id, int(roboCtrl.instance().robo.payoutmin), int(B.payout))
                        roboCtrl.instance().operContrl.calculoTotal(B.op_id, Idioma.traducao('Expiração Indisponível'))
                    else:
                        LogSys.show('ID:{} ' + Idioma.traducao('Payout inferior:') + ' {} ' + Idioma.traducao('atual:') + ' {}', B.op_id, int(roboCtrl.instance().robo.payoutmin), int(B.payout))
                        roboCtrl.instance().operContrl.calculoTotal(B.op_id, 'Payout {}'.format(int(B.payout)))
                    self.atualizarTela()
                    return
            if BL.instance().moeda == 'BRL':
                if float(B.money) < 2:
                    LogSys.show('ID:{} ' + Idioma.traducao('Entrada: $') + '{} ' + Idioma.traducao('inválido para a moeda') + ' [{}] ' + Idioma.traducao('mínimo de $') + '2.00', B.op_id, float(B.money), BL.instance().moeda)
                    return
            if BL.instance().moeda == 'USD':
                if float(B.money) < 1:
                    LogSys.show('ID:{} ' + Idioma.traducao('Entrada: $') + '{} ' + Idioma.traducao('inválido para a moeda') + ' [{}] ' + Idioma.traducao('mínimo de $') + '1.00', B.op_id, float(B.money), BL.instance().moeda)
                    return
            if B.direction != B.trend:
                if B.trend != '':
                    LogSys.show('ID:{} {} {} ' + Idioma.traducao('Contra Têndencia') + ' {}', B.op_id, B.pair, B.direction, B.trend)
                    roboCtrl.instance().operContrl.calculoTotal(B.op_id, Idioma.traducao('Contra Têndencia'))
                    self.atualizarTela()
                    return
            if roboCtrl.instance().robo.naonoticia:
                tem, noticia = PesquisaNoticia(B.programmedHour.strftime('%H:%M:%S'), B.pair)
                if tem:
                    LogSys.show('ID:{} {} {} ' + Idioma.traducao('Existe notícia de 3 touros') + '\n{} {} {}', B.op_id, B.pair, B.programmedHour.strftime('%H:%M:%S'), noticia.hora, noticia.moeda, noticia.texto)
                    roboCtrl.instance().operContrl.calculoTotal(B.op_id, Idioma.traducao('Notícia'))
                    self.atualizarTela()
                    return
            if B.payout == 0:
                B.payout = 80
            nomesinal = B.op_id + '_' + B.programmedHour.strftime('%H:%M:%S') + '_' + B.pair + '_' + B.direction.upper()
            try:
                roboCtrl.instance().operacoes.index(nomesinal)
            except:
                roboCtrl.instance().add_operacoes = nomesinal
                self.buy(B)
                time.sleep(1)

        else:
            LogSys.show('ID:{} {} {} {} {}.', B.op_id, B.programmedHour, B.pair, B.direction, Idioma.traducao('Excedeu tempo da entrada'))
            roboCtrl.instance().operContrl.calculoTotal(B.op_id, Idioma.traducao('Cancelado'))
            self.atualizarTela()
            return

    def cancelProxSinal(self, operation, gale=0):
        if roboCtrl.instance().robo.usarsoros:
            time.sleep(2)
            try:
                B = operation
                dhInic = operation.hourOrig
                if gale == 0:
                    dhTerm = operation.expirationDate
                elif gale == 1:
                    dhTerm = operation.expirationGale1
                else:
                    dhTerm = operation.expirationGale2
                for sinal in roboCtrl.instance().operContrl.agenda:
                    if sinal.programmedHour >= dhInic:
                        if sinal.programmedHour <= dhTerm:
                            if sinal.op_id != operation.op_id:
                                if not sinal.situacao == Idioma.traducao('Aguardando'):
                                    if sinal.situacao == Idioma.traducao('Agendado'):
                                        pass
                                Agenda.cancelId(sinal.op_id, False)
                                LogSys.save('ID:{} {} {} Cancelado Sobreposto', sinal.op_id, sinal.pair, sinal.programmedHour.strftime('%H:%M:%S'))

                self.atualizarTela()
            except Exception as e:
                try:
                    LogSys.save('Erro Cancelado Sobreposto: {}', str(e))
                finally:
                    e = None
                    del e

    def atualizaTotais(self, operation, id, gale, win):
        B = operation
        if gale == 1:
            vgale = 'Gale1'
        elif gale == 2:
            vgale = 'Gale2'
        else:
            vgale = ''
        win = round(win, 2)
        BL.instance().actual_balance = BL.instance().actual_balance + win
        BL.instance().actual_balance2 = BL.instance().actual_balance
        if win > 0:
            LogSys.save('ID:{} {} {} Payout {} Cod:{} WIN ${}', B.op_id, vgale.upper(), B.pair, int(B.payout), id, win)
            msg = 'ID:{} {} {} Payout {}% WIN ${}'.format(B.op_id, vgale.upper(), B.pair, int(B.payout), win)
            print(msg)
            if gale == 0:
                roboCtrl.instance().operContrl.calculoTotal(B.op_id, 'Win', win)
            else:
                roboCtrl.instance().operContrl.calculoTotal(B.op_id, 'Win ' + vgale, 0, win)
        elif win < 0 or B.typepair == 'D':
            LogSys.save('ID:{} {} {} Payout {} Cod:{} LOSS ${}', B.op_id, vgale.upper(), B.pair, int(B.payout), id, win)
            msg = 'ID:{} {} {} Payout {}% LOSS ${}'.format(B.op_id, vgale.upper(), B.pair, int(B.payout), win)
            print(msg)
            if gale == 0:
                roboCtrl.instance().operContrl.calculoTotal(B.op_id, 'Loss', win)
            else:
                roboCtrl.instance().operContrl.calculoTotal(B.op_id, 'Loss ' + vgale, 0, win)
        else:
            LogSys.save('ID:{} {} {} Payout {} Cod:{} DOJI ${}', B.op_id, vgale.upper(), B.pair, int(B.payout), id, win)
            msg = 'ID:{} {} {} Payout {}% DOJI ${}'.format(B.op_id, vgale.upper(), B.pair, int(B.payout), win)
            print(msg)
            roboCtrl.instance().operContrl.calculoTotal(B.op_id, 'Doji')
        self.atualizarTela()
        self.mostrar_saldo()
        tituloTL = emoji.emojize(':loud_sound:', use_aliases=True) + ' <b>Notificação:</b>'
        msgTL = msg
        msgTL = msgTL.replace(vgale.upper(), '')
        msgTL = msgTL.replace('ID:', emoji.emojize(':id:', use_aliases=True))
        msgTL = msgTL.replace('Payout', emoji.emojize(':bar_chart:', use_aliases=True) + ' Payout:')
        msgTL = msgTL.replace('WIN', '\n' + Idioma.traducao('Resultado:') + ' ' + emoji.emojize(':white_check_mark:', use_aliases=True))
        msgTL = msgTL.replace('LOSS', '\n' + Idioma.traducao('Resultado:') + ' ' + emoji.emojize(':red_circle:', use_aliases=True))
        if gale == 1:
            msgTL = msgTL + ' ' + emoji.emojize(':chicken:', use_aliases=True)
        elif gale == 2:
            msgTL = msgTL + ' ' + emoji.emojize(':chicken:', use_aliases=True) + emoji.emojize(':chicken:', use_aliases=True)
        self.enviarMsgTL(msgTL, tituloTL)

    def resultIQ(self, operation, id, gale, chktaxa, wintaxa):
        B = operation
        if gale == 1:
            dhExp = B.expirationGale1
        elif gale == 2:
            dhExp = B.expirationGale2
        else:
            dhExp = B.expirationDate
        check, win = E.D(id, B.typepair, dhExp)
        if check:
            self.atualizaTotais(operation, id, gale, win)
        else:
            LogSys.save('====> {} {} {} {} {}', id, check, win, B.typepair, dhExp)
            if chktaxa:
                check = chktaxa
                win = wintaxa
                self.atualizaTotais(operation, id, gale, win)
        return (
         check, win)

    def buy(self, operation):
        B = operation

        def resultado_candle():
            chkres = True
            lucro = 0
            velaPeq = False
            try:
                candle = E.getCandles(B.pair, int(B.expirationMode), 1)
                if candle:
                    if B.operaE1.txopen <= 0:
                        B.operaE1.txopen = candle[0]['open']
                    B.operaE1.txclose = candle[0]['close']
                    if B.operaE1.txclose > B.operaE1.txopen:
                        cor = 'G'
                    elif B.operaE1.txclose < B.operaE1.txopen:
                        cor = 'R'
                    else:
                        cor = 'C'
                    if cor == 'G' and not B.direction == 'call':
                        if not cor == 'R' or B.direction == 'put':
                            lucro = round(float(B.operaE1.valor) * (int(B.payout) / 100), 2)
                        else:
                            lucro = float(B.operaE1.valor) * -1
                        velaPeq = self.tamanhoVela(B.operaE1.txopen, B.operaE1.txclose)
            except:
                chkres = False

            return (chkres, float(lucro), velaPeq)

        if B.operaE1.id > 0:
            LogSys.save('ID:{} Entrada Repetida Cancelada Cod: {}', B.op_id, B.operaE1.id)
            return
        valor = B.money
        if roboCtrl.instance().robo.usarsoros:
            BL.instance().sorosgale.calcValorEntrada(B.payout)
        if BL.instance().sorosgale.valor_entrada > 0:
            valor = BL.instance().sorosgale.valor_entrada
        if self.stop_operation(B, float(valor)):
            if roboCtrl.instance().robo.usarsoros:
                BL.instance().sorosgale.valor_lucro = 0
            return
        S, C, tx = E.C(B, valor)
        if S:
            B.operaE1.id = C
            B.operaE1.valor = valor
            B.operaE1.txopen = tx
            LogSys.save('ID:{} {} {} {}M Payout {} {} {} ${} Cod: {} criada com sucesso', B.op_id, B.programmedHour, B.pair, B.expirationMode, B.payout, B.typepairName(), B.direction, round(float(B.operaE1.valor), 2), C)
            roboCtrl.instance().operContrl.calculoTotal(B.op_id, Idioma.traducao('1ª Entrada'))
            self.atualizarTela()
            self.docancelProxSinal(B)
            check = False
            vchkres = False
            vtamPeq = False
            vret = 0
            vesperouTaxa = False
            dhexpira = B.expirationDate - timedelta(seconds=(self.SECOND_RESULT))
            while not check:
                if datetime.now() >= dhexpira:
                    vchkres, vret, vtamPeq = resultado_candle()
                    check = True
                else:
                    time.sleep(1)

            if self.esperarResultTaxa(0):
                vesperouTaxa = True
                if check:
                    if vtamPeq or not vchkres:
                        if vtamPeq:
                            LogSys.save('ID:{} {} Tx({} x {}) ' + Idioma.traducao('Vela pequena, aguardar resultado IQ'), B.op_id, B.pair, B.operaE1.txopen, B.operaE1.txclose)
                        else:
                            LogSys.save('ID:{} {} ' + Idioma.traducao('Não houve retorno de taxas, aguardar resultado IQ'), B.op_id, B.pair)
                        check2, vret2 = self.resultIQ(B, C, 0, vchkres, vret)
                        if check2:
                            check = check2
                            vret = vret2
                    else:
                        BL.instance().actual_balance2 = BL.instance().actual_balance2 + round(vret, 2)
                        self.doresultIQ(B, C, 0, vchkres, vret)
                else:
                    LogSys.save('=> R0 {} {}', C, B.operaE1.valor)
                    check2, vret2 = self.resultIQ(B, C, 0, vchkres, vret)
                    if check2:
                        check = check2
                        vret = vret2
            else:
                check, vret = self.resultIQ(B, C, 0, vchkres, vret)
                vtamPeq = False
            B.operaE1.lucro = vret
            if check:
                if vesperouTaxa:
                    if not vtamPeq:
                        LogSys.save('ID:{} {} Tx({} x {})', B.op_id, B.pair, B.operaE1.txopen, B.operaE1.txclose)
                    if roboCtrl.instance().robo.usarsoros:
                        BL.instance().sorosgale.execute(B.operaE1.lucro)
                if B.operaE1.lucro < 0 or (B.operaE1.lucro == 0 and B.typepair == 'D'):
                    if roboCtrl.instance().robo.qtdgales > 0:
                        self.buy_gale1(B)
                    else:
                        pass
                if not B.operaE1.lucro == 0 or B.typepair != 'D':
                    B.operaE1.id = 0
                    if roboCtrl.instance().robo.usarsoros:
                        BL.instance().sorosgale.valor_lucro = 0
                    self.buy(B)
            else:
                LogSys.save('=> {} {} {}', C, check, B.operaE1.lucro)
        else:
            if roboCtrl.instance().robo.usarsoros:
                BL.instance().sorosgale.valor_lucro = 0
            LogSys.show('ID:{} {} ${} - {} {}', B.op_id, B.pair, round(float(valor), 2), Idioma.traducao('Resposta IQ:'), C)
            roboCtrl.instance().operContrl.calculoTotal(B.op_id, Idioma.traducao('Fechado'))
            self.atualizarTela()

    def buy_gale1(self, operation):
        B = operation

        def resultado_candle():
            chkres = True
            velaPeq = False
            lucro = 0
            try:
                candle = E.getCandles(B.pair, int(B.expirationMode), 1)
                if candle:
                    if B.operaG1.txopen <= 0:
                        B.operaG1.txopen = candle[0]['open']
                    B.operaG1.txclose = candle[0]['close']
                    if B.operaG1.txclose > B.operaG1.txopen:
                        cor = 'G'
                    elif B.operaG1.txclose < B.operaG1.txopen:
                        cor = 'R'
                    else:
                        cor = 'C'
                    if cor == 'G' and not B.direction == 'call':
                        if not cor == 'R' or B.direction == 'put':
                            lucro = round(float(B.operaG1.valor) * (int(B.payout) / 100), 2)
                        else:
                            lucro = float(B.operaG1.valor) * -1
                        velaPeq = self.tamanhoVela(B.operaG1.txopen, B.operaG1.txclose)
            except:
                pass

            return (
             chkres, float(lucro), velaPeq)

        if P(B.gale1.replace(Q, K).replace(R, K)) == 0:
            return
        if B.operaG1.id > 0:
            LogSys.save('ID:{} GALE1 Entrada Repetida Cancelada Cod: {}', B.op_id, B.operaG1.id)
            return
        dhmax = B.expirationDate + timedelta(seconds=20)
        if datetime.now() > dhmax:
            LogSys.save('ID:{} GALE1 {} Tempo máximo de entrada expirado', B.op_id, B.expirationDate)
            return
        valor = B.gale1
        if roboCtrl.instance().robo.usarsoros:
            BL.instance().sorosgale.calcValorEntrada(B.payout)
        if BL.instance().sorosgale.valor_entrada > 0:
            if roboCtrl.instance().robo.qtdgales < 1:
                if roboCtrl.instance().robo.usarsoros:
                    BL.instance().sorosgale.valor_lucro = 0
                return
            valor = BL.instance().sorosgale.valor_entrada
        if self.stop_operation(B, float(valor)):
            if roboCtrl.instance().robo.usarsoros:
                BL.instance().sorosgale.valor_lucro = 0
            return
        S, C, tx = E.C(B, valor)
        if S:
            B.operaG1.id = C
            B.operaG1.valor = valor
            B.operaG1.txopen = tx
            LogSys.save('ID:{} GALE1 {} {}M Payout {} {} {} ${} Cod: {} criada com sucesso', B.op_id, B.pair, B.expirationMode, B.payout, B.typepairName(), B.direction, round(float(B.operaG1.valor), 2), C)
            roboCtrl.instance().operContrl.calculoTotal(B.op_id, 'Gale 1')
            self.atualizarTela()
            self.docancelProxSinal(B, 1)
            check = False
            vchkres = False
            vtamPeq = False
            vret = 0
            vesperouTaxa = False
            dhexpira = B.expirationGale1 - timedelta(seconds=(self.SECOND_RESULT))
            while not check:
                if datetime.now() >= dhexpira:
                    vchkres, vret, vtamPeq = resultado_candle()
                    check = True
                else:
                    time.sleep(1)

            if self.esperarResultTaxa(1):
                vesperouTaxa = True
                if check:
                    if vtamPeq or not vchkres:
                        if vtamPeq:
                            LogSys.save('ID:{} GALE1 {} Tx({} x {}) ' + Idioma.traducao('Vela pequena, aguardar resultado IQ'), B.op_id, B.pair, B.operaG1.txopen, B.operaG1.txclose)
                        else:
                            LogSys.save('ID:{} GALE1 {} ' + Idioma.traducao('Não houve retorno de taxas, aguardar resultado IQ'), B.op_id, B.pair)
                        check2, vret2 = self.resultIQ(B, C, 1, vchkres, vret)
                        if check2:
                            check = check2
                            vret = vret2
                    else:
                        BL.instance().actual_balance2 = BL.instance().actual_balance2 + round(vret, 2)
                        self.doresultIQ(B, C, 1, vchkres, vret)
                else:
                    LogSys.save('=> R1 GALE1 {} {}', C, B.operaG1.valor)
                    check2, vret2 = self.resultIQ(B, C, 1, vchkres, vret)
                    if check2:
                        check = check2
                        vret = vret2
            else:
                check, vret = self.resultIQ(B, C, 1, vchkres, vret)
                vtamPeq = False
            B.operaG1.lucro = vret
            if check:
                if vesperouTaxa:
                    if not vtamPeq:
                        LogSys.save('ID:{} GALE1 {} Tx({} x {})', B.op_id, B.pair, B.operaG1.txopen, B.operaG1.txclose)
                    if roboCtrl.instance().robo.usarsoros:
                        BL.instance().sorosgale.execute(B.operaG1.lucro)
                if B.operaG1.lucro < 0:
                    self.buy_gale2(B)
                elif not B.operaG1.lucro == 0 or B.typepair != 'D':
                    B.operaG1.id = 0
                    if roboCtrl.instance().robo.usarsoros:
                        BL.instance().sorosgale.valor_lucro = 0
                    self.buy_gale1(B)
            else:
                LogSys.save('=> GALE1 {} {} {}', C, check, B.operaG1.lucro)
        else:
            if roboCtrl.instance().robo.usarsoros:
                BL.instance().sorosgale.valor_lucro = 0
            LogSys.show('ID:{} GALE1 {} ${} - {} {}', B.op_id, B.pair, round(float(valor), 2), Idioma.traducao('Resposta IQ:'), C)

    def buy_gale2(self, operation):
        B = operation

        def resultado_candle():
            chkres = True
            velaPeq = False
            lucro = 0
            try:
                candle = E.getCandles(B.pair, int(B.expirationMode), 1)
                if candle:
                    if B.operaG2.txopen <= 0:
                        B.operaG2.txopen = candle[0]['open']
                    B.operaG2.txclose = candle[0]['close']
                    if B.operaG2.txclose > B.operaG2.txopen:
                        cor = 'G'
                    elif B.operaG2.txclose < B.operaG2.txopen:
                        cor = 'R'
                    else:
                        cor = 'C'
                    if cor == 'G' and not B.direction == 'call':
                        if not cor == 'R' or B.direction == 'put':
                            lucro = round(float(B.operaG2.valor) * (int(B.payout) / 100), 2)
                        else:
                            lucro = float(B.operaG2.valor) * -1
                        velaPeq = self.tamanhoVela(B.operaG2.txopen, B.operaG2.txclose)
            except:
                pass

            return (
             chkres, float(lucro), velaPeq)

        if P(B.gale2.replace(Q, K).replace(R, K)) == 0:
            return
        if B.operaG2.id > 0:
            LogSys.save('ID:{} GALE2 Entrada Repetida Cancelada Cod: {}', B.op_id, B.operaG2.id)
            return
        dhmax = B.expirationGale1 + timedelta(seconds=20)
        if datetime.now() > dhmax:
            LogSys.save('ID:{} GALE2 {} Tempo máximo de entrada expirado', B.op_id, B.expirationGale1)
            return
        valor = B.gale2
        if roboCtrl.instance().robo.usarsoros:
            BL.instance().sorosgale.calcValorEntrada(B.payout)
        if BL.instance().sorosgale.valor_entrada > 0:
            if roboCtrl.instance().robo.qtdgales < 2:
                if roboCtrl.instance().robo.usarsoros:
                    BL.instance().sorosgale.valor_lucro = 0
                return
            valor = BL.instance().sorosgale.valor_entrada
        if self.stop_operation(B, float(valor)):
            if roboCtrl.instance().robo.usarsoros:
                BL.instance().sorosgale.valor_lucro = 0
            return
        S, C, tx = E.C(B, valor)
        if S:
            B.operaG2.id = C
            B.operaG2.valor = valor
            B.operaG2.txopen = tx
            LogSys.save('ID:{} GALE2 {} {}M Payout {} {} {} ${} Cod: {} criada com sucesso', B.op_id, B.pair, B.expirationMode, B.payout, B.typepairName(), B.direction, round(float(B.operaG2.valor), 2), C)
            roboCtrl.instance().operContrl.calculoTotal(B.op_id, 'Gale 2')
            self.atualizarTela()
            self.docancelProxSinal(B, 2)
            check = False
            vchkres = False
            vret = 0
            dhexpira = B.expirationGale2 - timedelta(seconds=(self.SECOND_RESULT))
            while not check:
                if datetime.now() >= dhexpira:
                    vchkres, vret, vtamPeq = resultado_candle()
                    check = True
                else:
                    time.sleep(1)

            check, vret = self.resultIQ(B, C, 2, vchkres, vret)
            B.operaG2.lucro = vret
            if check:
                if roboCtrl.instance().robo.usarsoros:
                    BL.instance().sorosgale.execute(B.operaG2.lucro)
                if not B.operaG2.lucro == 0 or B.typepair != 'D':
                    B.operaG2.id = 0
                    if roboCtrl.instance().robo.usarsoros:
                        BL.instance().sorosgale.valor_lucro = 0
                    self.buy_gale2(B)
            else:
                LogSys.save('=>> GALE2 {} {} {}', C, check, B.operaG2.lucro)
        else:
            if roboCtrl.instance().robo.usarsoros:
                BL.instance().sorosgale.valor_lucro = 0
            LogSys.show('ID:{} GALE2 {} ${} - {} {}', B.op_id, B.pair, round(float(valor), 2), Idioma.traducao('Resposta IQ:'), C)

    def calcValorFatorReducao(self, fator: float, value: float):
        return round(value * (fator / 100), 2)

    def atualizaNovosValoresPosStopWin(self):
        roboCtrl.instance().robo.ultrapassoustopwin = True
        BL.instance().stop_limit = calcValorFatorReducao(1 - roboCtrl.instance().robo.percwinpos, BL.instance().win_limit)
        BL.instance().win_limit = calcValorFatorReducao(roboCtrl.instance().robo.percwinpos, BL.instance().win_limit)
        roboCtrl.instance().robo.ent_valor1 = calcValorFatorReducao(roboCtrl.instance().robo.percwinpos, roboCtrl.instance().robo.ent_valor1)
        roboCtrl.instance().robo.ent_gale1 = calcValorFatorReducao(roboCtrl.instance().robo.percwinpos, roboCtrl.instance().robo.ent_gale1)
        roboCtrl.instance().robo.ent_gale2 = calcValorFatorReducao(roboCtrl.instance().robo.percwinpos, roboCtrl.instance().robo.ent_gale2)
        roboCtrl.instance().view.janela['stopgainv'].update(value=(round(C.instance().win_limit, 2)))
        roboCtrl.instance().view.janela['stoplossv'].update(value=(round(C.instance().stop_limit, 2)))
        if roboCtrl.instance().robo.gerenciar == 0:
            LogSys.show(Idioma.traducao('Entradas fixas:'))
            LogSys.show(Idioma.traducao('Entrada: $') + '{}', round(roboCtrl.instance().robo.ent_valor1, 2))
            if roboCtrl.instance().robo.ent_gale1 > 0:
                LogSys.show(Idioma.traducao('Gale 1: $') + '{}', round(roboCtrl.instance().robo.ent_gale1, 2))
            if roboCtrl.instance().robo.ent_gale2 > 0:
                LogSys.show(Idioma.traducao('Gale 2: $') + '{}', round(roboCtrl.instance().robo.ent_gale2, 2))
        elif roboCtrl.instance().robo.gerenciar == 1:
            roboCtrl.instance().sorosgale.config_ini(calcValorFatorReducao(roboCtrl.instance().robo.percwinpos, roboCtrl.instance().robo.valorinicial), roboCtrl.instance().robo.percent, roboCtrl.instance().robo.modelo, 1)
        elif roboCtrl.instance().robo.gerenciar == 2:
            roboCtrl.instance().sorosgale.config_ini(calcValorFatorReducao(roboCtrl.instance().robo.percwinpos, roboCtrl.instance().robo.valorinicial), roboCtrl.instance().robo.valorentsoros, 'S', roboCtrl.instance().robo.nivelsoros)