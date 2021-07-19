import time
from datetime import datetime, date, timedelta
import numpy as np
from talib import abstract
import connection.APIConnection as A

def getVelas(par, expiracao, candles):
    agora = datetime.now() - timedelta(minutes=expiracao)
    hora = datetime.timestamp(agora)
    indicadoresVela = A.instance().connection.get_candles(par, expiracao * 60, int(candles), hora)
    inputs = {'open':np.array([]), 
     'high':np.array([]), 
     'low':np.array([]), 
     'close':np.array([]), 
     'volume':np.array([])}
    for candles in indicadoresVela:
        inputs['open'] = np.append(inputs['open'], candles['open'])
        inputs['close'] = np.append(inputs['close'], candles['close'])
        inputs['high'] = np.append(inputs['high'], candles['max'])
        inputs['low'] = np.append(inputs['low'], candles['min'])
        inputs['volume'] = np.append(inputs['volume'], candles['volume'])

    return inputs


def gerarIndicadores(velaArray):
    momentumIndicatorsRED = 0
    momentumIndicatorsGREEN = 0
    overlapStudiesGREEN = 0
    overlapStudiesRED = 0
    overlapStudiesN = 0
    EMA5 = abstract.EMA(velaArray, timeperiod=5, price='close')
    SMA20 = abstract.SMA(velaArray, timeperiod=20, price='close')
    RSI14 = abstract.RSI(velaArray, timeperiod=14, price='close')
    info = ''
    if round(EMA5[(-10)], 6) > round(EMA5[(-1)], 6):
        info = info + ' EMA5: BAIXA'
        momentumIndicatorsRED += 1
    else:
        info = info + ' EMA5: ALTA'
        momentumIndicatorsGREEN += 1
    if round(SMA20[(-10)], 6) > round(SMA20[(-1)], 6):
        info = info + ' SMA20: BAIXA'
        momentumIndicatorsRED += 1
    else:
        info = info + ' SMA20: ALTA'
        momentumIndicatorsGREEN += 1
    if round(RSI14[(-1)], 6) > 70.0:
        info = info + ' RSI: VENDER'
        overlapStudiesRED += 1
    elif round(RSI14[(-1)], 6) < 30.0:
        info = info + ' RSI: COMPRAR'
        overlapStudiesGREEN += 1
    else:
        overlapStudiesN += 1
    TotalBaixa = momentumIndicatorsRED + overlapStudiesGREEN
    TotalAlta = momentumIndicatorsGREEN + overlapStudiesRED
    neutroTotal = overlapStudiesN
    if TotalBaixa > TotalAlta:
        return ('put', info)
    if TotalAlta > TotalBaixa:
        return ('call', info)
    return (
     '', info)


def EmaSma(velaArray):
    momentumIndicatorsRED = 0
    momentumIndicatorsGREEN = 0
    periodoEma = 5
    periodoSma = 20
    EMA5 = abstract.EMA(velaArray, timeperiod=periodoEma, price='close')
    SMA20 = abstract.SMA(velaArray, timeperiod=periodoSma, price='close')
    info = ''
    if round(EMA5[(-periodoEma)], 6) > round(EMA5[(-1)], 6):
        info = info + ' EMA5: BAIXA'
        momentumIndicatorsRED += 1
    else:
        info = info + ' EMA5: ALTA'
        momentumIndicatorsGREEN += 1
    if round(SMA20[(-periodoSma)], 6) > round(SMA20[(-1)], 6):
        info = info + ' SMA20: BAIXA'
        momentumIndicatorsRED += 1
    else:
        info = info + ' SMA20: ALTA'
        momentumIndicatorsGREEN += 1
    TotalBaixa = momentumIndicatorsRED
    TotalAlta = momentumIndicatorsGREEN
    if TotalBaixa > TotalAlta:
        return ('put', info)
    if TotalAlta > TotalBaixa:
        return ('call', info)
    return (
     '', info)


def Ema5Ema20(velaArray):
    momentumIndicatorsRED = 0
    momentumIndicatorsGREEN = 0
    periodoEma = 5
    periodoEma = 20
    EMA5 = abstract.EMA(velaArray, timeperiod=periodoEma, price='close')
    EMA20 = abstract.EMA(velaArray, timeperiod=periodoEma, price='close')
    info = ''
    if round(EMA5[(-periodoEma)], 6) > round(EMA5[(-1)], 6):
        info = info + ' EMA5: BAIXA'
        momentumIndicatorsRED += 1
    else:
        info = info + ' EMA5: ALTA'
        momentumIndicatorsGREEN += 1
    if round(EMA20[(-periodoEma)], 6) > round(EMA20[(-1)], 6):
        info = info + ' EMA20: BAIXA'
        momentumIndicatorsRED += 1
    else:
        info = info + ' EMA20: ALTA'
        momentumIndicatorsGREEN += 1
    TotalBaixa = momentumIndicatorsRED
    TotalAlta = momentumIndicatorsGREEN
    if TotalBaixa > TotalAlta:
        return ('put', info)
    if TotalAlta > TotalBaixa:
        return ('call', info)
    return (
     '', info)