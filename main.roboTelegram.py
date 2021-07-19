import os, sys, time
from log.path import PathLogs
import models.roboController as roboCtrl
from services.utils import *
from main.roboUtils import *
from main.roboExtras import *
import telebot
from telebot import types
import emoji
if str(roboCtrl.instance().robo.telegrantoken).strip() != '':
    botTG = telebot.TeleBot((roboCtrl.instance().robo.telegrantoken), parse_mode='HTML')
    roboCtrl.instance().robo.botTG = botTG
else:
    roboCtrl.instance().robo.botTG = None
botAceitarDoc = False
commands = {'start': emoji.emojize(':bulb:', use_aliases=True) + ' ' + Idioma.traducao('Mostra as opções de comandos do robô')}
opc_iniciar = '▶ ' + Idioma.traducao('Iniciar as operações do robô')
opc_parar = '⏹ ' + Idioma.traducao('Parar as operações do robô')
opc_opcoes = emoji.emojize(':pencil:', use_aliases=True) + ' ' + Idioma.traducao('Configurar meu gerenciamento')
opc_placar = emoji.emojize(':dart:', use_aliases=True) + ' ' + Idioma.traducao('Resultado parcial')
opc_noticias = emoji.emojize(':calendar:', use_aliases=True) + ' ' + Idioma.traducao('Notícias de hoje')
menu_iniciar = types.ReplyKeyboardMarkup(one_time_keyboard=True)
menu_iniciar.add(opc_iniciar)
menu_iniciar.add(opc_parar)
menu_iniciar.add(opc_opcoes)
menu_iniciar.add(opc_placar)
menu_iniciar.add(opc_noticias)
opc_GERAL = '✔ ' + Idioma.traducao('Geral')
opc_NOTIC = '✔ ' + Idioma.traducao('Opç Notícias')
opc_TEND = '✔ ' + Idioma.traducao('Opç Tendência')
opc_SALDO = '✔ ' + Idioma.traducao('Saldo Inicial')
opc_ENTFIX = '✔ ' + Idioma.traducao('Entradas Fixas')
opc_SOROSG = '✔ ' + Idioma.traducao('Sorosgale')
opc_SOROS = '✔ ' + Idioma.traducao('Soros')
opc_CICLOS = '✔ ' + Idioma.traducao('Ciclos')
if roboCtrl.instance().robo.prime:
    opc_PRIME = emoji.emojize(':low_brightness:', use_aliases=True) + ' Config. PRIME'
else:
    opc_PRIME = emoji.emojize(':low_brightness:', use_aliases=True) + ' ' + Idioma.traducao('Origem Sinais')
opc_VOLTAR = emoji.emojize(':leftwards_arrow_with_hook:', use_aliases=True) + ' ' + Idioma.traducao('Menu Principal')
opc_VOLTAR2 = emoji.emojize(':leftwards_arrow_with_hook:', use_aliases=True) + ' ' + Idioma.traducao('Voltar')
prm_ORIGEM = '✔ ' + Idioma.traducao('Origem Sinais')
prm_HORAOP = '✔ ' + Idioma.traducao('Horários de Operação')
hrop_ADD = emoji.emojize(':heavy_plus_sign:', use_aliases=True) + ' ' + 'Inserir Horário'
hrop_DEL = emoji.emojize(':heavy_minus_sign:', use_aliases=True) + ' ' + 'Excluir Horário'
tipoconta = types.ReplyKeyboardMarkup(one_time_keyboard=True)
tipoconta.add(Idioma.traducao('Real'), Idioma.traducao('Treinamento'))
menu_opcoes = types.ReplyKeyboardMarkup(one_time_keyboard=True)
menu_opcoes.add(opc_GERAL, opc_NOTIC)
menu_opcoes.add(opc_TEND, opc_SALDO)
menu_opcoes.add(opc_ENTFIX, opc_CICLOS)
menu_opcoes.add(opc_SOROSG, opc_SOROS)
menu_opcoes.add(opc_PRIME)
menu_opcoes.add(opc_VOLTAR)
menu_prime = types.ReplyKeyboardMarkup(one_time_keyboard=True)
menu_prime.add(prm_ORIGEM)
if roboCtrl.instance().robo.prime:
    menu_prime.add(prm_HORAOP)
menu_prime.add(opc_VOLTAR2)
menu_prime_hora = types.ReplyKeyboardMarkup(one_time_keyboard=True)
menu_prime_hora.add(hrop_ADD)
menu_prime_hora.add(hrop_DEL)
menu_prime_hora.add(opc_VOLTAR2)
qst_sim_nao = types.ReplyKeyboardMarkup(one_time_keyboard=True)
qst_sim_nao.add(Idioma.traducao('Sim'), Idioma.traducao('Não'))
tipoger = types.ReplyKeyboardMarkup(one_time_keyboard=True)
tipoger.add(Idioma.traducao('Entradas Fixas'), 'SorosGale')
tipoger.add('Soros', Idioma.traducao('Ciclos'))
tipopriori = types.ReplyKeyboardMarkup(one_time_keyboard=True)
tipopriori.add(Idioma.traducao('Maior Payout'), Idioma.traducao('Digital'), Idioma.traducao('Binárias'), Idioma.traducao('Somente Digital'), Idioma.traducao('Somente Binárias'))
tipoespera = types.ReplyKeyboardMarkup(one_time_keyboard=True)
tipoespera.add(Idioma.traducao('Resultado por Taxas'), Idioma.traducao('Resultado Resp. IQ'))
tipotend = types.ReplyKeyboardMarkup(one_time_keyboard=True)
tipotend.add(Idioma.traducao('Quant. Velas'), Idioma.traducao('Usar EMA5 + EMA20'))
tipovalor = types.ReplyKeyboardMarkup(one_time_keyboard=True)
tipovalor.add(Idioma.traducao('Percentual'), Idioma.traducao('Valor'))
tipomodelo = types.ReplyKeyboardMarkup(one_time_keyboard=True)
tipomodelo.add(Idioma.traducao('Agressivo'), Idioma.traducao('Moderado'), Idioma.traducao('Conservador'))
origemsinal = types.ReplyKeyboardMarkup(one_time_keyboard=True)
if roboCtrl.instance().robo.prime:
    origemsinal.add(Idioma.traducao('Lista de Sinais'), 'MetaTrader', Idioma.traducao('Servidor Sinais'))
else:
    origemsinal.add(Idioma.traducao('Lista de Sinais'), Idioma.traducao('Servidor Sinais'))
hideBoard = types.ReplyKeyboardRemove()
tmp_cicloval10 = 0
tmp_cicloval11 = 0
tmp_cicloval12 = 0
tmp_cicloval20 = 0
tmp_cicloval21 = 0
tmp_cicloval22 = 0
tmp_cicloval30 = 0
tmp_cicloval31 = 0
tmp_cicloval32 = 0
tmp_prime_hrinic = ''
tmp_prime_hrterm = ''

def tratarErro(error):
    LogSys.send(Idioma.traducao('Ocorreu um erro...') + '\n' + str(error))
    roboCtrl.instance().robo.botTG = None
    botTG = telebot.TeleBot((roboCtrl.instance().robo.telegrantoken), parse_mode='HTML')
    roboCtrl.instance().robo.botTG = botTG


@botTG.message_handler(content_types=['document'])
def down_lista(message):
    global botAceitarDoc
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        if not roboCtrl.instance().robo.iniciado or botAceitarDoc:
            try:
                file_id = message.document.file_id
                file_info = botTG.get_file(file_id)
                downloaded_file = botTG.download_file(file_info.file_path)
                nomelista = os.path.join(os.getcwd(), 'downloads')
                PathLogs.create_dir(nomelista)
                nomelista = os.path.join(nomelista, message.document.file_name)
                if downloaded_file:
                    with open(nomelista, 'wb') as f:
                        f.write(downloaded_file)
                    f.close()
                    roboCtrl.instance().robo.arqLista = nomelista
                    roboCtrl.instance().view.janela['arqlista'].update(value=nomelista)
                    if btn_Iniciar('-Iniciar-'):
                        botTG.reply_to(message, (Idioma.traducao('Robô iniciado com sucesso!')), reply_markup=hideBoard)
                    else:
                        roboCtrl.instance().robo.senha = ''
                        cmd_menu_iniciar(message)
                        return
            except Exception as e:
                try:
                    tratarErro(e)
                finally:
                    e = None
                    del e


def iniciarRobo(message):
    try:
        contatipo = Idioma.traducao('Treinamento')
        if roboCtrl.instance().robo.contareal:
            contatipo = Idioma.traducao('Real')
        GravaConfigTP(roboCtrl.instance().robo.email, contatipo)
        if roboCtrl.instance().robo.origemsinal == 1 and roboCtrl.instance().robo.prime or roboCtrl.instance().robo.origemsinal == 2:
            if btn_Iniciar('-Iniciar-'):
                botTG.reply_to(message, (Idioma.traducao('Robô iniciado com sucesso!')), reply_markup=hideBoard)
            else:
                roboCtrl.instance().robo.senha = ''
                cmd_menu_iniciar(message)
                return
        else:
            listasignal = types.ReplyKeyboardMarkup(one_time_keyboard=True)
            if roboCtrl.instance().robo.VerificarLicenca(roboCtrl.instance().robo.afiliadocfg, 0, '1'):
                roboCtrl.instance().robo.wslista.getLista(roboCtrl.instance().robo.afiliadocfg, roboCtrl.instance().robo.Lic.idtipolista)
                for item in roboCtrl.instance().robo.wslista.lista:
                    listasignal.add(item['data'] + ' ' + item['nome'])

            listasignal.add(Idioma.traducao('Enviar manualmente'))
            msg = botTG.reply_to(message, (Idioma.traducao('Selecione:')), reply_markup=listasignal)
            botTG.register_next_step_handler(msg, cmd_iniciar_step5)
    except Exception as e:
        try:
            tratarErro(e)
        finally:
            e = None
            del e


def cmd_iniciar_step5(message):
    global botAceitarDoc
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Enviar manualmente'):
                botAceitarDoc = True
                botTG.send_message(roboCtrl.instance().robo.telegranchatid, Idioma.traducao('Envie sua lista de sinais (txt)'))
                return
            achouitem = False
            for item in roboCtrl.instance().robo.wslista.lista:
                if message.text == item['data'] + ' ' + item['nome']:
                    achouitem = True
                    nomelista = os.path.join(os.getcwd(), 'downloads')
                    PathLogs.create_dir(nomelista)
                    arq = item['id'] + '_' + item['data'] + '_' + item['nome'] + '.txt'
                    arq = arq.replace('-', '_')
                    arq = arq.replace(':', '_')
                    arq = arq.replace('/', '_')
                    arq = arq.replace(' ', '_')
                    nomelista = os.path.join(nomelista, arq)
                    arqlista = roboCtrl.instance().robo.wslista.getArquivo(int(item['id']))
                    if arqlista:
                        with open(nomelista, 'wb') as f:
                            f.write(arqlista)
                        f.close()
                        roboCtrl.instance().robo.arqLista = nomelista
                        roboCtrl.instance().view.janela['arqlista'].update(value=nomelista)
                        if btn_Iniciar('-Iniciar-'):
                            botTG.reply_to(message, Idioma.traducao('Robô iniciado com sucesso!'))
                        else:
                            roboCtrl.instance().robo.senha = ''
                            cmd_menu_iniciar(message)
                            return
                    break

            if not achouitem:
                botTG.send_message(roboCtrl.instance().robo.telegranchatid, Idioma.traducao('Tente novamente...'))
                iniciarRobo(message)
                return
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_iniciar_step4(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            roboCtrl.instance().robo.senha = message.text
            roboCtrl.instance().view.janela['senha'].update(roboCtrl.instance().robo.senha)
            iniciarRobo(message)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_iniciar_step3(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            roboCtrl.instance().robo.email = message.text
            roboCtrl.instance().view.janela['email'].update(roboCtrl.instance().robo.email)
            msg = botTG.reply_to(message, Idioma.traducao('Qual sua senha?'))
            botTG.register_next_step_handler(msg, cmd_iniciar_step4)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_iniciar_step2(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Não'):
                msg = botTG.reply_to(message, Idioma.traducao('Qual seu e-mail de login?'))
                botTG.register_next_step_handler(msg, cmd_iniciar_step3)
            elif str(roboCtrl.instance().robo.senha).strip() != '':
                iniciarRobo(message)
            else:
                msg = botTG.reply_to(message, Idioma.traducao('Qual sua senha?'))
                botTG.register_next_step_handler(msg, cmd_iniciar_step4)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_iniciar_step1(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Real'):
                roboCtrl.instance().robo.contareal = True
            elif message.text == Idioma.traducao('Treinamento'):
                roboCtrl.instance().robo.contareal = False
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=tipoconta)
                botTG.register_next_step_handler(msg, cmd_iniciar_step1)
                return
            if roboCtrl.instance().robo.contareal:
                roboCtrl.instance().view.janela['contatipo'].update(value=(Idioma.traducao('Real')))
            else:
                roboCtrl.instance().view.janela['contatipo'].update(value=(Idioma.traducao('Treinamento')))
            if str(roboCtrl.instance().robo.email).strip() != '':
                msg = botTG.reply_to(message, (Idioma.traducao('Continuar usando este e-mail?') + '\n' + roboCtrl.instance().robo.email), reply_markup=qst_sim_nao)
                botTG.register_next_step_handler(msg, cmd_iniciar_step2)
            else:
                msg = botTG.reply_to(message, Idioma.traducao('Qual seu e-mail de login?'))
                botTG.register_next_step_handler(msg, cmd_iniciar_step3)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_step2(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        botTG.reply_to(message, message.text)


def cmd_opcoes_geral_step4(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Maior Payout'):
                roboCtrl.instance().robo.priorid = 0
            elif message.text == Idioma.traducao('Digital'):
                roboCtrl.instance().robo.priorid = 1
            elif message.text == Idioma.traducao('Binárias'):
                roboCtrl.instance().robo.priorid = 2
            elif message.text == Idioma.traducao('Somente Digital'):
                roboCtrl.instance().robo.priorid = 3
            elif message.text == Idioma.traducao('Somente Binárias'):
                roboCtrl.instance().robo.priorid = 4
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=tipopriori)
                botTG.register_next_step_handler(msg, cmd_opcoes_geral_step4)
                return
            roboCtrl.instance().robo.saveConfig()
            msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_opcoes)
            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_geral_step3(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vdelay = message.text
            if not vdelay.isdigit():
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_opcoes_geral_step3)
                return
            roboCtrl.instance().robo.delay = vdelay
            roboCtrl.instance().view.janela['delay'].update(value=(roboCtrl.instance().robo.delay))
            msg = botTG.reply_to(message, (Idioma.traducao('Defina sua prioridade:')), reply_markup=tipopriori)
            botTG.register_next_step_handler(msg, cmd_opcoes_geral_step4)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_geral_step2(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Resultado por Taxas'):
                roboCtrl.instance().robo.esperarIQ = False
                roboCtrl.instance().view.janela['esperarIQ'].update(value=(Idioma.traducao('Resultado por Taxas')))
            elif message.text == Idioma.traducao('Resultado Resp. IQ'):
                roboCtrl.instance().robo.esperarIQ = True
                roboCtrl.instance().view.janela['esperarIQ'].update(value=(Idioma.traducao('Resultado Resp. IQ')))
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=tipoespera)
                botTG.register_next_step_handler(msg, cmd_opcoes_geral_step2)
                return
            msg = botTG.reply_to(message, Idioma.traducao('Defina o delay (seg)'))
            botTG.register_next_step_handler(msg, cmd_opcoes_geral_step3)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_geral_step1(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            roboCtrl.instance().robo.prestop = False if message.text == Idioma.traducao('Não') else True
            roboCtrl.instance().view.janela['prestop'].update(value=(roboCtrl.instance().robo.prestop))
            msg = botTG.reply_to(message, (Idioma.traducao('Aguardar por Resultado?')), reply_markup=tipoespera)
            botTG.register_next_step_handler(msg, cmd_opcoes_geral_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_geral(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Entradas Fixas'):
                roboCtrl.instance().robo.gerenciar = 0
                roboCtrl.instance().view.janela['gerenciar'].update(value=(Idioma.traducao('Entradas Fixas')))
            elif message.text == 'SorosGale':
                roboCtrl.instance().robo.gerenciar = 1
                roboCtrl.instance().view.janela['gerenciar'].update(value='SorosGale')
            elif message.text == 'Soros':
                roboCtrl.instance().robo.gerenciar = 2
                roboCtrl.instance().view.janela['gerenciar'].update(value='Soros')
            elif message.text == Idioma.traducao('Ciclos'):
                roboCtrl.instance().robo.gerenciar = 3
                roboCtrl.instance().view.janela['gerenciar'].update(value=(Idioma.traducao('Ciclos')))
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=tipoger)
                botTG.register_next_step_handler(msg, cmd_opcoes_geral)
                return
            msg = botTG.reply_to(message, (Idioma.traducao('Usar Pré Stop Loss') + '?'), reply_markup=qst_sim_nao)
            botTG.register_next_step_handler(msg, cmd_opcoes_geral_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_noticia_step4(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vmin = message.text
            if not vmin.isdigit():
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_opcoes_noticia_step4)
                return
            roboCtrl.instance().robo.notminapos = vmin
            roboCtrl.instance().view.janela['notminapos'].update(value=(roboCtrl.instance().robo.notminapos))
            roboCtrl.instance().robo.saveConfig()
            msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_opcoes)
            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_noticia_step3(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vmin = message.text
            if not vmin.isdigit():
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_opcoes_noticia_step3)
                return
            roboCtrl.instance().robo.notminantes = vmin
            roboCtrl.instance().view.janela['notminantes'].update(value=(roboCtrl.instance().robo.notminantes))
            msg = botTG.reply_to(message, Idioma.traducao('Minutos (Após)') + '?')
            botTG.register_next_step_handler(msg, cmd_opcoes_noticia_step4)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_noticia_step2(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            roboCtrl.instance().robo.touros2 = False if message.text == Idioma.traducao('Não') else True
            roboCtrl.instance().view.janela['touros2'].update(value=(roboCtrl.instance().robo.touros2))
            msg = botTG.reply_to(message, Idioma.traducao('Minutos (Antes)') + '?')
            botTG.register_next_step_handler(msg, cmd_opcoes_noticia_step3)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_noticia_step1(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            roboCtrl.instance().robo.naonoticia = False if message.text == Idioma.traducao('Não') else True
            roboCtrl.instance().view.janela['naonoticia'].update(value=(roboCtrl.instance().robo.naonoticia))
            msg = botTG.reply_to(message, (Idioma.traducao('Incluir Notícias 2 Touros') + '?'), reply_markup=qst_sim_nao)
            botTG.register_next_step_handler(msg, cmd_opcoes_noticia_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_tendencia_step3(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vqtde = message.text
            if not vqtde.isdigit():
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_opcoes_tendencia_step3)
                return
            roboCtrl.instance().robo.tendvelas = vqtde
            roboCtrl.instance().view.janela['tendvelas'].update(value=(roboCtrl.instance().robo.tendvelas))
            roboCtrl.instance().robo.saveConfig()
            msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_opcoes)
            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_tendencia_step2(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Quant. Velas'):
                roboCtrl.instance().robo.tendqtdvela = True
                roboCtrl.instance().robo.tendemasma = False
                roboCtrl.instance().view.janela['tendqtdvela'].update(value=(roboCtrl.instance().robo.tendqtdvela))
                roboCtrl.instance().view.janela['tendemasma'].update(value=(roboCtrl.instance().robo.tendemasma))
                msg = botTG.reply_to(message, Idioma.traducao('Informe a quantidade de velas:'))
                botTG.register_next_step_handler(msg, cmd_opcoes_tendencia_step3)
            elif message.text == Idioma.traducao('Usar EMA5 + EMA20'):
                roboCtrl.instance().robo.tendqtdvela = False
                roboCtrl.instance().robo.tendemasma = True
                roboCtrl.instance().view.janela['tendqtdvela'].update(value=(roboCtrl.instance().robo.tendqtdvela))
                roboCtrl.instance().view.janela['tendemasma'].update(value=(roboCtrl.instance().robo.tendemasma))
                roboCtrl.instance().robo.saveConfig()
                msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_opcoes)
                botTG.register_next_step_handler(msg, cmd_opcoes_step1)
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=tipotend)
                botTG.register_next_step_handler(msg, cmd_opcoes_tendencia_step2)
                return
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_tendencia_step1(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            roboCtrl.instance().robo.tendusar = False if message.text == Idioma.traducao('Não') else True
            roboCtrl.instance().view.janela['tendusar'].update(value=(roboCtrl.instance().robo.tendusar))
            msg = botTG.reply_to(message, (Idioma.traducao('Qual tipo de tendência vai usar?')), reply_markup=tipotend)
            botTG.register_next_step_handler(msg, cmd_opcoes_tendencia_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_saldo_step6(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            if vvalor == 0:
                msg = botTG.reply_to(message, Idioma.traducao('Valor do Stop Gain não pode ser zero.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            if vvalor > 100:
                if roboCtrl.instance().robo.tipostop == 'P':
                    msg = botTG.reply_to(message, Idioma.traducao('Valor do Stop Loss não pode ser maior do que 100%.'))
                    botTG.register_next_step_handler(msg, cmd_saldo_step5)
                    return
            if vvalor > roboCtrl.instance().robo.valorinicial:
                if roboCtrl.instance().robo.tipostop == 'V':
                    msg = botTG.reply_to(message, Idioma.traducao('Valor do Stop Loss não pode ser maior do que o Saldo Inicial.'))
                    botTG.register_next_step_handler(msg, cmd_saldo_step5)
                    return
            roboCtrl.instance().robo.stoploss = vvalor
            roboCtrl.instance().view.janela['stoploss'].update(value=(roboCtrl.instance().robo.stoploss))
            roboCtrl.instance().robo.saveConfig()
            msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_opcoes)
            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_saldo_step5(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            if vvalor == 0:
                msg = botTG.reply_to(message, Idioma.traducao('Valor do Stop Gain não pode ser zero.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            roboCtrl.instance().robo.stopgain = vvalor
            roboCtrl.instance().view.janela['stopgain'].update(value=(roboCtrl.instance().robo.stopgain))
            msg = botTG.reply_to(message, Idioma.traducao('Informe seu Stop Loss:'))
            botTG.register_next_step_handler(msg, cmd_saldo_step6)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_saldo_step4(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Percentual'):
                roboCtrl.instance().robo.tipostop = 'P'
                roboCtrl.instance().view.janela['tipostop'].update(value=(Idioma.traducao('Percentual')))
            elif message.text == Idioma.traducao('Valor'):
                roboCtrl.instance().robo.tipostop = 'V'
                roboCtrl.instance().view.janela['tipostop'].update(value=(Idioma.traducao('Valor')))
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=tipovalor)
                botTG.register_next_step_handler(msg, cmd_saldo_step4)
                return
            msg = botTG.reply_to(message, Idioma.traducao('Informe seu Stop Gain:'))
            botTG.register_next_step_handler(msg, cmd_saldo_step5)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_saldo_step3(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vvalor = message.text
            if not vvalor.isdigit():
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step3)
                return
            roboCtrl.instance().robo.qtdgales = vvalor
            roboCtrl.instance().view.janela['qtdgale'].update(value=(roboCtrl.instance().robo.qtdgales))
            msg = botTG.reply_to(message, (Idioma.traducao('Selecione o Tipo de Stop:')), reply_markup=tipovalor)
            botTG.register_next_step_handler(msg, cmd_saldo_step4)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_saldo_step2(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vvalor = message.text
            if not vvalor.isdigit():
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step2)
                return
            if vvalor == 0:
                msg = botTG.reply_to(message, Idioma.traducao('Payout não pode ser zero.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step2)
                return
            roboCtrl.instance().robo.payoutmin = vvalor
            roboCtrl.instance().view.janela['payout'].update(value=(roboCtrl.instance().robo.payoutmin))
            msg = botTG.reply_to(message, Idioma.traducao('Quantidade de Gales:'))
            botTG.register_next_step_handler(msg, cmd_saldo_step3)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_saldo_step1(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            if vvalor == 0:
                msg = botTG.reply_to(message, Idioma.traducao('Saldo Inicial não pode ser zero.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step1)
                return
            roboCtrl.instance().robo.valorinicial = vvalor
            roboCtrl.instance().view.janela['valinic'].update(value=(roboCtrl.instance().robo.valorinicial))
            msg = botTG.reply_to(message, Idioma.traducao('Payout Mínimo %'))
            botTG.register_next_step_handler(msg, cmd_saldo_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_entfixa_step4(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            roboCtrl.instance().robo.ent_gale2 = vvalor
            roboCtrl.instance().view.janela['gale2'].update(value=(roboCtrl.instance().robo.ent_gale2))
            roboCtrl.instance().robo.saveConfig()
            msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_opcoes)
            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_entfixa_step3(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            roboCtrl.instance().robo.ent_gale1 = vvalor
            roboCtrl.instance().view.janela['gale1'].update(value=(roboCtrl.instance().robo.ent_gale1))
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Gale 2'))
            botTG.register_next_step_handler(msg, cmd_entfixa_step4)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_entfixa_step2(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            if vvalor == 0:
                if roboCtrl.instance().robo.gerenciar == 0:
                    msg = botTG.reply_to(message, Idioma.traducao('o valor da 1ª Entrada % não pode ser zero.'))
                    botTG.register_next_step_handler(msg, cmd_entfixa_step2)
                    return
            roboCtrl.instance().robo.ent_valor1 = vvalor
            roboCtrl.instance().view.janela['valor1'].update(value=(roboCtrl.instance().robo.ent_valor1))
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Gale 1'))
            botTG.register_next_step_handler(msg, cmd_entfixa_step3)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_entfixa_step1(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Percentual'):
                roboCtrl.instance().robo.ent_tipo = 'P'
                roboCtrl.instance().view.janela['percent'].update(value=(Idioma.traducao('Percentual')))
            elif message.text == Idioma.traducao('Valor'):
                roboCtrl.instance().robo.ent_tipo = 'V'
                roboCtrl.instance().view.janela['percent'].update(value=(Idioma.traducao('Valor')))
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=tipovalor)
                botTG.register_next_step_handler(msg, cmd_entfixa_step1)
                return
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor da 1ª Entrada:'))
            botTG.register_next_step_handler(msg, cmd_entfixa_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_soros_step3(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            if vvalor == 0:
                if roboCtrl.instance().robo.gerenciar == 2:
                    msg = botTG.reply_to(message, Idioma.traducao('o valor do Nível não pode ser zero.'))
                    botTG.register_next_step_handler(msg, cmd_soros_step3)
                    return
            roboCtrl.instance().robo.nivelsoros = vvalor
            roboCtrl.instance().view.janela['nivelsoros'].update(value=(roboCtrl.instance().robo.nivelsoros))
            roboCtrl.instance().robo.saveConfig()
            msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_opcoes)
            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_soros_step2(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            if vvalor == 0:
                if roboCtrl.instance().robo.gerenciar == 2:
                    msg = botTG.reply_to(message, Idioma.traducao('o valor da 1ª Entrada % não pode ser zero.'))
                    botTG.register_next_step_handler(msg, cmd_soros_step2)
                    return
            roboCtrl.instance().robo.valorentsoros = vvalor
            roboCtrl.instance().view.janela['valorentsoros'].update(value=(roboCtrl.instance().robo.valorentsoros))
            msg = botTG.reply_to(message, Idioma.traducao('Informe o nível:'))
            botTG.register_next_step_handler(msg, cmd_soros_step3)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_soros_step1(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Percentual'):
                roboCtrl.instance().robo.tipovalsoros = 'P'
                roboCtrl.instance().view.janela['tipovalsoros'].update(value=(Idioma.traducao('Percentual')))
            elif message.text == Idioma.traducao('Valor'):
                roboCtrl.instance().robo.tipovalsoros = 'V'
                roboCtrl.instance().view.janela['tipovalsoros'].update(value=(Idioma.traducao('Valor')))
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=tipovalor)
                botTG.register_next_step_handler(msg, cmd_soros_step1)
                return
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor da 1ª Entrada:'))
            botTG.register_next_step_handler(msg, cmd_soros_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_sorosgale_step2(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Agressivo'):
                roboCtrl.instance().robo.modelo = 'A'
                roboCtrl.instance().view.janela['modelo'].update(value=(Idioma.traducao('Agressivo')))
            elif message.text == Idioma.traducao('Moderado'):
                roboCtrl.instance().robo.modelo = 'M'
                roboCtrl.instance().view.janela['modelo'].update(value=(Idioma.traducao('Moderado')))
            elif message.text == Idioma.traducao('Conservador'):
                roboCtrl.instance().robo.modelo = 'C'
                roboCtrl.instance().view.janela['modelo'].update(value=(Idioma.traducao('Conservador')))
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=tipomodelo)
                botTG.register_next_step_handler(msg, cmd_sorosgale_step2)
                return
            roboCtrl.instance().robo.saveConfig()
            msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_opcoes)
            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_sorosgale_step1(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            if vvalor == 0:
                if roboCtrl.instance().robo.gerenciar == 1:
                    msg = botTG.reply_to(message, Idioma.traducao('o valor da 1ª Entrada % não pode ser zero.'))
                    botTG.register_next_step_handler(msg, cmd_sorosgale_step1)
                    return
            roboCtrl.instance().robo.percent = vvalor
            roboCtrl.instance().view.janela['percentsoros'].update(value=(roboCtrl.instance().robo.percent))
            msg = botTG.reply_to(message, (Idioma.traducao('Qual Modelo?')), reply_markup=tipomodelo)
            botTG.register_next_step_handler(msg, cmd_sorosgale_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_ciclos_c3_step3(message):
    global tmp_cicloval10
    global tmp_cicloval11
    global tmp_cicloval12
    global tmp_cicloval20
    global tmp_cicloval21
    global tmp_cicloval22
    global tmp_cicloval30
    global tmp_cicloval31
    global tmp_cicloval32
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_ciclos_c3_step3)
                return
            tmp_cicloval32 = vvalor
            if roboCtrl.instance().robo.gerenciar == 3:
                if tmp_cicloval10 + tmp_cicloval11 + tmp_cicloval12 + tmp_cicloval20 + tmp_cicloval21 + tmp_cicloval22 + tmp_cicloval30 + tmp_cicloval31 + tmp_cicloval32 == 0:
                    msg = botTG.reply_to(message, (Idioma.traducao('Ciclos, nenhum valor foi digitado.')), reply_markup=menu_opcoes)
                    botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                    return
            if not roboCtrl.instance().robo.gerenciar == 3 or roboCtrl.instance().robo.qtdgales == 0:
                if tmp_cicloval10 == 0 and not tmp_cicloval11 > 0:
                    if tmp_cicloval11 == 0 and not tmp_cicloval12 > 0:
                        if not tmp_cicloval12 == 0 or tmp_cicloval20 > 0:
                            msg = botTG.reply_to(message, (Idioma.traducao('Ciclos, valor do ciclo 1 inválido.')), reply_markup=menu_opcoes)
                            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                            return
                        if tmp_cicloval20 == 0 and not tmp_cicloval21 > 0:
                            if tmp_cicloval21 == 0 and not tmp_cicloval22 > 0:
                                if not tmp_cicloval22 == 0 or tmp_cicloval30 > 0:
                                    msg = botTG.reply_to(message, (Idioma.traducao('Ciclos, valor do ciclo 2 inválido.')), reply_markup=menu_opcoes)
                                    botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                                    return
                                if tmp_cicloval30 == 0 and not tmp_cicloval31 > 0:
                                    if not tmp_cicloval31 == 0 or tmp_cicloval32 > 0:
                                        msg = botTG.reply_to(message, (Idioma.traducao('Ciclos, valor do ciclo 3 inválido.')), reply_markup=menu_opcoes)
                                        botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                                        return
            if roboCtrl.instance().robo.gerenciar == 3:
                if roboCtrl.instance().robo.qtdgales == 1:
                    if tmp_cicloval10 > 0 and not tmp_cicloval11 == 0:
                        if tmp_cicloval10 == 0 and tmp_cicloval11 > 0 or tmp_cicloval12 > 0:
                            msg = botTG.reply_to(message, (Idioma.traducao('Ciclos, valor do ciclo 1 inválido.')), reply_markup=menu_opcoes)
                            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                            return
                        if tmp_cicloval20 > 0 and not tmp_cicloval21 == 0:
                            if tmp_cicloval20 == 0 and tmp_cicloval21 > 0 or tmp_cicloval22 > 0:
                                msg = botTG.reply_to(message, (Idioma.traducao('Ciclos, valor do ciclo 2 inválido.')), reply_markup=menu_opcoes)
                                botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                                return
                            if tmp_cicloval30 > 0 and not tmp_cicloval31 == 0:
                                if tmp_cicloval30 == 0 and tmp_cicloval31 > 0 or tmp_cicloval32 > 0:
                                    msg = botTG.reply_to(message, (Idioma.traducao('Ciclos, valor do ciclo 3 inválido.')), reply_markup=menu_opcoes)
                                    botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                                    return
                            if not roboCtrl.instance().robo.gerenciar == 3 or roboCtrl.instance().robo.qtdgales == 2:
                                if tmp_cicloval10 > 0:
                                    if tmp_cicloval11 == 0 or (tmp_cicloval12 == 0):
                                        msg = botTG.reply_to(message, (Idioma.traducao('Ciclos, valor do ciclo 1 inválido.')), reply_markup=menu_opcoes)
                                        botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                                        return
                                    if tmp_cicloval20 > 0:
                                        if tmp_cicloval21 == 0 or (tmp_cicloval22 == 0):
                                            msg = botTG.reply_to(message, (Idioma.traducao('Ciclos, valor do ciclo 2 inválido.')), reply_markup=menu_opcoes)
                                            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                                            return
                                    if tmp_cicloval30 > 0:
                                        if tmp_cicloval31 == 0 or tmp_cicloval32 == 0:
                                            msg = botTG.reply_to(message, (Idioma.traducao('Ciclos, valor do ciclo 3 inválido.')), reply_markup=menu_opcoes)
                                            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                                            return
            roboCtrl.instance().robo.cicloval10 = tmp_cicloval10
            roboCtrl.instance().robo.cicloval11 = tmp_cicloval11
            roboCtrl.instance().robo.cicloval12 = tmp_cicloval12
            roboCtrl.instance().robo.cicloval20 = tmp_cicloval20
            roboCtrl.instance().robo.cicloval21 = tmp_cicloval21
            roboCtrl.instance().robo.cicloval22 = tmp_cicloval22
            roboCtrl.instance().robo.cicloval30 = tmp_cicloval30
            roboCtrl.instance().robo.cicloval31 = tmp_cicloval31
            roboCtrl.instance().robo.cicloval32 = tmp_cicloval32
            roboCtrl.instance().view.janela['cicloval10'].update(value=(roboCtrl.instance().robo.cicloval10))
            roboCtrl.instance().view.janela['cicloval11'].update(value=(roboCtrl.instance().robo.cicloval11))
            roboCtrl.instance().view.janela['cicloval12'].update(value=(roboCtrl.instance().robo.cicloval12))
            roboCtrl.instance().view.janela['cicloval20'].update(value=(roboCtrl.instance().robo.cicloval20))
            roboCtrl.instance().view.janela['cicloval21'].update(value=(roboCtrl.instance().robo.cicloval21))
            roboCtrl.instance().view.janela['cicloval22'].update(value=(roboCtrl.instance().robo.cicloval22))
            roboCtrl.instance().view.janela['cicloval30'].update(value=(roboCtrl.instance().robo.cicloval30))
            roboCtrl.instance().view.janela['cicloval31'].update(value=(roboCtrl.instance().robo.cicloval31))
            roboCtrl.instance().view.janela['cicloval32'].update(value=(roboCtrl.instance().robo.cicloval32))
            roboCtrl.instance().robo.saveConfig()
            msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_opcoes)
            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_ciclos_c3_step2(message):
    global tmp_cicloval31
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            tmp_cicloval31 = vvalor
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Ciclo C-{} ({}º Coluna):').format(3, 3))
            botTG.register_next_step_handler(msg, cmd_ciclos_c3_step3)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_ciclos_c3_step1(message):
    global tmp_cicloval30
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            tmp_cicloval30 = vvalor
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Ciclo C-{} ({}º Coluna):').format(3, 2))
            botTG.register_next_step_handler(msg, cmd_ciclos_c3_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_ciclos_c2_step3(message):
    global tmp_cicloval22
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            tmp_cicloval22 = vvalor
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Ciclo C-{} ({}º Coluna):').format(3, 1))
            botTG.register_next_step_handler(msg, cmd_ciclos_c3_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_ciclos_c2_step2(message):
    global tmp_cicloval21
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            tmp_cicloval21 = vvalor
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Ciclo C-{} ({}º Coluna):').format(2, 3))
            botTG.register_next_step_handler(msg, cmd_ciclos_c2_step3)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_ciclos_c2_step1(message):
    global tmp_cicloval20
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            tmp_cicloval20 = vvalor
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Ciclo C-{} ({}º Coluna):').format(2, 2))
            botTG.register_next_step_handler(msg, cmd_ciclos_c2_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_ciclos_c1_step3(message):
    global tmp_cicloval12
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            tmp_cicloval12 = vvalor
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Ciclo C-{} ({}º Coluna):').format(2, 1))
            botTG.register_next_step_handler(msg, cmd_ciclos_c2_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_ciclos_c1_step2(message):
    global tmp_cicloval11
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            tmp_cicloval11 = vvalor
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Ciclo C-{} ({}º Coluna):').format(1, 3))
            botTG.register_next_step_handler(msg, cmd_ciclos_c1_step3)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_ciclos_c1_step1(message):
    global tmp_cicloval10
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vret, vvalor = isFloat(message.text)
            if not vret:
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_saldo_step5)
                return
            tmp_cicloval10 = vvalor
            msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Ciclo C-{} ({}º Coluna):').format(1, 2))
            botTG.register_next_step_handler(msg, cmd_ciclos_c1_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_prime_add_hora_step3(message):
    global tmp_prime_hrinic
    global tmp_prime_hrterm
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Sim'):
                tmp_prime_hrinic = ''
                tmp_prime_hrterm = ''
                msg = botTG.reply_to(message, Idioma.traducao('Informe o Horário de Início (HH:MM)'))
                botTG.register_next_step_handler(msg, cmd_prime_add_hora_step1)
            else:
                cmd_menu_iniciar(message)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_prime_add_hora_step2(message):
    global tmp_prime_hrterm
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if not isTimeFormat(message.text):
                botTG.send_message(message.chat.id, Idioma.traducao('Horário de término inválido'))
                msg = botTG.reply_to(message, Idioma.traducao('Informe o Horário de Término (HH:MM)'))
                botTG.register_next_step_handler(msg, cmd_prime_add_hora_step2)
                return
            tmp_prime_hrterm = message.text + ':00'
            ret, retmsg = AddHorarioOperacao(datetime.strptime(tmp_prime_hrinic, '%H:%M:%S'), datetime.strptime(tmp_prime_hrterm, '%H:%M:%S'))
            if not ret:
                msg = botTG.reply_to(message, retmsg + '\n' + Idioma.traducao('Informe o Horário de Início (HH:MM)'))
                botTG.register_next_step_handler(msg, cmd_prime_add_hora_step1)
            else:
                roboCtrl.instance().robo.saveConfig()
                botTG.send_message(message.chat.id, Idioma.traducao('Parâmetros salvo com sucesso!'))
                msg = botTG.reply_to(message, (Idioma.traducao('Deseja inserir mais algum horário de operação?')), reply_markup=qst_sim_nao)
                botTG.register_next_step_handler(msg, cmd_prime_add_hora_step3)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_prime_add_hora_step1(message):
    global tmp_prime_hrinic
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if not isTimeFormat(message.text):
                botTG.send_message(message.chat.id, Idioma.traducao('Horário de início inválido'))
                msg = botTG.reply_to(message, Idioma.traducao('Informe o Horário de Início (HH:MM)'))
                botTG.register_next_step_handler(msg, cmd_prime_add_hora_step1)
            else:
                tmp_prime_hrinic = message.text + ':00'
                msg = botTG.reply_to(message, Idioma.traducao('Informe o Horário de Término (HH:MM)'))
                botTG.register_next_step_handler(msg, cmd_prime_add_hora_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_prime_step2(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            vdelay = message.text
            if not vdelay.isdigit():
                msg = botTG.reply_to(message, Idioma.traducao('Valor inválido, somente números serão válidos.'))
                botTG.register_next_step_handler(msg, cmd_prime_step2)
                return
            roboCtrl.instance().robo.maxdelaymt4 = vdelay
            roboCtrl.instance().view.janela['maxdelaymt4'].update(value=(roboCtrl.instance().robo.maxdelaymt4))
            roboCtrl.instance().robo.saveConfig()
            msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_opcoes)
            botTG.register_next_step_handler(msg, cmd_opcoes_step1)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_prime_step1(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == Idioma.traducao('Lista de Sinais'):
                roboCtrl.instance().robo.origemsinal = 0
                roboCtrl.instance().view.janela['origemsinal'].update(value=(Idioma.traducao('Lista de Sinais')))
            elif message.text == 'MetaTrader':
                roboCtrl.instance().robo.origemsinal = 1
                roboCtrl.instance().view.janela['origemsinal'].update(value='MetaTrader')
            elif message.text == Idioma.traducao('Servidor Sinais'):
                roboCtrl.instance().robo.origemsinal = 2
                roboCtrl.instance().view.janela['origemsinal'].update(value=(Idioma.traducao('Servidor Sinais')))
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=origemsinal)
                botTG.register_next_step_handler(msg, cmd_prime_step1)
                return
            msg = botTG.reply_to(message, Idioma.traducao('Informe o Máx. Delay (seg):'))
            botTG.register_next_step_handler(msg, cmd_prime_step2)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_prime_del_hora_step1(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text != '':
                excluido = False
                for itemhr in roboCtrl.instance().robo.listahoraoperacao:
                    if message.text == itemhr:
                        roboCtrl.instance().robo.listahoraoperacao.remove(itemhr)
                        excluido = True
                        break

            if excluido:
                roboCtrl.instance().robo.saveConfig()
                msg = botTG.reply_to(message, (Idioma.traducao('Parâmetros salvo com sucesso!')), reply_markup=menu_prime_hora)
                botTG.register_next_step_handler(msg, cmd_prime_hora)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_prime_hora(message):
    global tmp_prime_hrinic
    global tmp_prime_hrterm
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == hrop_ADD:
                tmp_prime_hrinic = ''
                tmp_prime_hrterm = ''
                msg = botTG.reply_to(message, Idioma.traducao('Informe o Horário de Início (HH:MM)'))
                botTG.register_next_step_handler(msg, cmd_prime_add_hora_step1)
            elif message.text == hrop_DEL:
                if roboCtrl.instance().robo.listahoraoperacao:
                    listahoras = types.ReplyKeyboardMarkup(one_time_keyboard=True)
                    for itemhr in roboCtrl.instance().robo.listahoraoperacao:
                        listahoras.add(itemhr)

                    msg = botTG.reply_to(message, (Idioma.traducao('Excluir o horário selecionado ?')), reply_markup=listahoras)
                    botTG.register_next_step_handler(msg, cmd_prime_del_hora_step1)
                else:
                    msg = botTG.reply_to(message, (Idioma.traducao('Nenhum horário foi encontrado')), reply_markup=menu_prime_hora)
                    botTG.register_next_step_handler(msg, cmd_prime_hora)
            elif message.text == opc_VOLTAR2:
                msg = botTG.reply_to(message, (Idioma.traducao('Selecione:')), reply_markup=menu_prime)
                botTG.register_next_step_handler(msg, cmd_prime_submenu)
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=menu_prime_hora)
                botTG.register_next_step_handler(msg, cmd_prime_hora)
                return
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_prime_submenu(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == '/start':
                cmd_menu_iniciar(message)
                return
            if message.text == prm_ORIGEM:
                msg = botTG.reply_to(message, (Idioma.traducao('Selecione a Origem dos Sinais:')), reply_markup=origemsinal)
                botTG.register_next_step_handler(msg, cmd_prime_step1)
            elif message.text == prm_HORAOP:
                msg = botTG.reply_to(message, (Idioma.traducao('Selecione:')), reply_markup=menu_prime_hora)
                botTG.register_next_step_handler(msg, cmd_prime_hora)
            elif message.text == opc_VOLTAR2:
                msg = botTG.reply_to(message, (Idioma.traducao('Selecione:')), reply_markup=menu_opcoes)
                botTG.register_next_step_handler(msg, cmd_opcoes_step1)
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=menu_prime)
                botTG.register_next_step_handler(msg, cmd_prime_submenu)
                return
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_opcoes_step1(message):
    global tmp_cicloval10
    global tmp_cicloval11
    global tmp_cicloval12
    global tmp_cicloval20
    global tmp_cicloval21
    global tmp_cicloval22
    global tmp_cicloval30
    global tmp_cicloval31
    global tmp_cicloval32
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        if not roboCtrl.instance().robo.iniciado:
            try:
                if message.text == '/start':
                    cmd_menu_iniciar(message)
                    return
                if message.text == opc_GERAL:
                    msg = botTG.reply_to(message, (Idioma.traducao('Vai usar qual gerenciamento?')), reply_markup=tipoger)
                    botTG.register_next_step_handler(msg, cmd_opcoes_geral)
                elif message.text == opc_NOTIC:
                    msg = botTG.reply_to(message, (Idioma.traducao('Não Operar em Notícias') + '?'), reply_markup=qst_sim_nao)
                    botTG.register_next_step_handler(msg, cmd_opcoes_noticia_step1)
                elif message.text == opc_TEND:
                    msg = botTG.reply_to(message, (Idioma.traducao('Não Operar Contra Tendência') + '?'), reply_markup=qst_sim_nao)
                    botTG.register_next_step_handler(msg, cmd_opcoes_tendencia_step1)
                elif message.text == opc_SALDO:
                    msg = botTG.reply_to(message, Idioma.traducao('Informe o Saldo Inicial:'))
                    botTG.register_next_step_handler(msg, cmd_saldo_step1)
                elif message.text == opc_ENTFIX:
                    if roboCtrl.instance().robo.gerenciar != 0:
                        msg = botTG.reply_to(message, (Idioma.traducao('Seu gerenciamento não é <b>{}</b>, configure ele primeiro.').format('[ENTRADA FIXA]')), reply_markup=menu_opcoes)
                        botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                        return
                    msg = botTG.reply_to(message, (Idioma.traducao('Qual Tipo de Valor da Entrada Fixa?')), reply_markup=tipovalor)
                    botTG.register_next_step_handler(msg, cmd_entfixa_step1)
                elif message.text == opc_SOROSG:
                    if roboCtrl.instance().robo.gerenciar != 1:
                        msg = botTG.reply_to(message, (Idioma.traducao('Seu gerenciamento não é <b>{}</b>, configure ele primeiro.').format('[SOROSGALE]')), reply_markup=menu_opcoes)
                        botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                        return
                    msg = botTG.reply_to(message, Idioma.traducao('Informe o valor da 1ª Entrada:'))
                    botTG.register_next_step_handler(msg, cmd_sorosgale_step1)
                elif message.text == opc_SOROS:
                    if roboCtrl.instance().robo.gerenciar != 2:
                        msg = botTG.reply_to(message, (Idioma.traducao('Seu gerenciamento não é <b>{}</b>, configure ele primeiro.').format('[SOROS]')), reply_markup=menu_opcoes)
                        botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                        return
                    msg = botTG.reply_to(message, (Idioma.traducao('Qual Tipo de Valor do Soros?')), reply_markup=tipovalor)
                    botTG.register_next_step_handler(msg, cmd_soros_step1)
                elif message.text == opc_PRIME:
                    msg = botTG.reply_to(message, (Idioma.traducao('Selecione:')), reply_markup=menu_prime)
                    botTG.register_next_step_handler(msg, cmd_prime_submenu)
                elif message.text == opc_CICLOS:
                    if roboCtrl.instance().robo.gerenciar != 3:
                        msg = botTG.reply_to(message, (Idioma.traducao('Seu gerenciamento não é <b>{}</b>, configure ele primeiro.').format('[CICLOS]')), reply_markup=menu_opcoes)
                        botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                        return
                    tmp_cicloval10 = 0
                    tmp_cicloval11 = 0
                    tmp_cicloval12 = 0
                    tmp_cicloval20 = 0
                    tmp_cicloval21 = 0
                    tmp_cicloval22 = 0
                    tmp_cicloval30 = 0
                    tmp_cicloval31 = 0
                    tmp_cicloval32 = 0
                    msg = botTG.reply_to(message, Idioma.traducao('Informe o valor do Ciclo C-{} ({}º Coluna):'.format(1, 1)))
                    botTG.register_next_step_handler(msg, cmd_ciclos_c1_step1)
                elif message.text == opc_VOLTAR:
                    cmd_menu_iniciar(message)
                else:
                    msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=menu_opcoes)
                    botTG.register_next_step_handler(msg, cmd_opcoes_step1)
            except Exception as e:
                try:
                    tratarErro(e)
                finally:
                    e = None
                    del e

        else:
            botTG.reply_to(message, Idioma.traducao('Robô já está em operação'))


def cmd_menu_step1(message):
    global botAceitarDoc
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if message.text == opc_iniciar:
                if not roboCtrl.instance().robo.iniciado:
                    try:
                        botAceitarDoc = False
                        msg = botTG.reply_to(message, (Idioma.traducao('Vai operar com qual conta?')), reply_markup=tipoconta)
                        botTG.register_next_step_handler(msg, cmd_iniciar_step1)
                    except Exception as e:
                        try:
                            tratarErro(e)
                        finally:
                            e = None
                            del e

                else:
                    msg = botTG.reply_to(message, (Idioma.traducao('Robô já está em operação')), reply_markup=menu_iniciar)
                    botTG.register_next_step_handler(msg, cmd_menu_step1)
            elif message.text == opc_parar:
                if roboCtrl.instance().robo.iniciado:
                    try:
                        botAceitarDoc = False
                        btn_Parar('-Parar-')
                        msg = botTG.reply_to(message, (Idioma.traducao('Robô parado com sucesso!')), reply_markup=menu_iniciar)
                        botTG.register_next_step_handler(msg, cmd_menu_step1)
                    except Exception as e:
                        try:
                            tratarErro(e)
                        finally:
                            e = None
                            del e

                else:
                    msg = botTG.reply_to(message, (Idioma.traducao('Robô já se encontra parado')), reply_markup=menu_iniciar)
                    botTG.register_next_step_handler(msg, cmd_menu_step1)
            elif message.text == opc_opcoes:
                if not roboCtrl.instance().robo.iniciado:
                    try:
                        msg = botTG.reply_to(message, (Idioma.traducao('Selecione:')), reply_markup=menu_opcoes)
                        botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                    except Exception as e:
                        try:
                            tratarErro(e)
                        finally:
                            e = None
                            del e

                else:
                    botTG.reply_to(message, Idioma.traducao('Robô já está em operação'))
            elif message.text == opc_placar:
                msgTotal = ('{} ' + Idioma.traducao('Parcial:') + '\n{} WIN: {} {} LOSS: {} ( {}% )\n{}<b>' + Idioma.traducao('Lucro atual: $') + '{}</b>').format(emoji.emojize(':checkered_flag:', use_aliases=True), emoji.emojize(':white_check_mark:', use_aliases=True), roboCtrl.instance().operContrl.wins, emoji.emojize(':no_entry:', use_aliases=True), roboCtrl.instance().operContrl.hits, roboCtrl.instance().operContrl.getAssertividade(), emoji.emojize(':moneybag:', use_aliases=True), round(roboCtrl.instance().operContrl.saldo, 2))
                msg = botTG.reply_to(message, msgTotal, reply_markup=menu_iniciar)
                botTG.register_next_step_handler(msg, cmd_menu_step1)
            elif message.text == opc_noticias:
                noticias_text = ''
                for item in roboCtrl.instance().noticias:
                    noticias_text += item.hora[:5] + ' - ' + item.moeda + ' - ' + item.texto[:20] + '\n'

                if noticias_text == '':
                    noticias_text = Idioma.traducao('Nenhuma notícia foi encontrada')
                msg = botTG.reply_to(message, noticias_text, reply_markup=menu_iniciar)
                botTG.register_next_step_handler(msg, cmd_menu_step1)
            else:
                msg = botTG.reply_to(message, (Idioma.traducao('Opção inválida.\nUse os botões para sua escolha.')), reply_markup=menu_opcoes)
                botTG.register_next_step_handler(msg, cmd_opcoes_step1)
                return
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


def cmd_menu_iniciar(message):
    try:
        msg = botTG.reply_to(message, (Idioma.traducao('Selecione:')), reply_markup=menu_iniciar)
        botTG.register_next_step_handler(msg, cmd_menu_step1)
    except Exception as e:
        try:
            tratarErro(e)
        finally:
            e = None
            del e


@botTG.message_handler(commands=['start'])
def command_help(message):
    if roboCtrl.instance().robo.telegranchatid == message.chat.id:
        try:
            if roboCtrl.instance().robo.imgbase64:
                logo_png = os.path.join(os.getcwd(), 'logo64.png')
                if not os.path.exists(logo_png):
                    with open(logo_png, 'wb') as fh:
                        fh.write(base64.standard_b64decode(roboCtrl.instance().robo.imgbase64))
                    fh.close()
                if os.path.exists(logo_png):
                    file_logo_png = open(logo_png, 'rb')
                    ret_img = botTG.send_photo(roboCtrl.instance().robo.telegranchatid, file_logo_png)
                    file_logo_png.close()
                    try:
                        os.remove(logo_png)
                    except:
                        pass

            cmd_menu_iniciar(message)
        except Exception as e:
            try:
                tratarErro(e)
            finally:
                e = None
                del e


@botTG.message_handler(commands=['meuchatid'])
def cmd_meuchatid(message):
    botTG.reply_to(message, 'Meu Chat-ID: ' + str(message.chat.id))