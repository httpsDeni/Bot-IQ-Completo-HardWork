class sorosgale:

    def __init__(self):
        self.payout = 80
        self.modelo = 'A'
        self.perc_entrada = 1
        self.valor_lucro = 0
        self.count_soros = 0
        self.count_win = 0
        self.count_loss = 0
        self.valor_entrada = 0
        self.valor_recuperar = 0
        self.qtdgales = 0
        self.entrada_inicial = self.valor_entrada
        self.valor10 = 0
        self.valor11 = 0
        self.valor12 = 0
        self.valor20 = 0
        self.valor21 = 0
        self.valor22 = 0
        self.valor30 = 0
        self.valor31 = 0
        self.valor32 = 0
        self.max_loss = 0

    def config_ciclos(self, valor10: float=0, valor11: float=0, valor12: float=0, valor20: float=0, valor21: float=0, valor22: float=0, valor30: float=0, valor31: float=0, valor32: float=0):
        self.valor10 = round(valor10, 2)
        self.valor11 = round(valor11, 2)
        self.valor12 = round(valor12, 2)
        self.valor20 = round(valor20, 2)
        self.valor21 = round(valor21, 2)
        self.valor22 = round(valor22, 2)
        self.valor30 = round(valor30, 2)
        self.valor31 = round(valor31, 2)
        self.valor32 = round(valor32, 2)
        if self.valor11 > 0:
            self.max_loss += 1
        if self.valor12 > 0:
            self.max_loss += 1
        if self.valor20 > 0:
            self.max_loss += 1
        if self.valor21 > 0:
            self.max_loss += 1
        if self.valor22 > 0:
            self.max_loss += 1
        if self.valor30 > 0:
            self.max_loss += 1
        if self.valor31 > 0:
            self.max_loss += 1
        if self.valor32 > 0:
            self.max_loss += 1
        self.valorperc = 'V'
        self.valor_inicial = self.valor10
        self._sorosgale__calculo_entrada_inicial(self.valor_inicial)
        self.entrada_inicial = self.valor_entrada
        self.valor_lucro = 0

    def config_ini(self, valor_inicial: float, perc_entrada: float, modelo: str='C', total_soros: int=1, valorperc: str='P'):
        self.modelo = modelo.upper()
        self.valorperc = valorperc
        self.perc_entrada = perc_entrada
        self.valor_inicial = valor_inicial
        self.total_soros = 0
        self.fator_soros = 0
        self.total_soros = 1
        if self.modelo == 'A':
            self.fator_soros = 0.5
        elif self.modelo == 'M':
            self.fator_soros = 0.25
        elif self.modelo == 'S':
            self.total_soros = total_soros
        self.fator_valor = round(self.valor_inicial * self.fator_soros / 100, 2)
        self.count_soros = 0
        self.count_win = 0
        self.count_loss = 0
        self.valor_recuperar = 0
        self.valor_entrada = 0
        self._sorosgale__calculo_entrada_inicial(self.valor_inicial)
        self.entrada_inicial = self.valor_entrada
        self.valor_lucro = 0

    def __calculo_entrada_inicial(self, valor: float):
        if self.valorperc == 'P':
            self.valor_entrada = round(valor * self.perc_entrada / 100, 2)
        else:
            self.valor_entrada = valor
        self.valor_lucro = round(self.valor_entrada * self.payout / 100, 2)

    def __calculo_entrada_loss(self, valor: float):
        self.valor_entrada = round(self.valor_recuperar / self.payout * 100, 2)
        if self.fator_soros > 0:
            self.valor_entrada = round(self.valor_entrada + self.fator_valor * (self.payout / 100), 2)
        self.valor_lucro = round(self.valor_entrada * self.payout / 100, 2)

    def calcValorEntrada(self, payout: float):
        if payout == 0:
            self.payout = 80
        else:
            self.payout = payout
        if self.count_win == 0 and self.count_loss == 0:
            self._sorosgale__calculo_entrada_inicial(self.valor_inicial)
        elif not (self.valor_lucro > 0and self.count_soros <= self.total_soros and self.count_soros <= self.total_soros and self.modelo[0] != 'L'):
            if not self.count_soros < self.total_soros or self.modelo == 'S':
                self.valor_entrada = self.valor_entrada + self.valor_lucro
                self.valor_lucro = round(self.valor_entrada * self.payout / 100, 2)
            else:
                self.count_soros = 0
                self._sorosgale__calculo_entrada_inicial(self.valor_inicial)
            self.count_soros += 1
        elif self.valor_lucro < 0:
            self.count_soros = 0
            if self.modelo == 'S':
                self._sorosgale__calculo_entrada_inicial(self.valor_inicial)
            elif self.modelo == 'L0':
                self.defineValorCicloMaoFixa()
            elif self.modelo == 'L1':
                self.defineValorCicloGale1()
            elif self.modelo == 'L2':
                self.defineValorCicloGale2()
            else:
                self._sorosgale__calculo_entrada_loss(self.valor_recuperar)

    def execute(self, result: float=0):
        self.valor_lucro = round(result, 2)
        if self.valor_lucro > 0:
            self.count_win += 1
            if self.modelo[0] == 'L':
                self.count_win = 0
                self.count_loss = 0
            if self.valor_recuperar > 0:
                self.valor_recuperar = round(self.valor_recuperar - self.valor_lucro, 2)
            if self.valor_recuperar < 0:
                self.valor_recuperar = 0
        elif self.valor_lucro < 0:
            if self.count_loss == self.max_loss and self.modelo[0] == 'L':
                self.count_loss = 0
            else:
                self.count_loss += 1
            if self.modelo[0] == 'L':
                self.count_win = 0
            self.valor_recuperar = round(self.valor_recuperar + self.valor_entrada, 2)

    def defineValorCicloMaoFixa(self):
        if self.count_loss == 0:
            self._sorosgale__calculo_entrada_inicial(self.valor10)
        elif self.count_loss == 1:
            if self.valor11 > 0:
                self._sorosgale__calculo_entrada_inicial(self.valor11)
            else:
                self._sorosgale__calculo_entrada_inicial(self.valor10)
        elif self.count_loss == 2:
            if self.valor12 > 0:
                self._sorosgale__calculo_entrada_inicial(self.valor12)
            else:
                self._sorosgale__calculo_entrada_inicial(self.valor10)
        elif self.count_loss == 3:
            if self.valor20 > 0:
                self._sorosgale__calculo_entrada_inicial(self.valor20)
            else:
                self._sorosgale__calculo_entrada_inicial(self.valor10)
        elif self.count_loss == 4:
            if self.valor21 > 0:
                self._sorosgale__calculo_entrada_inicial(self.valor21)
            else:
                self._sorosgale__calculo_entrada_inicial(self.valor10)
        elif self.count_loss == 5:
            if self.valor22 > 0:
                self._sorosgale__calculo_entrada_inicial(self.valor22)
            else:
                self._sorosgale__calculo_entrada_inicial(self.valor10)
        elif self.count_loss == 6:
            if self.valor30 > 0:
                self._sorosgale__calculo_entrada_inicial(self.valor30)
            else:
                self._sorosgale__calculo_entrada_inicial(self.valor10)
        elif self.count_loss == 7:
            if self.valor31 > 0:
                self._sorosgale__calculo_entrada_inicial(self.valor31)
            else:
                self._sorosgale__calculo_entrada_inicial(self.valor10)
        elif self.count_loss == 8:
            if self.valor32 > 0:
                self._sorosgale__calculo_entrada_inicial(self.valor32)
            else:
                self._sorosgale__calculo_entrada_inicial(self.valor10)
        else:
            self._sorosgale__calculo_entrada_inicial(self.valor10)

    def defineValorCicloGale1(self):
        if self.count_loss == 1:
            self._sorosgale__calculo_entrada_inicial(self.valor11)
        elif self.count_loss == 2:
            self._sorosgale__calculo_entrada_inicial(self.valor20)
        elif self.count_loss == 3:
            self._sorosgale__calculo_entrada_inicial(self.valor21)
        elif self.count_loss == 4:
            self._sorosgale__calculo_entrada_inicial(self.valor30)
        elif self.count_loss == 5:
            self._sorosgale__calculo_entrada_inicial(self.valor31)
        else:
            self._sorosgale__calculo_entrada_inicial(self.valor10)

    def defineValorCicloGale2(self):
        if self.count_loss == 1:
            self._sorosgale__calculo_entrada_inicial(self.valor11)
        elif self.count_loss == 2:
            self._sorosgale__calculo_entrada_inicial(self.valor12)
        elif self.count_loss == 3:
            self._sorosgale__calculo_entrada_inicial(self.valor20)
        elif self.count_loss == 4:
            self._sorosgale__calculo_entrada_inicial(self.valor21)
        elif self.count_loss == 5:
            self._sorosgale__calculo_entrada_inicial(self.valor22)
        elif self.count_loss == 6:
            self._sorosgale__calculo_entrada_inicial(self.valor30)
        elif self.count_loss == 7:
            self._sorosgale__calculo_entrada_inicial(self.valor31)
        elif self.count_loss == 8:
            self._sorosgale__calculo_entrada_inicial(self.valor32)
        else:
            self._sorosgale__calculo_entrada_inicial(self.valor10)