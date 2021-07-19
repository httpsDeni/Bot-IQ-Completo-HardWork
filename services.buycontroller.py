import decimal, time
from datetime import datetime, timedelta
from wrapt import synchronized as A
import models.Operation
import connection.APIConnection as APIConnection
from iqoptionapi.expiration import *

@A
def C(operation, valuecurrenc):
    O = operation
    status = False
    id = 0
    taxa = 0
    try:
        if O.typepair == 'D':
            status, id = APIConnection.instance().connection.buy_digital_spot_v2(O.pair, float(valuecurrenc), str(O.direction).lower(), int(O.expirationMode))
            if status:
                res = APIConnection.instance().connection.get_digital_position(id)
                orders = res['msg']['position']['orders']
                for order in orders:
                    if order['id'] == id:
                        taxa = order['instrument_strike']
                        break

        else:
            status, id, taxa = APIConnection.instance().connection.buy(float(valuecurrenc), O.pair, str(O.direction).lower(), int(O.expirationMode))
    except Exception as e:
        try:
            status = False
            id = 0
            taxa = 0
        finally:
            e = None
            del e

    if not isinstance(taxa, float):
        taxa = 0
    return (status, id, float(taxa))


@A
def D(idaction, typepair, dhend):
    status = False
    win = 0
    try:
        dhend = dhend + timedelta(seconds=15)
        if typepair == 'D':
            while True:
                status, win = APIConnection.instance().connection.check_win_digital_v2(idaction)
                if status:
                    break

        else:
            result = APIConnection.instance().connection.check_binary_order(idaction)
            status = result['result']
            try:
                win = round(float(result['profit_amount']) - float(result['amount']), 2)
            except:
                win = 0

    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e

    return (
     status, win)


@A
def getCandles(candle_ativo: str, candle_duracao: int, candle_ticks: int):
    data = []
    try:
        if candle_ticks > 1000:
            resultdiv = decimal.getcontext().divmod(candle_ticks, 1000)
            qtdefor = int(resultdiv[0])
            fracao = str(resultdiv[1])
            qtdesobrou = int(fracao)
            ANS = []
            errocnt = 0
            candle_ticks = 1000
            end_from_time = time.time()
            if qtdefor > 0:
                for i in range(qtdefor):
                    data = APIConnection.instance().connection.get_candles(candle_ativo, candle_duracao * 60, candle_ticks, end_from_time)
                    ANS = data + ANS
                    end_from_time = int(data[0]['from']) - 1

            if qtdesobrou > 0:
                candle_ticks = qtdesobrou
                data = APIConnection.instance().connection.get_candles(candle_ativo, candle_duracao * 60, candle_ticks, end_from_time)
                ANS = ANS + data
            data = ANS
        else:
            data = APIConnection.instance().connection.get_candles(candle_ativo, candle_duracao * 60, candle_ticks, time.time())
    except Exception as e:
        try:
            pass
        finally:
            e = None
            del e

    return data