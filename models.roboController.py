import threading
from datetime import datetime, date
from models.OperationCalc import *
HOST_NAME = 'http://74.63.254.230:8087/'

class roboController(object):
    _roboController__instance = None
    _roboController__robo = None
    _roboController__view = 'console'
    _roboController__thr_conexao = None
    _roboController__thr_conexao: threading
    _roboController__listThread = []
    _roboController__dianoticias = 0
    _roboController__noticias = []
    _roboController__operacoes = []
    _roboController__telegran1 = None
    operContrl = operController()

    @property
    def robo(self):
        return self._roboController__robo

    @robo.setter
    def robo(self, value):
        self._roboController__robo = value

    @property
    def view(self):
        return self._roboController__view

    @view.setter
    def view(self, value):
        self._roboController__view = value

    @property
    def thr_conexao(self):
        return self._roboController__thr_conexao

    @thr_conexao.setter
    def thr_conexao(self, value):
        self._roboController__thr_conexao = value

    @property
    def listThread(self):
        return self._roboController__listThread

    @listThread.setter
    def add_listThread(self, value):
        self._roboController__listThread.append(value)

    @property
    def dianoticias(self):
        return self._roboController__dianoticias

    @dianoticias.setter
    def dianoticias(self, value):
        self._roboController__dianoticias = value

    @property
    def noticias(self):
        return self._roboController__noticias

    @noticias.setter
    def add_noticias(self, value):
        self._roboController__noticias.append(value)

    @property
    def operacoes(self):
        return self._roboController__operacoes

    @noticias.setter
    def add_operacoes(self, value):
        self._roboController__operacoes.append(value)

    @noticias.setter
    def clear_operacoes(self, value):
        self._roboController__operacoes = []

    @property
    def telegran1(self):
        return self._roboController__telegran1

    @telegran1.setter
    def telegran1(self, value):
        self._roboController__telegran1 = value

    @staticmethod
    def instance():
        if not roboController._roboController__instance:
            roboController._roboController__instance = roboController()
        return roboController._roboController__instance
