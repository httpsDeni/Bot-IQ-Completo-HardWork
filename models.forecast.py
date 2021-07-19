# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: models\forecast.py
# Compiled at: 1995-09-27 13:18:56
# Size of source mod 2**32: 272 bytes


class forecast:

    def __init__(self):
        self.total_entradas = 0
        self.stop_win = 0
        self.payout = 0
        self.valor_inicial = 0
        self.count = 0
        self.count_win = 0
        self.count_loss = 0
        self.valor_entrada = 0
        self.valor_lucro = 0
        self.total_lucro = 0
        self.stop = False

    def config_ini(self, total_entradas: int, stop_win: int, valorinicial: float):
        self.total_entradas = total_entradas
        self.stop_win = stop_win
        self.valor_inicial = round(valorinicial, 2)
        self.fatores = {}
        self.count = 0
        self.count_win = 0
        self.count_loss = 0
        self.valor_entrada = 0
        self.valor_lucro = 0
        self.total_lucro = 0
        self.stop = False

    def prevValorEntrada(self, total_entradas: int, stop_win: int, valorinicial: float, payout: int):
        self.config_ini(total_entradas, stop_win, valorinicial)
        self.calcValorEntrada(payout)
        return self.valor_entrada

    def calcValorEntrada(self, payout: int):
        if payout == 0:
            self.payout = 80
        else:
            self.payout = payout
        self.payout = self.payout / 100
        self._forecast__gerarFatores()
        try:
            vfatorw = self.fatores[self.getKey(self.count + 1, self.count_win + 1)]
            vfatorl = self.fatores[self.getKey(self.count + 1, self.count_win)]
        except:
            vfatorw = 0
            vfatorl = 0

        vtotal = round(self.valor_inicial + self.total_lucro, 2)
        try:
            if vfatorw > 0 and vfatorl > 0:
                vcalc = 1 - (1 + self.payout) * (vfatorw / (vfatorl + self.payout * vfatorw))
                self.valor_entrada = round(vcalc * vtotal, 2)
            else:
                self.valor_entrada = round(vtotal, 2)
        except:
            self.valor_entrada = round(vtotal, 2)

        if self.valor_entrada < 0:
            self.valor_entrada = 0
        self.stop = self.count_win >= self.stop_win or self.count >= self.total_entradas

    def execute(self, result: float=0):
        self.valor_lucro = round(result, 2)
        self.count += 1
        if self.valor_lucro > 0:
            self.count_win += 1
            self.total_lucro
            self.total_lucro = round(self.total_lucro + self.valor_lucro, 2)
        elif self.valor_lucro < 0:
            self.count_loss += 1
            self.total_lucro = round(self.total_lucro - self.valor_entrada, 2)

    def getKey(self, win, loss):
        return f"'{win}-{loss}'"

    def __gerarFatores(self):
        payout = self.payout + 1
        for _w in range(self.total_entradas - 1, -1, -1):
            for _l in range(self.stop_win, -1, -1):
                key = self.getKey(_w, _l)
                value = 0
                if _l == self.stop_win:
                    value = 1
                else:
                    pass
                if self.stop_win - _l == self.total_entradas - _w:
                    value = round(payout ** (self.total_entradas - _w), 5)
                else:
                    try:
                        win_Prox = self.fatores[self.getKey(_w + 1, _l)]
                        loss_Prox = self.fatores[self.getKey(_w + 1, _l + 1)]
                        value = round(payout * win_Prox * loss_Prox / (win_Prox + (payout - 1) * loss_Prox), 5)
                    except:
                        value = 0

                try:
                    self.fatores[key] = value
                except:
                    pass