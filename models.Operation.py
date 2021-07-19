# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: models\Operation.py
# Compiled at: 1995-09-27 13:18:56
# Size of source mod 2**32: 272 bytes
from main.roboUtils import Idioma

class V:
    id = 0
    valor = 0
    lucro = 0
    txopen = 0
    txclose = 0


class A:

    def __init__(self, op_id, pair, expirationMode, direction, money, gale1, gale2, hourOrig, programmedHour, expirationDate, expirationGale1, expirationGale2, day, pre_order, typepair='D'):
        self.op_id = op_id
        self.pair = pair
        self.expirationMode = expirationMode
        self.direction = direction
        self.money = money
        self.hourOrig = hourOrig
        self.programmedHour = programmedHour
        self.expirationDate = expirationDate
        self.expirationGale1 = expirationGale1
        self.expirationGale2 = expirationGale2
        self.day = day
        self.gale1 = gale1
        self.gale2 = gale2
        self.pre_order = pre_order
        self.typepair = typepair
        self.payout = 0
        self.trend = ''
        self.situacao = Idioma.traducao('Agendado')
        self.lucro = 0
        self.operaE1 = V()
        self.operaG1 = V()
        self.operaG2 = V()

    def typepairName(self):
        if self.typepair == 'D':
            return 'Digital'
        return 'Binaria'