import os, sys, socket, selectors, types, time, datetime, configparser
from main.roboUtils import *
from services.utils import *
from services import loadlist
import services.scheduleservice as Agenda
import models.roboController as roboCtrl
FORMAT = 'utf-8'

class serverSocket:

    def __init__(self, server, port):
        self.ADDR = (
         server, port)
        self.srvsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.srvsocket.bind(self.ADDR)
        self.sel = selectors.DefaultSelector()
        self.srvsocket.listen()
        self.srvsocket.setblocking(False)
        self.sel.register((self.srvsocket), (selectors.EVENT_READ), data=None)

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b'', outb=b'')
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024).decode(FORMAT)
            if recv_data:
                LogSys.save('{} sinal recebido', recv_data[:17])
                self.loadsinal(recv_data)
            else:
                self.sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                try:
                    msg = str(data.outb, FORMAT)
                    LogSys.save(msg[:17])
                    self.loadsinal(msg)
                    data.outb = b''
                except Exception as e:
                    try:
                        LogSys.save('#5 {}', str(e))
                    finally:
                        e = None
                        del e

                self.sel.unregister(sock)
                sock.close()

    def loadsinal(self, dados):
        if roboCtrl.instance().robo.iniciado:
            try:
                dados = str(dados).split(';')
                datahora = dados[0]
                ativo = dados[1]
                acao = dados[2]
                duracao = dados[3]
                afiliado = int(dados[4])
                try:
                    indicador = int(dados[5])
                except:
                    indicador = 0

                if afiliado > 0 and roboCtrl.instance().robo.Lic.idafiliado != afiliado:
                    LogSys.show(Idioma.traducao('Sinal enviado pelo servidor, não é válido para este robô. Cod.') + str(afiliado))
                else:
                    qtdlista, lista = loadlist.geraSinalMT4(0, datahora, ativo, acao, duracao, roboCtrl.instance().robo.ent_valor1, roboCtrl.instance().robo.ent_gale1, roboCtrl.instance().robo.ent_gale2)
                    if qtdlista > 0:
                        Agenda.P(lista)
            except Exception as e:
                try:
                    LogSys.save('#7 {}', str(e))
                    try:
                        LogSys.save(dados)
                    except:
                        pass

                finally:
                    e = None
                    del e