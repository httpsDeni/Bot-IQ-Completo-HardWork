# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: models\HorarioOperacao.py
# Compiled at: 1995-09-27 13:18:56
# Size of source mod 2**32: 272 bytes
import time
from datetime import datetime, timedelta

class HorarioOpera:

    def __init__(self, *args):
        self.horaInicio = None
        self.minInicio = None
        self.horaTermino = None
        self.minTermino = None

    def getDateTimeInicio(self):
        return datetime(datetime.now().year, datetime.now().month, datetime.now().day, self.horaInicio, self.minInicio, 0)

    def getDateTimeTermino(self):
        return datetime(datetime.now().year, datetime.now().month, datetime.now().day, self.horaTermino, self.minTermino, 0)

    def toStr(self):
        return '{:02d}'.format(self.horaInicio) + ':' + '{:02d}'.format(self.minInicio) + '  -  ' + '{:02d}'.format(self.horaTermino) + ':' + '{:02d}'.format(self.minTermino)

    def importTxt(self, item):
        c = 0
        x = item.split()
        for a in x:
            if ':' in a:
                c += 1
                if c == 1:
                    hr = a.split(':')
                    self.horaInicio = int(hr[0])
                    self.minInicio = int(hr[1])
                else:
                    hr = a.split(':')
                    self.horaTermino = int(hr[0])
                    self.minTermino = int(hr[1])