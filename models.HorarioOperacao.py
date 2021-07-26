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
