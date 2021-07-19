import time
from datetime import datetime, date, timedelta
import connection.APIConnection as A
from main.roboUtils import *

def tendenciaCandles(ativo, expiracao, ticks: int):
    try:
        if ticks <= 0:
            ticks = 2
        doji = 0
        call = 0
        put = 0
        tot = 0
        dire = ''
        seq = ''
        agora = datetime.now() - timedelta(minutes=expiracao)
        hora = datetime.timestamp(agora)
        candles = A.instance().connection.get_candles(ativo, 60 * expiracao, int(ticks), hora)
        for candle in candles:
            tot += 1
            if candle['close'] > candle['open']:
                call += 1
                seq = seq + 'G'
            else:
                if candle['close'] < candle['open']:
                    put += 1
                    seq = seq + 'R'
                else:
                    doji += 1
                    seq = seq + 'C'

        pcall = 0
        pput = 0
        if call > 0:
            pcall = int(round(call / tot, 2) * 100)
        if put > 0:
            pput = int(round(put / tot, 2) * 100)
        if pcall >= 55:
            dire = 'call'
        elif pput >= 55:
            dire = 'put'
    except Exception as e:
        try:
            LogSys.save('Erro tendenciaCandles: {}', str(e))
        finally:
            e = None
            del e

    return (
     dire, seq, pcall, pput)


def getIndicadores(ativo: str, duracao: int):
    oscila_put = 0
    oscila_neu = 0
    oscila_call = 0
    medias_put = 0
    medias_neu = 0
    medias_call = 0
    pivots_put = 0
    pivots_neu = 0
    pivots_call = 0
    descr_ema = ''
    descr_sma = ''
    tendencia = ''
    descricao = ''
    try:
        data = A.instance().connection.get_technical_indicators(ativo)
        for item in data:
            if int(item['candle_size']) == duracao * 60:
                if str(item['group']).lower() == 'OSCILLATORS'.lower():
                    if str(item['name']).lower() == 'Relative Strength Index (14)'.lower() or (str(item['name']).lower() == 'Stochastic RSI Fast (3, 3, 14, 14)'.lower()):
                        if str(item['action']).lower() == 'sell':
                            oscila_put += 1
                        if str(item['action']).lower() == 'buy':
                            oscila_call += 1
                        if str(item['action']).lower() == 'hold':
                            oscila_neu += 1
                    if str(item['group']).lower() == 'MOVING AVERAGES'.lower():
                        if str(item['name']).lower() == 'Exponential Moving Average (5)'.lower():
                            if str(item['action']).lower() == 'sell':
                                descr_ema = 'EMA5: VENDER'
                                medias_put += 1
                            if str(item['action']).lower() == 'buy':
                                descr_ema = 'EMA5: COMPRAR'
                                medias_call += 1
                            if str(item['action']).lower() == 'hold':
                                descr_ema = 'EMA5: NEUTRO'
                                medias_neu += 1
                        if str(item['name']).lower() == 'Simple Moving Average (20)'.lower():
                            if str(item['action']).lower() == 'sell':
                                descr_sma = 'SMA20: VENDER'
                                medias_put += 1
                            if str(item['action']).lower() == 'buy':
                                descr_sma = 'SMA20: COMPRAR'
                                medias_call += 1
                            if str(item['action']).lower() == 'hold':
                                descr_sma = 'SMA20: NEUTRO'
                                medias_neu += 1
                    if str(item['group']).lower() == 'PIVOTS'.lower():
                        if str(item['action']).lower() == 'sell':
                            pivots_put += 1
                        elif str(item['action']).lower() == 'buy':
                            pivots_call += 1
                        if str(item['action']).lower() == 'hold':
                            pivots_neu += 1

        descricao = descr_ema + ' | ' + descr_sma
        if medias_call > medias_put:
            tendencia = 'call'
        elif medias_put > medias_call:
            tendencia = 'put'
    except:
        pass

    return (
     tendencia, descricao)