import time
from datetime import datetime, timedelta
import simplejson as Y
from collections import OrderedDict as X
import csv
import models.roboController as roboCtrl
from main.roboUtils import *
V = 'Nao agendado'
U = 'Situação'
T = 'Expiração(Min)'
S = 'Gale 2($)'
R = 'Gale 1($)'
Q = 'Valor($)'
P = 'Operação'
O = 'Dia'
N = 'Ativo'
K = 'ID'
J = 'Horário'
H = ':'

def remove_carespeciais(old):
    to_remove = '!@#$%¨&ï»¿'
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x, '')

    return new_string


def geralista(arq, ent_valor1, ent_gale1, ent_gale2, usarsoros):
    W = []
    tmp = []
    cnt = 0
    b = None
    try:
        with open(arq) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            cnt = 0
            line_count = 0
            for B in csv_reader:
                if B:
                    if str(B[0]) != 'Moeda':
                        if str(B[0]) != 'Ativo':
                            if str(B[0]) != '':
                                A = X()
                                hr = B[2].split(H)
                                F = '{:02d}'.format(int(hr[0]))
                                G = '{:02d}'.format(int(hr[1]))
                                try:
                                    I = str(hr[2])
                                except:
                                    I = str('00')

                                cnt += 1
                                try:
                                    A[K] = int(cnt)
                                    A[N] = remove_carespeciais(str(B[0]).strip())
                                    A[O] = int(B[1].strip())
                                    A[J] = str(F) + H + str(G) + H + str(I)
                                    A[P] = remove_carespeciais(str(B[3]).strip())
                                    A[Q] = B[4].strip()
                                    A[R] = B[5].strip()
                                    A[S] = B[6].strip()
                                    A[T] = int(B[7])
                                    A[U] = V
                                except:
                                    A[K] = int(cnt)
                                    A[N] = remove_carespeciais(str(B[0]).strip())
                                    A[O] = int(B[1].strip())
                                    A[J] = str(F) + H + str(G) + H + str(I)
                                    A[P] = remove_carespeciais(str(B[3]).strip())
                                    A[Q] = ent_valor1
                                    A[R] = ent_gale1
                                    A[S] = ent_gale2
                                    A[T] = int(B[4].strip())
                                    A[U] = V

                                if usarsoros:
                                    pesq = str(F) + H + str(G)
                                    if pesq in tmp:
                                        valid = False
                                    else:
                                        tmp.append(pesq)
                                        valid = True
                                else:
                                    valid = True
                                if valid:
                                    W.append(A)
                    line_count += 1

        WS = sorted(W, key=(lambda i: (i[O], i[J])))
        b = Y.dumps(WS)
    except Exception as e:
        try:
            print(e)
            raise Exception(Idioma.traducao('Layout inválido.\nLayout correto: ATIVO;DIA;HORARIO;DIRECAO;DURACAO'))
        finally:
            e = None
            del e

    return (
     cnt, b)


def geralistaMT4(arq, ent_valor1, ent_gale1, ent_gale2):
    W = []
    tmp = []
    cnt = 0
    line_count = 0
    b = None
    try:
        with open(arq) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            cnt = 0
            line_count = 0
            for B in csv_reader:
                if B:
                    try:
                        dthr = datetime.fromtimestamp(int(B[0]))
                        dthr = dthr + timedelta(seconds=5)
                        A = X()
                        F = '{:02d}'.format(int(dthr.hour))
                        G = '{:02d}'.format(int(dthr.minute))
                        I = '00'
                        cnt += 1
                        A[K] = int(cnt)
                        A[N] = remove_carespeciais(str(B[1]).strip())
                        A[O] = int(dthr.day)
                        A[J] = str(F) + H + str(G) + H + str(I)
                        A[P] = remove_carespeciais(str(B[2]).strip())
                        A[Q] = ent_valor1
                        A[R] = ent_gale1
                        A[S] = ent_gale2
                        A[T] = int(B[3].strip())
                        A[U] = V
                        valid = True
                        if roboCtrl.instance().robo.usarsoros:
                            pesq = str(F) + H + str(G)
                            if pesq in tmp:
                                valid = False
                            else:
                                tmp.append(pesq)
                                valid = True
                        else:
                            valid = True
                    except:
                        valid = False

                    if valid:
                        W.append(A)
                    else:
                        line_count += 1

        try:
            WS = sorted(W, key=(lambda i: (i[O], i[J])))
        except Exception as e:
            try:
                LogSys.save(str(e))
                WS = W
            finally:
                e = None
                del e

        b = Y.dumps(WS)
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e

    if line_count > 0:
        with open(arq, 'wb') as csv_file:
            writer = csv.writer(csv_file)
    return (
     cnt, b)


def geraSinalMT4(somasec, datahora, ativo, acao, duracao, ent_valor1, ent_gale1, ent_gale2):
    W = []
    tmp = []
    line_count = 0
    b = None
    try:
        try:
            dthr = datetime.fromtimestamp(int(datahora))
            dthr = dthr + timedelta(seconds=somasec)
            dthr = dthr + timedelta(seconds=(roboCtrl.instance().robo.delay))
            A = X()
            F = '{:02d}'.format(int(dthr.hour))
            G = '{:02d}'.format(int(dthr.minute))
            I = '{:02d}'.format(int(dthr.second))
            A[K] = 1
            A[N] = remove_carespeciais(str(ativo).strip())
            A[O] = int(dthr.day)
            A[J] = str(F) + H + str(G) + H + str(I)
            A[P] = remove_carespeciais(str(acao).strip())
            A[Q] = ent_valor1
            A[R] = ent_gale1
            A[S] = ent_gale2
            A[T] = int(duracao.strip())
            A[U] = V
            valid = True
        except Exception as e:
            try:
                valid = False
                LogSys.save(str(e))
            finally:
                e = None
                del e

        if valid:
            W.append(A)
        line_count += 1
        try:
            WS = sorted(W, key=(lambda i: (i[O], i[J])))
        except Exception as e:
            try:
                LogSys.save(str(e))
                WS = W
            finally:
                e = None
                del e

        b = Y.dumps(WS)
    except Exception as e:
        try:
            LogSys.save(str(e))
        finally:
            e = None
            del e

    return (
     line_count, b)