import requests
from bs4 import BeautifulSoup
from datetime import date, datetime, timedelta
import models.roboController as roboCtrl
from models.ThreadOperacion import *

class Noticia:

    def __init__(self, hora, moeda, texto):
        self.hora = hora.strip() + ':00'
        self.moeda = moeda.upper().strip()
        self.texto = texto.strip()


def getNoticias():
    if datetime.now().isoweekday() > 0:
        if datetime.now().isoweekday() < 6:
            K = ThreadOper(target=WebNoticias, args=())
            roboCtrl.instance().add_listThread = K
            K.start()


def WebNoticias():
    try:
        data = []
        roboCtrl.instance().__noticias = []
        importacia = '3'
        if roboCtrl.instance().robo.touros2:
            importacia = '2,3'
        url = 'https://sslecal2.forexprostools.com?columns=exc_currency,exc_importance&importance=' + importacia
        url = url + '&countries=110,17,29,25,32,6,37,36,26,5,22,39,14,48,10,35,7,43,38,4,12,72&calType=day'
        if roboCtrl.instance().robo.lang == 'pt-br':
            url = url + '&timeZone=12&lang=12'
        response = requests.get(url, headers={'User-Agent': 'Mozilla'}, timeout=5)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            soup.prettify()
            table = soup.find_all(id='ecEventsTable')[0]
            linhas = table.find_all('tr')
            for lin in linhas:
                events = lin.find_all('td', class_='left event')
                if events:
                    times = lin.find_all('td', class_='first left time')
                    if not times:
                        times = lin.find_all('td', class_='center time')
                    flags = lin.find_all('td', class_='flagCur')
                    sents = lin.find_all('td', class_='sentiment')
                    if times:
                        if flags:
                            if sents:
                                if events:
                                    moe = flags[0].get_text().replace('&nbsp;', '').replace('\xa0 ', '')
                                    moe.strip()
                                    if moe != '':
                                        hor = times[0].get_text().strip()
                                        des = events[0].get_text().strip()
                                        item = [hor, moe, des]
                                        data.append(item)
                try:
                    roboCtrl.instance().add_noticias = Noticia(hor, moe, des)
                except:
                    pass

            roboCtrl.instance().dianoticias = datetime.now().date()
        roboCtrl.instance().view.janela['-TABLENOTICIAS-'].update(values=data)
    except:
        pass


def PesquisaNoticia(horario, ativo):
    TemNoticia = False
    noticia = None
    try:
        ativo = ativo.replace('-OTC', '')
        Moeda1 = str(ativo[:-3])
        Moeda2 = str(ativo[3:])
        Moeda1 = Moeda1.upper()
        Moeda2 = Moeda2.upper()
        for item in roboCtrl.instance().noticias:
            if item.moeda == Moeda1:
                if Moeda1 != '':
                    Dia = date.today()
                    hor = horario.split(':')[0]
                    min = horario.split(':')[1]
                    dataativo = datetime(Dia.year, Dia.month, Dia.day, int(hor), int(min), int('00'))
                    hor = item.hora.split(':')[0]
                    min = item.hora.split(':')[1]
                    data = datetime(Dia.year, Dia.month, Dia.day, int(hor), int(min), int('00'))
                    try:
                        minantes = int(roboCtrl.instance().robo.notminantes)
                    except:
                        minantes = 0

                    dataant = data - timedelta(minutes=minantes)
                    try:
                        minapos = int(roboCtrl.instance().robo.notminapos)
                    except:
                        minapos = 0

                    datapos = data + timedelta(minutes=minapos)
                    if dataativo >= dataant:
                        if dataativo <= datapos:
                            noticia = item
                            TemNoticia = True
                            break
            if item.moeda == Moeda2:
                if Moeda2 != '':
                    Dia = date.today()
                    hor = horario.split(':')[0]
                    min = horario.split(':')[1]
                    dataativo = datetime(Dia.year, Dia.month, Dia.day, int(hor), int(min), int('00'))
                    hor = item.hora.split(':')[0]
                    min = item.hora.split(':')[1]
                    data = datetime(Dia.year, Dia.month, Dia.day, int(hor), int(min), int('00'))
                    try:
                        minantes = int(roboCtrl.instance().robo.notminantes)
                    except:
                        minantes = 0

                    dataant = data - timedelta(minutes=minantes)
                    try:
                        minapos = int(roboCtrl.instance().robo.notminapos)
                    except:
                        minapos = 0

                    datapos = data + timedelta(minutes=minapos)
                    if dataativo >= dataant:
                        if dataativo <= datapos:
                            noticia = item
                            TemNoticia = True
                            break

    except:
        pass

    return (
     TemNoticia, noticia)