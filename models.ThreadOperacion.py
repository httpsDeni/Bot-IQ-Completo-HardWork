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
