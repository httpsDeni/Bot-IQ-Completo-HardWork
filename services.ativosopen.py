import time
from datetime import datetime
import connection.APIConnection as APIConnection
import models.roboController as roboCtrl
from models.ThreadOperacion import *
from main.roboUtils import *

class AtivosAbertos:
    aguardarMinutos1 = 20
    aguardarMinutos2 = 5
    executor = ThreadOper()

    def verif_ativos(self):
        while roboCtrl.instance().robo.iniciado:
            try:
                roboCtrl.instance().robo.ativosabertos = APIConnection.instance().connection.get_all_open_time()
                time.sleep(60 * self.aguardarMinutos1)
            except Exception as e:
                try:
                    LogSys.save('Não foi possível buscar a lista de ativos, fazendo nova tentativa. Erro: {0}'.format(str(e)))
                    time.sleep(60 * self.aguardarMinutos2)
                finally:
                    e = None
                    del e

    def start_ativos(self):
        self.executor = ThreadOper(target=(self.verif_ativos), args=())
        roboCtrl.instance().add_listThread = self.executor
        self.executor.start()

    def stop_ativos(self):
        self.executor.stop()