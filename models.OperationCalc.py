# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: models\OperationCalc.py
# Compiled at: 1995-09-27 13:18:56
# Size of source mod 2**32: 272 bytes


class operController(object):

    def __init__(self):
        self.agenda = []
        self.wins = 0
        self.hits = 0
        self.saldo = 0

    def somaWin(self, value):
        self.wins += 1
        self.saldo += round(value, 2)

    def somaLoss(self, value):
        self.hits += 1
        self.saldo += round(value, 2)

    def delLoss(self):
        self.hits -= 1

    def zerar(self):
        self.wins = 0
        self.hits = 0
        self.saldo = 0

    def getAssertividade(self):
        try:
            return round(self.wins / (self.wins + abs(self.hits)) * 100, 2)
        except:
            return 0

    def calculoTotal(self, id, situacao, win=0, win2=0):
        vwin = win
        if win == 0:
            if win2 != 0:
                vwin = win2
        if vwin < 0 or (vwin > 0):
            if win2 != 0:
                self.delLoss()
            if vwin > 0:
                self.somaWin(vwin)
            if vwin < 0:
                self.somaLoss(vwin)
        self.atualAgenda(id, situacao, vwin)

    def atualAgenda(self, id, situacao, vwin=0):
        for sinal in self.agenda:
            if int(sinal.op_id) == int(id):
                self.agenda[(int(sinal.op_id) - 1)].situacao = situacao
                if not vwin < 0:
                    if vwin > 0:
                        pass
                self.agenda[(int(sinal.op_id) - 1)].lucro += vwin

    def cancelAgenda(self, id, situacao, sitAceitas):
        for sinal in self.agenda:
            if int(sinal.op_id) >= int(id):
                try:
                    sitAceitas.index(sinal.situacao)
                    sinal.situacao = situacao
                    self.agenda[(int(sinal.op_id) - 1)].situacao = sinal.situacao
                except:
                    pass

    def cancelAgendaId(self, id, situacao, sitAceitas):
        for sinal in self.agenda:
            if int(sinal.op_id) == int(id):
                try:
                    sitAceitas.index(sinal.situacao)
                    sinal.situacao = situacao
                    self.agenda[(int(sinal.op_id) - 1)].situacao = sinal.situacao
                except:
                    pass

                break