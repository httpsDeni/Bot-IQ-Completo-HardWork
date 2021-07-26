import json, requests
from requests.auth import HTTPBasicAuth
import models.roboController as roboCtrl
from models.roboController import *
from services.utils import *
from main.roboUtils import *
import telebot

def getTelegran1():
    host = HOST_NAME
    service = 'SE1/gettelegran1'
    token = ''
    try:
        resp = requests.get((host + service), auth=(HTTPBasicAuth('xxx', 'xxx')))
        if resp.status_code == 200:
            resp = Cripto64(resp.content, True)
            data = json.loads(resp)
            token = data['token']
    except:
        pass

    return token


def enviarMsg(id, msg):
    if not id and msg or roboCtrl.instance().robo.telegranusar:
        try:
            if roboCtrl.instance().robo.botTG:
                roboCtrl.instance().robo.botTG.send_message(id, msg)
            else:
                if roboCtrl.instance().robo.telegramTOKENAviso == '':
                    roboCtrl.instance().robo.telegramTOKENAviso = getTelegran1()
                if roboCtrl.instance().robo.telegramTOKENAviso != '':
                    if not roboCtrl.instance().telegran1:
                        roboCtrl.instance().telegran1 = telebot.TeleBot((roboCtrl.instance().robo.telegramTOKENAviso), parse_mode='HTML')
                    roboCtrl.instance().telegran1.send_message(id, msg)
        except Exception as e:
            try:
                LogSys.show('Msg não foi enviada para o seu telegran... {0}'.format(str(e)))
            finally:
                e = None
                del e
