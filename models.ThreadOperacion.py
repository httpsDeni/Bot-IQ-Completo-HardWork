# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: models\ThreadOperacion.py
# Compiled at: 1995-09-27 13:18:56
# Size of source mod 2**32: 272 bytes
import sys, time, threading

class StopThread(StopIteration):
    pass


threading.SystemExit = (
 SystemExit, StopThread)

class ThreadOper(threading.Thread):

    def stop(self):
        self._ThreadOper__stop = True

    def _bootstrap(self):
        if threading._trace_hook is not None:
            raise ValueError('Não é possível executar o segmento com rastreamento!')
        self._ThreadOper__stop = False
        self.daemon = True
        sys.settrace(self._ThreadOper__trace)
        super()._bootstrap()

    def __trace(self, frame, event, arg):
        if self._ThreadOper__stop:
            raise StopThread()
        return self._ThreadOper__trace