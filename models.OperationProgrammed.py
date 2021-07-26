
import time
from datetime import datetime, timedelta
import json
import models.Operation as Operation
from iqoptionapi.expiration import *
S = 'call'
A = int
D = str

def getExpiration(dthr, duration):
    timestamp = date_to_timestamp(dthr)
    if duration == 1:
        exp, _ = get_expiration_time(timestamp, duration)
    else:
        now_date = datetime.fromtimestamp(timestamp) + timedelta(minutes=1, seconds=30)
        while True:
            if now_date.minute % duration == 0:
                if time.mktime(now_date.timetuple()) - timestamp > 30:
                    break
            now_date = now_date + timedelta(minutes=1)

        exp = time.mktime(now_date.timetuple())
    return datetime.fromtimestamp(exp)


def add_month(data):
    return data + timedelta(days=(data.max.day - data.day + 1))


def insOper(direcao, op_id, hour, minute, sec, pair, price, gale1, gale2, day, expiration, delay=0):
    G = datetime.now().year
    H = datetime.now().month
    while 1:
        try:
            O = datetime(G, H, A(day), A(hour), A(minute), A(sec))
            break
        except:
            day = datetime(G, H, 1, A(hour), A(minute), A(sec)).min.day
            O = datetime(G, H, A(day), A(hour), A(minute), A(sec))

    if O.date() < datetime.now().date():
        try:
            Dt = add_month(O)
            O = datetime(Dt.year, Dt.month, A(day), A(hour), A(minute), A(sec))
        except:
            O = datetime(G, H, A(day), A(hour), A(minute), A(sec))

        programmedHour = O - timedelta(seconds=delay)
        dhpre = O - timedelta(seconds=25)
        dhexpiration = getExpiration(O, expiration)
        dhexpiration = dhexpiration.replace(second=0, microsecond=0)
        dhexpirationgale1 = dhexpiration + timedelta(minutes=expiration)
        dhexpirationgale2 = dhexpirationgale1 + timedelta(minutes=expiration)
        dhexpirationgale1 = dhexpirationgale1.replace(second=0, microsecond=0)
        dhexpirationgale2 = dhexpirationgale2.replace(second=0, microsecond=0)
        hourOrig = dhexpiration - timedelta(minutes=expiration)
        hourOrig = hourOrig.replace(second=0, microsecond=0)
        return Operation(op_id, pair, expiration, direcao, price, gale1, gale2, hourOrig, programmedHour, dhexpiration, dhexpirationgale1, dhexpirationgale2, day, dhpre)


def G(operations, delay=0):
    F = []
    cnt = 0
    operacoes = json.loads(operations)
    for oper in operacoes:
        cnt += 1
        for A in oper:
            if A == 'ID':
                id = D(cnt)
            else:
                if A == 'Ativo':
                    ativo = D(oper[A]).replace('/', '').strip()
                if A == 'Horário':
                    hora = D(oper[A]).split(':')[0]
                    min = D(oper[A]).split(':')[1]
                    seg = D(oper[A]).split(':')[2]
                if A == 'Valor($)':
                    valor = D(oper[A]).strip()
                if A == 'Operação':
                    M = D(oper[A]).lower().strip()
                if A == 'Gale 1($)':
                    gale1 = D(oper[A]).strip()
                if A == 'Gale 2($)':
                    gale2 = D(oper[A]).strip()
                if A == 'Dia':
                    dia = D(oper[A]).strip()
            if A == 'Expiração(Min)':
                duracao = oper[A]

        if M == S or M == 'cal':
            io = insOper('call', id, hora, min, seg, ativo, valor, gale1, gale2, dia, duracao, delay)
        else:
            io = insOper('put', id, hora, min, seg, ativo, valor, gale1, gale2, dia, duracao, delay)
        F.append(io)

    return F
