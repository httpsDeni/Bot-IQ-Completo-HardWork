import sys, os, PySimpleGUI as sg
from main.roboUtils import *

class JobsView:

    def __init__(self, nomeapp='JOBsPlay', tema='Reddit', versao='', img_logo=None, img_base64=None, afiliado=0):
        self.appStarted = False
        self.nomeApp = nomeapp
        self.versao = Idioma.traducao('Versão') + ' ' + versao
        sg.theme(tema)
        self.headings = [
         'ID',
         Idioma.traducao('Data'),
         Idioma.traducao('Horário'),
         Idioma.traducao('Ativo'),
         Idioma.traducao('Direção'),
         Idioma.traducao('Dur.'),
         Idioma.traducao('Situação'),
         Idioma.traducao('Lucro')]
        self.data = [['' for _ in range(len(self.headings))]]
        self.headings2 = [
         Idioma.traducao('Horário'),
         Idioma.traducao('Moeda'),
         Idioma.traducao('Notícias')]
        self.data2 = [['' for _ in range(len(self.headings2))]]
        self.col01 = sg.Column([
         [
          sg.Frame((Idioma.traducao('Opções')), [
           [
            sg.Text(Idioma.traducao('Gerenciamento')),
            sg.OptionMenu(values=(Idioma.traducao('Entradas Fixas'), 'SorosGale', 'Soros', Idioma.traducao('Ciclos')), key='gerenciar')],
           [
            sg.Checkbox((Idioma.traducao('Usar Pré Stop Loss')), key='prestop')],
           [
            sg.Text(Idioma.traducao('Aguardar')),
            sg.OptionMenu(values=(Idioma.traducao('Resultado por Taxas'), Idioma.traducao('Resultado Resp. IQ')), key='esperarIQ')],
           [
            sg.Text('Delay (seg)', size=(14, 0)), sg.Spin(values=[i for i in range(0, 11)], initial_value=0, enable_events=True, key='delay')],
           [
            sg.Text((Idioma.traducao('Prioridade')), size=(14, 0)),
            sg.OptionMenu(values=(Idioma.traducao('Maior Payout'), Idioma.traducao('Digital'), Idioma.traducao('Binárias'),
             Idioma.traducao('Somente Digital'), Idioma.traducao('Somente Binárias')),
              key='priorid')],
           [
            sg.Frame((Idioma.traducao('Notícias')), [
             [
              sg.Checkbox((Idioma.traducao('Não Operar em Notícias')), key='naonoticia')],
             [
              sg.Checkbox((Idioma.traducao('Incluir Notícias 2 Touros')), key='touros2')],
             [
              sg.Text((Idioma.traducao('Minutos (Antes)')), size=(13, 0)), sg.Spin(values=[i for i in range(0, 60)], initial_value=0, enable_events=True, key='notminantes')],
             [
              sg.Text((Idioma.traducao('Minutos (Após)')), size=(13, 0)), sg.Spin(values=[i for i in range(0, 60)], initial_value=0, enable_events=True, key='notminapos')]],
              key='-framenoticia-')],
           [
            sg.Frame((Idioma.traducao('Tendência')), [
             [
              sg.Checkbox((Idioma.traducao('Não Operar Contra')), key='tendusar')],
             [
              sg.Radio((Idioma.traducao('Quant. Velas')), size=(13, 0), group_id='tendemasma', key='tendqtdvela'), sg.Spin(values=[i for i in range(0, 100)], initial_value=0, enable_events=True, key='tendvelas')],
             [
              sg.Radio((Idioma.traducao('Usar EMA5 + EMA20')), group_id='tendemasma', key='tendemasma')]],
              key='-frametend-')]],
            key='-frameopcao-')],
         [
          sg.Frame((Idioma.traducao('Idioma')), [
           [
            sg.Text(Idioma.traducao('Selecione')),
            sg.OptionMenu(values=('Pt-BR', 'Inglês', 'Espanhol'), key='opclang')]],
            key='-frameidioma-')]],
          key='-tab1col01-',
          pad=(0, 0),
          justification='left',
          element_justification='left',
          vertical_alignment='top')
        self.col02 = sg.Column([
         [
          sg.Frame('', [
           [
            sg.Frame('', [
             [
              sg.Text((Idioma.traducao('Saldo Inicial $')), size=(15, 0), font=('Helvetica', 9, 'bold')),
              sg.InputText(size=(13, 0), font=('Helvetica', 9, 'bold'), justification='right', enable_events=True, key='valinic')]],
              key='-framevalinic-')],
           [
            sg.Frame((Idioma.traducao('Opções de Entrada')), [
             [
              sg.Text((Idioma.traducao('Payout Mínimo %')), size=(17, 0)),
              sg.Spin(values=[i for i in range(50, 99)], initial_value=80, size=(13, 1), enable_events=True, key='payout')],
             [
              sg.Text((Idioma.traducao('Qtd. Gales')), size=(17, 0)),
              sg.Spin(values=[i for i in range(0, 3)], initial_value=0, size=(13, 1), enable_events=True, key='qtdgale')],
             [
              sg.Text((Idioma.traducao('Tipo de Stop')), size=(17, 0)),
              sg.OptionMenu(values=(Idioma.traducao('Percentual'), Idioma.traducao('Valor')), size=(9,
                                                                                      1), key='tipostop')],
             [
              sg.Text('Stop Gain $', size=(17, 0)),
              sg.InputText(size=(15, 0), justification='right', enable_events=True, key='stopgain')],
             [
              sg.Text('Stop Loss $', size=(17, 0)),
              sg.InputText(size=(15, 0), justification='right', enable_events=True, key='stoploss')]],
              key='-frameopcent-')]],
            key='-frameentinicial-')],
         [
          sg.Frame((Idioma.traducao('Opções')), [
           [
            sg.Text((Idioma.traducao('Origem Sinais')), key='lblorigemsinal44'),
            sg.OptionMenu(values=(Idioma.traducao('Lista de Sinais'), Idioma.traducao('Servidor Sinais')), key='origemsinal44')],
           [
            sg.Frame('MetaTrader', [
             [
              sg.Text('Máx. Delay (seg)', size=(14, 0)),
              sg.Spin(values=[i for i in range(0, 30)], initial_value=0, size=(13, 1), enable_events=True, key='maxdelaymt44')],
             [
              sg.Text((Idioma.traducao('Delay = 0, desabilita a verificação e aceita qualquer sinal dentro do tempo de expiração.')), size=(35,
                                                                                                                              3), enable_events=True, key='-labelmaxmt44-')]],
              key='-framemt44-')]],
            key='-frameopcao44-')]],
          key='-tab1col02-',
          pad=(0, 0),
          justification='left',
          element_justification='left',
          vertical_alignment='top')
        self.col03 = sg.Column([
         [
          sg.Frame((Idioma.traducao('Entradas Fixas')), [
           [
            sg.Text((Idioma.traducao('Tipo')), size=(10, 0)),
            sg.OptionMenu(values=(Idioma.traducao('Percentual'), Idioma.traducao('Valor')), size=(15,
                                                                                      1), key='percent')],
           [
            sg.Text((Idioma.traducao('1ª Entrada $')), size=(10, 0)),
            sg.InputText(size=(15, 0), justification='right', enable_events=True, key='valor1')],
           [
            sg.Text((Idioma.traducao('Gale 1 $')), size=(10, 0)),
            sg.InputText(size=(15, 0), justification='right', enable_events=True, key='gale1')],
           [
            sg.Text((Idioma.traducao('Gale 2 $')), size=(10, 0)),
            sg.InputText(size=(15, 0), justification='right', enable_events=True, key='gale2')],
           [
            sg.Checkbox((Idioma.traducao('MT4 - Aceitar sinais no mesmo horário')), key='entfixamt4')]],
            key='-frameentfixa-')],
         [
          sg.Frame((Idioma.traducao('Ciclos')), [
           [
            sg.Text('', size=(3, 0)),
            sg.Text((Idioma.traducao('Entrada') + ' $'), size=(8, 0))],
           [
            sg.Text('C-1', size=(3, 0)),
            sg.InputText(size=(8, 0), justification='right', enable_events=True, key='cicloval10'),
            sg.InputText(size=(8, 0), justification='right', enable_events=True, key='cicloval11'),
            sg.InputText(size=(8, 0), justification='right', enable_events=True, key='cicloval12')],
           [
            sg.Text('C-2', size=(3, 0)),
            sg.InputText(size=(8, 0), justification='right', enable_events=True, key='cicloval20'),
            sg.InputText(size=(8, 0), justification='right', enable_events=True, key='cicloval21'),
            sg.InputText(size=(8, 0), justification='right', enable_events=True, key='cicloval22')],
           [
            sg.Text('C-3', size=(3, 0)),
            sg.InputText(size=(8, 0), justification='right', enable_events=True, key='cicloval30'),
            sg.InputText(size=(8, 0), justification='right', enable_events=True, key='cicloval31'),
            sg.InputText(size=(8, 0), justification='right', enable_events=True, key='cicloval32')],
           [
            sg.Text((Idioma.traducao('Horário sobrepostos serão cancelados automáticamente')), size=(30,
                                                                                         2))]],
            key='-frameciclos-')]],
          key='-tab1col03-',
          pad=(0, 0),
          justification='left',
          element_justification='left',
          vertical_alignment='top')
        self.col04 = sg.Column([
         [
          sg.Frame('SorosGale', [
           [
            sg.Text((Idioma.traducao('1ª Entrada %')), size=(10, 0)),
            sg.InputText(size=(15, 0), justification='right', enable_events=True, key='percentsoros')],
           [
            sg.Text((Idioma.traducao('Modelo')), size=(10, 0)),
            sg.OptionMenu(values=(Idioma.traducao('Agressivo'), Idioma.traducao('Moderado'), Idioma.traducao('Conservador')), size=(12,
                                                                                                                        1), key='modelo')],
           [
            sg.Text((Idioma.traducao('Horário sobrepostos serão cancelados automáticamente')), size=(30,
                                                                                         2))]],
            key='-framesorosgale-')],
         [
          sg.Frame('Soros', [
           [
            sg.Text((Idioma.traducao('Tipo')), size=(10, 0)),
            sg.OptionMenu(values=(Idioma.traducao('Percentual'), Idioma.traducao('Valor')), size=(12,
                                                                                      1), key='tipovalsoros')],
           [
            sg.Text((Idioma.traducao('1ª Entrada $')), size=(10, 0)),
            sg.InputText(size=(15, 0), justification='right', enable_events=True, key='valorentsoros')],
           [
            sg.Text((Idioma.traducao('Nível')), size=(10, 0)),
            sg.Spin(values=[i for i in range(0, 20)], initial_value=0, size=(13, 1), enable_events=True, key='nivelsoros')],
           [
            sg.Text((Idioma.traducao('Horário sobrepostos serão cancelados automáticamente')), size=(30,
                                                                                         2))]],
            key='-framesoros-')]],
          key='-tab1col04-',
          pad=(0, 0),
          justification='left',
          element_justification='left',
          vertical_alignment='top')
        self.col11 = sg.Column([
         [
          sg.Frame((Idioma.traducao('Opções')), [
           [
            sg.Text((Idioma.traducao('Origem Sinais')), key='lblorigemsinal'),
            sg.OptionMenu(values=(Idioma.traducao('Lista de Sinais'), 'MetaTrader', Idioma.traducao('Servidor Sinais')), key='origemsinal')],
           [
            sg.Frame('MetaTrader', [
             [
              sg.Text('Máx. Delay (seg)', size=(14, 0)),
              sg.Spin(values=[i for i in range(0, 30)], initial_value=0, size=(13, 1), enable_events=True, key='maxdelaymt4')],
             [
              sg.Text((Idioma.traducao('Delay = 0, desabilita a verificação e aceita qualquer sinal dentro do tempo de expiração.')), size=(35,
                                                                                                                              3), enable_events=True, key='-labelmaxmt4-')]],
              key='-framemt4-')]],
            key='-frameopcao11-')],
         [
          sg.Frame((Idioma.traducao('Horários de Operação')), [
           [
            sg.Text((Idioma.traducao('Horário de Início')), size=(15, 0)), sg.Text(Idioma.traducao('Horário de Término'))],
           [
            sg.Spin(values=[i for i in range(0, 24)], initial_value=0, size=(3, 1), enable_events=True, key='hrinicmt'),
            sg.Spin(values=[i for i in range(0, 60)], initial_value=0, size=(3, 1), enable_events=True, key='mininicmt'),
            sg.Text(' '),
            sg.Spin(values=[i for i in range(0, 24)], initial_value=0, size=(3, 1), enable_events=True, key='hrtermmt'),
            sg.Spin(values=[i for i in range(0, 60)], initial_value=0, size=(3, 1), enable_events=True, key='mintermmt'),
            sg.Text(' '),
            sg.Button('+', size=(2, 1), font=('Helvetica', 10, 'bold'), key='-AddHrOper-')],
           [
            sg.Listbox([], size=(20, 5), font=('Helvetica', 12), enable_events=True, bind_return_key=True, key='-LISTAHORAOPERA-'),
            sg.Button('-', size=(2, 1), font=('Helvetica', 10, 'bold'), key='-DelHrOper-')]],
            key='-framehoraoperacao-')]],
          key='-tab4col01-',
          pad=(0, 0),
          justification='left',
          element_justification='left',
          vertical_alignment='top')
        self.col12 = sg.Column([
         [
          sg.Frame('Telegram', [
           [
            sg.Checkbox((Idioma.traducao('Autorizo o envio dos resultados')), key='telegranusar')],
           [
            sg.Text('Chat_ID', size=(10, 0)),
            sg.InputText(size=(20, 0), enable_events=True, key='telegranchatid')],
           [
            sg.Text((Idioma.traducao('Opção para descobrir seu Chat_ID, envie msg para {0}').format('@chatid_echo_bot')), size=(65,
                                                                                                                    1), enable_events=True, key='-linktelegranecho-')],
           [
            sg.Text((Idioma.traducao('Para o {0} começar a te enviar msg, ele precisa de conhecer, diga um "Olá" pra ele.').format('@RoboNotifyOB_Bot')), size=(66,
                                                                                                                                                    2), enable_events=True, key='-linktelegran1-')],
           [
            sg.Text('')],
           [
            sg.Text((Idioma.traducao('Para criar seu bot no telegram, localize o {0} ele vai de ajudar, e gerar o seu token.').format('@BotFather')), size=(66,
                                                                                                                                                2), enable_events=True, key='-linktelegran2-')],
           [
            sg.Text('Token Bot', size=(10, 0)),
            sg.InputText(size=(55, 0), key='telegrantoken')]],
            key='-frametelegran-')]],
          key='-tab4col02-',
          pad=(0, 0),
          justification='left',
          element_justification='left',
          vertical_alignment='top')
        self.layout_tab1 = [
         [
          self.col01, self.col02, self.col03, self.col04]]
        self.layout_tab22 = [
         [
          self.col11]]
        self.layout_tab3 = [
         [
          self.col12]]
        self.layoutX = [
         [
          sg.TabGroup([
           [
            sg.Tab(('   ' + Idioma.traducao('Geral') + '   '), (self.layout_tab1), key='-tabgeral-'),
            sg.Tab(' * Prime * ', (self.layout_tab22), key='-tabprime-'),
            sg.Tab(' Telegram ', (self.layout_tab3), key='-tabtelgram-')]],
            pad=(0, 0),
            key='--tabgroup11',
            font=('Helvetica', 10, 'bold'))],
         [
          sg.Button((Idioma.traducao('Gravar')), size=(20, 1), key='-Gravar-'),
          sg.Text('', size=(100, 2)),
          sg.Button((Idioma.traducao('Leiame')), size=(20, 1), key='-Ajuda-')]]
        if img_base64:
            self.imglogo = sg.Image(data=img_base64, size=(300, 130), key='-imglogo-')
        elif img_logo:
            self.imglogo = sg.Image(img_logo, size=(300, 130), key='-imglogo-')
        else:
            self.imglogo = sg.Frame('', [], size=(305, 130), pad=(0, 0), key='-imglogo-')
        self.col1 = sg.Column([
         [
          self.imglogo],
         [
          sg.Frame('', [
           [
            sg.Text('Email', size=(10, 0), font=('Helvetica', 8, 'bold')),
            sg.InputText(size=(20, 0), key='email')],
           [
            sg.Text((Idioma.traducao('Senha')), size=(10, 0), font=('Helvetica', 8, 'bold')),
            sg.Input(size=(20, 0), password_char='*', key='senha')],
           [
            sg.Text((Idioma.traducao('Conta')), size=(10, 0), font=('Helvetica', 8, 'bold')),
            sg.OptionMenu(values=(Idioma.traducao('Treinamento'), Idioma.traducao('Real')), size=(20,
                                                                                      1), key='contatipo')]],
            pad=(0, 0),
            key='-framelogin-')],
         [
          sg.Frame('', [
           [
            sg.Text((Idioma.traducao('Saldo Atual $')), size=(18, 0), font=('Helvetica', 8, 'bold'), justification='rigth'),
            sg.Text(size=(10, 0), relief='sunken', font=('Helvetica', 8, 'bold'), justification='right', key='saldoatual')],
           [
            sg.Text('Stop Gain %', font=('Helvetica', 8, 'bold'), size=(10, 0)),
            sg.Text(size=(4, 0), relief='sunken', font=('Helvetica', 8, 'bold'), justification='right', key='stopgainp'),
            sg.Text('$', font=('Helvetica', 8, 'bold'), size=(1, 0), justification='right'),
            sg.Text(size=(10, 0), relief='sunken', font=('Helvetica', 8, 'bold'), justification='right', key='stopgainv')],
           [
            sg.Text('Stop Loss %', font=('Helvetica', 8, 'bold'), text_color='red', size=(10, 0)),
            sg.Text(size=(4, 0), relief='sunken', font=('Helvetica', 8, 'bold'), text_color='red', justification='right', key='stoplossp'),
            sg.Text('$', font=('Helvetica', 8, 'bold'), size=(1, 0), justification='right'),
            sg.Text(size=(10, 0), relief='sunken', font=('Helvetica', 8, 'bold'), text_color='red', justification='right', key='stoplossv')]],
            pad=(0, 0),
            key='-framesaldo-')],
         [
          sg.Frame('', [
           [
            sg.Text((Idioma.traducao('Saldo Inicial $')), size=(26, 0), font=('Helvetica', 8, 'bold'), justification='rigth'),
            sg.Text(size=(8, 0), relief='sunken', font=('Helvetica', 8, 'bold'), justification='right', key='valorinic')],
           [
            sg.Text('WIN', size=(3, 0), font=('Helvetica', 8, 'bold')),
            sg.Text(size=(7, 0), relief='sunken', font=('Helvetica', 8, 'bold'), justification='right', key='placarW'),
            sg.Text((Idioma.traducao('Assertividade %')), font=('Helvetica', 8, 'bold'), size=(13,
                                                                                   0), justification='right'),
            sg.Text(size=(8, 0), relief='sunken', font=('Helvetica', 8, 'bold'), justification='right', key='assertividade')],
           [
            sg.Text('HIT', size=(3, 0), font=('Helvetica', 8, 'bold'), text_color='red'),
            sg.Text(size=(7, 0), relief='sunken', font=('Helvetica', 8, 'bold'), text_color='red', justification='right', key='placarH'),
            sg.Text((Idioma.traducao('Lucro/Perda $')), font=('Helvetica', 8, 'bold'), size=(13,
                                                                                 0), justification='right'),
            sg.Text(size=(8, 0), relief='sunken', font=('Helvetica', 8, 'bold'), justification='right', key='saldolucro')]],
            pad=(0, 0),
            key='-frameplacar-')],
         [
          sg.Table(values=(self.data2), headings=(self.headings2), background_color='white',
            text_color='black',
            selected_row_colors=('white', 'black'),
            header_font=('Helvetica', 8, 'bold'),
            justification='center',
            auto_size_columns=False,
            col_widths=(7, 7, 22),
            num_rows=11,
            pad=(0, 0),
            key='-TABLENOTICIAS-')],
         [
          sg.Text('Licença:', size=(50, 1), text_color='green', pad=(0, 0), key='-licenca-', justification='left')]],
          key='-tab2col1-',
          justification='left',
          element_justification='left',
          vertical_alignment='top')
        self.col2 = sg.Column([
         [
          sg.Text(Idioma.traducao('Lista (txt)')),
          sg.Input(size=(30, 0), key='arqlista'),
          sg.FileBrowse((Idioma.traducao('Abrir')), size=(7, 1), key='-abrirlista-', file_types=(('Lista de sinais', '*.txt'), )),
          sg.Button('Download', size=(10, 1), key='-Download-', visible=(afiliado > 0))],
         [
          sg.Button((Idioma.traducao('Iniciar')), size=(20, 1), font=('Helvetica', 10, 'bold'), bind_return_key=True, button_color=('white',
                                                                                                                          'springgreen4'), key='-Iniciar-'),
          sg.Button((Idioma.traducao('Parar')), size=(20, 1), font=('Helvetica', 10, 'bold'), button_color=('white',
                                                                                                  'firebrick3'), key='-Parar-')],
         [
          sg.Table(values=(self.data), headings=(self.headings), background_color='white',
            text_color='black',
            selected_row_colors=('white', 'black'),
            header_font=('Helvetica', 8, 'bold'),
            justification='center',
            auto_size_columns=False,
            col_widths=(5, 8, 8, 13, 7, 6, 14, 14),
            num_rows=28,
            enable_events=False,
            bind_return_key=True,
            key='-TABLE-')],
         [
          sg.Output(size=(57, 6), font=('Courier New', 8), pad=(0, 0), background_color='black',
            text_color='white',
            key='-output-')]],
          key='-tab2col2-',
          justification='left',
          element_justification='left',
          vertical_alignment='top')
        self.layout_tab2 = [
         [
          self.col1, self.col2]]
        self.layout = [
         [
          sg.TabGroup([
           [
            sg.Tab(Idioma.traducao('Lista de Sinais'), self.layout_tab2),
            sg.Tab(Idioma.traducao('Configurações'), self.layoutX)]],
            pad=(0, 0),
            key='--tabgroup1')],
         [
          sg.Text('', size=(50, 1), text_color='red', justification='left', key='-status-'),
          sg.Button((Idioma.traducao('Fechar')), size=(20, 1), font=('Helvetica', 10, 'bold'), key='-Fechar-')]]

    def Show(self):
        sg.set_options(text_element_background_color=(sg.theme_input_text_color()), element_background_color=(sg.theme_input_background_color()),
          input_elements_background_color=(sg.theme_input_background_color()),
          enable_treeview_869_patch=False)
        self.janela = sg.Window((self.nomeApp + ' - ' + self.versao), (self.layout), font=('Helvetica',
                                                                                           8),
          margins=(0, 0),
          finalize=True,
          disable_close=True,
          alpha_channel=0.9,
          icon='./icon/jobsplay.ico')
        for col in ('-status-', 'saldoatual', 'valorinic', '-TABLENOTICIAS-', '-licenca-',
                    '-status-', 'email', 'senha', 'contatipo', 'stopgainv', 'stoplossv',
                    'assertividade', 'saldolucro', '-frameidioma-', 'valinic', 'payout',
                    'qtdgale', 'tipostop', 'stopgain', 'stoploss', 'origemsinal',
                    'gerenciar', 'opclang', 'percent', 'valor1', 'gale1', 'gale2',
                    'percentsoros', 'modelo', 'priorid', 'tendemasma', 'esperarIQ',
                    'delay', 'notminantes', 'notminapos', 'tendvelas', 'tipovalsoros',
                    'valorentsoros', 'nivelsoros', '-framemt4-', 'maxdelaymt4', '-labelmaxmt4-',
                    '-framemt44-', 'maxdelaymt44', '-labelmaxmt44-', 'origemsinal44',
                    '-framenoticia-', '-frametend-', 'arqlista', '-Iniciar-', '-Parar-'):
            self.janela[col].expand(expand_x=True)

        for col in ('-frameopcao-', '-frameentinicial-', '-frameentfixa-', '-framesoros-',
                    '-framesorosgale-', '-frameciclos-', '-framehoraoperacao-', '-frameopcao44-'):
            self.janela[col].expand(expand_y=True)

        for col in ('-framelogin-', '-framesaldo-', '-frameplacar-', '-output-', '-tab2col2-',
                    '-TABLE-', '-frametelegran-'):
            self.janela[col].expand(expand_y=True, expand_x=True)


def ExemploCriarNovoTema():
    sg.LOOK_AND_FEEL_TABLE['MyNewTheme'] = {'BACKGROUND':'#3d4854', 
     'TEXT':'white', 
     'INPUT':'white', 
     'TEXT_INPUT':'#000000', 
     'SCROLL':'#c7e78b', 
     'BUTTON':('white', '#3d4854'), 
     'PROGRESS':('#01826B', '#D0D0D0'), 
     'BORDER':1, 
     'SLIDER_DEPTH':0,  'PROGRESS_DEPTH':0}
    sg.theme('MyNewTheme')