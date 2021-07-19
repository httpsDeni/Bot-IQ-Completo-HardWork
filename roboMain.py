import glob, os, sys, queue, webbrowser, PySimpleGUI as sg
from log.path import PathLogs
from personal import dencryptfile as Decryp
import models.Operation as E
import models.roboController as roboCtrl
from models.ThreadOperacion import *
import models.forecast as forecast
from services.getimglogo import *
from services.versaojobs import *
from services.utils import *
import services.robo as RoboIQ
from main.roboView import JobsView
from main.roboDownloadView import JobsViewDownload
from main.roboUtils import *
from main.roboExtras import *
obrigarTemplate = True
if obrigarTemplate:
    nomeApp = 'Robô'
else:
    nomeApp = 'Denis'
tema = 'Topanga'
lang = 'pt-br'
afiliado = 0
prime = False
template = None
for file in glob.glob('*.cfg'):
    template = Decryp.getTemplate(file)
    break

if template:
    try:
        afiliado = int(template['afiliado'])
        nomeApp = template['nomeApp']
        tema = template['tema']
        lang = template['lang']
        try:
            img_base64 = template['imagem']
        except:
            img_base64 = ''

        try:
            prime = True if template['prime'] == 1 else 0
        except:
            prime = False

    except:
        if obrigarTemplate:
            sys.exit(0)

elif obrigarTemplate:
    sys.exit(0)
Idioma.setlang(lang)
img_logo = None
versaoapp = '6.5'
if prime:
    versaoapp += ' Prime'
roboCtrl.instance().robo = RoboIQ(versaoapp)
roboCtrl.instance().robo.lang = lang
roboCtrl.instance().robo.prime = prime
roboCtrl.instance().robo.imgbase64 = img_base64
roboCtrl.instance().robo.afiliadocfg = afiliado
cf = roboCtrl.instance().robo.loadConfig()
roboCtrl.instance().robo.setConfig(cf)
roboCtrl.instance().view = JobsView(nomeApp, tema, versaoapp, img_logo, img_base64, afiliado)
roboCtrl.instance().robo.View = roboCtrl.instance().view
if str(roboCtrl.instance().robo.telegrantoken).strip() != '':
    from main.roboTelegram import *

def executeBot():
    if roboCtrl.instance().robo.botTG:
        roboCtrl.instance().robo.botTG.infinity_polling(True)


def main():
    global afiliado
    roboCtrl.instance().view.Show()
    roboCtrl.instance().view.janela['-tabprime-'].update(visible=prime)
    roboCtrl.instance().view.janela['entfixamt4'].update(visible=prime)
    roboCtrl.instance().view.janela['-frameopcao44-'].update(visible=(not prime))
    LeConfig()
    threadBot = ThreadOper(target=executeBot)
    threadBot.start()
    janelaDown = False
    while 1:
        event, values = roboCtrl.instance().view.janela.Read()
        if event == None:
            break
        else:
            if event == 'valinic':
                validarEditsNumeros('valinic', values)
            if event == 'delay':
                validarEditsNumeros('delay', values)
            if event == 'payout':
                validarEditsNumeros('payout', values)
            if event == 'qtdgale':
                validarEditsNumeros('qtdgale', values)
            if event == 'valor1':
                validarEditsNumeros('valor1', values)
            if event == 'gale1':
                validarEditsNumeros('gale1', values)
            if event == 'gale2':
                validarEditsNumeros('gale2', values)
            if event == 'percentsoros':
                validarEditsNumeros('percentsoros', values)
            if event == 'valorentsoros':
                validarEditsNumeros('valorentsoros', values)
            if event == 'nivelsoros':
                validarEditsNumeros('nivelsoros', values)
            if event == 'stopgain':
                validarEditsNumeros('stopgain', values)
            if event == 'stoploss':
                validarEditsNumeros('stoploss', values)
            if event == 'cicloval10':
                validarEditsNumeros('cicloval10', values)
            if event == 'cicloval11':
                validarEditsNumeros('cicloval11', values)
            if event == 'cicloval12':
                validarEditsNumeros('cicloval12', values)
            if event == 'cicloval20':
                validarEditsNumeros('cicloval20', values)
            if event == 'cicloval21':
                validarEditsNumeros('cicloval21', values)
            if event == 'cicloval22':
                validarEditsNumeros('cicloval22', values)
            if event == 'cicloval30':
                validarEditsNumeros('cicloval30', values)
            if event == 'cicloval31':
                validarEditsNumeros('cicloval31', values)
            if event == 'cicloval32':
                validarEditsNumeros('cicloval32', values)
            if event == 'telegranchatid':
                validarEditsNumeros('telegranchatid', values)
            if event == 'hrinicmt':
                validarEditsNumeros('hrinicmt', values)
            if event == 'mininicmt':
                validarEditsNumeros('mininicmt', values)
            if event == 'hrtermmt':
                validarEditsNumeros('hrtermmt', values)
            if event == 'mintermmt':
                validarEditsNumeros('mintermmt', values)
            if event == '-Iniciar-' and not roboCtrl.instance().view.appStarted:
                try:
                    valido = True
                    if values['email'] == '':
                        sg.popup((Idioma.traducao('Informe seu email.')), no_titlebar=True,
                          keep_on_top=True,
                          text_color='black',
                          background_color='#DFDDDD')
                        valido = False
                    if values['senha'] == '':
                        if valido:
                            sg.popup((Idioma.traducao('Informe sua senha.')), no_titlebar=True,
                              keep_on_top=True,
                              text_color='black',
                              background_color='#DFDDDD')
                            valido = False
                    if not checkEmail(values['email']):
                        if valido:
                            sg.popup_error((Idioma.traducao('Email inválido.')), no_titlebar=True,
                              keep_on_top=True,
                              text_color='black',
                              background_color='#DFDDDD')
                            valido = False
                    if roboCtrl.instance().robo.origemsinal == 0:
                        if not os.path.isfile(values['arqlista']):
                            if valido:
                                sg.popup((Idioma.traducao('Arquivo da lista não foi localizado.')), no_titlebar=True,
                                  keep_on_top=True,
                                  text_color='black',
                                  background_color='#DFDDDD')
                                valido = False
                        if valido:
                            GravaConfigTP(values['email'], values['contatipo'])
                            roboCtrl.instance().robo.senha = values['senha']
                            roboCtrl.instance().robo.arqLista = values['arqlista']
                            btn_Iniciar(event)
                except Exception as e:
                    try:
                        LogSys.save(str(e))
                    finally:
                        e = None
                        del e

            if event == '-Gravar-':
                try:
                    GravaConfig(values)
                    sg.popup((Idioma.traducao('Atenção')), (Idioma.traducao('Parâmetros gravados com sucesso!')), no_titlebar=True,
                      keep_on_top=True,
                      text_color='black',
                      background_color='#DFDDDD')
                except Exception as inst:
                    try:
                        sg.popup_error((str(inst)), no_titlebar=True,
                          keep_on_top=True,
                          text_color='black',
                          background_color='#DFDDDD')
                    finally:
                        inst = None
                        del inst

                if event == '-Ajuda-':
                    Leiame = Idioma.traducaoLeiame()
                    sg.popup_scrolled((Idioma.traducao('Leiame')), Leiame, size=(120,
                                                                                 20), font=('Helvetica',
                                                                                            8),
                      no_titlebar=True,
                      keep_on_top=True,
                      text_color='black',
                      background_color='#DFDDDD')
                if event == '-linktelegran1-':
                    webbrowser.open_new_tab('https://web.telegram.org/#/im?p=@RoboNotifyOB_Bot')
                if event == '-linktelegran2-':
                    webbrowser.open_new_tab('https://web.telegram.org/#/im?p=@BotFather')
                if event == '-linktelegranecho-':
                    webbrowser.open_new_tab('https://web.telegram.org/#/im?p=@chatid_echo_bot')
        if event == '-TABLE-':
            try:
                item = int(values['-TABLE-'][0])
                cancelitem = sg.popup_yes_no(('ID: ' + str(item + 1) + ' ' + Idioma.traducao('Cancelar este sinal?')), no_titlebar=True,
                  keep_on_top=True,
                  text_color='black',
                  background_color='#DFDDDD')
                if cancelitem == 'Yes':
                    cancelSinal(item)
            except:
                pass

            if event == '-Download-':
                if not janelaDown:
                    valido = True
                    if values['email'] == '':
                        sg.popup((Idioma.traducao('Informe seu email.')), no_titlebar=True,
                          keep_on_top=True,
                          text_color='black',
                          background_color='#DFDDDD')
                        valido = False
                    if not checkEmail(values['email']):
                        sg.popup_error((Idioma.traducao('Email inválido.')), no_titlebar=True,
                          keep_on_top=True,
                          text_color='black',
                          background_color='#DFDDDD')
                        valido = False
                    if valido:
                        roboCtrl.instance().robo.email = values['email']
                        if roboCtrl.instance().robo.VerificarLicenca(afiliado, 0, '1'):
                            janelaDown = True
                            viewDown = JobsViewDownload()
                            viewDown.Show()
                            roboCtrl.instance().robo.wslista.getLista(afiliado, roboCtrl.instance().robo.Lic.idtipolista)
                            viewDown.atualizaGrid(roboCtrl.instance().robo.wslista.lista)
                if janelaDown:
                    ev2, vals2 = viewDown.janela.read()
                    if ev2 is None or (ev2 == '-CancLista-'):
                        janelaDown = False
                        viewDown.janela.close()
                    if ev2 == '-ConfLista-':
                        janelaDown = False
                        try:
                            idx = int(vals2['-TABLELISTA-'][0])
                        except:
                            idx = -1
                            sg.popup_error((Idioma.traducao('Não foi selecionado nenhuma lista.')), no_titlebar=True,
                              keep_on_top=True,
                              text_color='black',
                              background_color='#DFDDDD')

                        if idx >= 0:
                            try:
                                nomelista = os.path.join(os.getcwd(), 'downloads')
                                PathLogs.create_dir(nomelista)
                                arq = roboCtrl.instance().robo.wslista.lista[idx]['id'] + '_' + roboCtrl.instance().robo.wslista.lista[idx]['data'] + '_' + roboCtrl.instance().robo.wslista.lista[idx]['nome'] + '.txt'
                                arq = arq.replace('-', '_')
                                arq = arq.replace(':', '_')
                                arq = arq.replace('/', '_')
                                arq = arq.replace(' ', '_')
                                nomelista = os.path.join(nomelista, arq)
                                arqlista = roboCtrl.instance().robo.wslista.getArquivo(int(roboCtrl.instance().robo.wslista.lista[idx]['id']))
                                if arqlista:
                                    with open(nomelista, 'wb') as f:
                                        f.write(arqlista)
                                    roboCtrl.instance().view.janela['arqlista'].update(value=nomelista)
                            except Exception as inst:
                                try:
                                    sg.popup_error((str(inst)), no_titlebar=True,
                                      keep_on_top=True,
                                      text_color='black',
                                      background_color='#DFDDDD')
                                finally:
                                    inst = None
                                    del inst

                        viewDown.janela.close()
                if event == '-AddHrOper-':
                    ok, msg = AddHorarioOperacaoMT(values)
                    if not ok:
                        sg.popup_error(msg, no_titlebar=True, keep_on_top=True, text_color='black', background_color='#DFDDDD')
                    if event == '-DelHrOper-':
                        DelHorarioOperacaoMT(values)
                    if not event in ('-Parar-', '-Fechar-'):
                        if sg.WIN_CLOSED:
                            pass
                    btn_Parar(event)
                    if not event == '-Fechar-':
                        if sg.WIN_CLOSED:
                            pass
                        break

    roboCtrl.instance().view.janela.close()
    del roboCtrl.instance().view.janela


if __name__ == '__main__':
    main()
# global lang ## Warning: Unused global
# global nomeApp ## Warning: Unused global
# global tema ## Warning: Unused global
# global versaoapp ## Warning: Unused global