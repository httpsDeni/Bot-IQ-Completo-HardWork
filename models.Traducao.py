# decompyle3 version 3.3.2
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: models\Traducao.py
# Compiled at: 1995-09-27 13:18:56
# Size of source mod 2**32: 272 bytes


class Traduzir:

    def __init__(self, lang='pt-br'):
        self.lang = lang.lower()
        self.textos_pt_br = [
         'Geral',
         'Versão',
         'Agendado',
         'Real',
         'Treinamento',
         'Percentual',
         'Valor',
         'Agressivo',
         'Moderado',
         'Conservador',
         'Informe sua senha.',
         'Informe seu email.',
         'Arquivo da lista não foi localizado.',
         'Atenção',
         'Parâmetros gravados com sucesso!',
         'Agendamentos cancelados com sucesso!',
         'Arquivo não localizado na pasta.',
         'Lista vazia ou com dia/horário expirados.',
         'Aguarde, conectando a IQ...',
         'Gerenciamento',
         'Tipo de conta:',
         'Parâmetros iniciais:',
         'Saldo inicial: $',
         'Quantidade de gales:',
         'Payout mínimo:',
         'Pré-Stop Loss: Ligado',
         'Não operar em notícia',
         'Entradas fixas:',
         'Entrada: $',
         'Gale 1: $',
         'Gale 2: $',
         'Modelo: Agressivo',
         'Modelo: Moderado',
         'Modelo: Conservador',
         '1ª entrada: %',
         'Valor: $',
         'Parar de operar quando atingir: $',
         'Parar de operar quando atingir: $',
         'Agendamento realizado com sucesso!',
         'Abrir',
         'Data',
         'Horário',
         'Ativo',
         'Direção',
         'Dur.',
         'Situação',
         'Lucro',
         'Moeda',
         'Notícias (3 Touros)',
         'Incluir Notícias 2 Touros',
         'Opções',
         'Usar SorosGale',
         'Usar Pré Stop Loss',
         'Não Operar em Notícias',
         'Opções de Entrada',
         'Saldo Inicial $',
         'Payout mínimo %',
         'Qtd. Gales',
         'Tipo de Stop',
         'Entradas Fixas',
         'Tipo',
         '1ª Entrada $',
         'Gale 1 $',
         'Gale 2 $',
         '1ª Entrada %',
         'Modelo',
         'Gravar',
         'Senha',
         'Conta',
         'Saldo Atual $',
         'Assertividade %',
         'Lucro/Perda $',
         'Lista (txt)',
         'Iniciar',
         'Parar',
         'Fechar',
         'Lista de Sinais',
         'Configurações',
         'Diferença de horário:',
         'Problema na conexão, verifique sua internet.',
         'Login/Senha inválido.',
         'Conta conectada:',
         'Fechado',
         'Aberto',
         'Tendência',
         'Cancelado',
         'Erro... Não houve comunição com servidor para validar sua licença. Código',
         'Sua licença expirou dia {}',
         'Sua licença vai expirar dia {}\nNão esqueça de renová-la!',
         'Licença: {} até {}',
         'Licença inválida. Não existe para este email ou está cancelada.',
         'Erro... Não houve comunição com servidor para validar sua licença.',
         'Queda de Internet durante a Operacao',
         'Lucro atual: $',
         'Lucro previsto: $',
         'inválido para a moeda',
         'mínimo de $',
         'Contra Têndencia',
         'Existe notícia de 3 touros',
         'Notícia',
         'Payout inferior:',
         'atual:',
         '1ª Entrada',
         'Perdeu: $',
         'Ganhou: $',
         'Resposta IQ:',
         'Notícias',
         'Minutos (Antes)',
         'Minutos (Após)',
         'Layout inválido.\nLayout correto: ATIVO;DIA;HORARIO;DIRECAO;DURACAO',
         'Leiame',
         'Prioridade',
         'Digital',
         'Binárias',
         'Maior Payout',
         'Não Operar Contra',
         'Quant. Velas',
         'Horário sobrepostos serão cancelados automáticamente',
         'Cancelar este sinal?',
         'Usar EMA5 + EMA20',
         'Aguardar',
         'Resultado por Taxas',
         'Resultado Resp. IQ',
         'Expiração Indisponível',
         'Saldo Inicial não pode ser zero.',
         'Payout não pode ser zero.',
         'Valor do Stop Gain não pode ser zero.',
         'Valor do Stop Loss não pode ser zero.',
         'Valor do Stop Loss não pode ser maior do que 100%.',
         'Valor do Stop Loss não pode ser maior do que o Saldo Inicial.',
         'Excedeu tempo da entrada',
         'Sua versão está desatualizada!\nVersão atual: {0}',
         'o valor da 1ª Entrada % não pode ser zero.',
         'o valor da 1ª Entrada $ não pode ser zero.',
         'o valor do Nível não pode ser zero.',
         'Sua licença não é valida para este robô.',
         'Vela pequena, aguardar resultado IQ',
         'Não houve retorno de taxas, aguardar resultado IQ',
         'Email inválido',
         'Ciclos',
         'Ciclo',
         'Entrada',
         'Gale',
         'Ciclos, nenhum valor foi digitado.',
         'Ciclos, valor do ciclo 1 inválido.',
         'Ciclos, valor do ciclo 2 inválido.',
         'Ciclos, valor do ciclo 3 inválido.',
         'Diferença de horário do seu pc com a IQ, está muito alta!',
         'Origem Sinais',
         'Autorizo o envio dos resultados',
         'Chat_ID do telegram inválido',
         'Opção para descobrir seu Chat_ID, envie msg para {0}',
         'Para o {0} começar a te enviar msg, ele precisa de conhecer, diga um "Olá" pra ele.',
         'Para criar seu bot no telegram, localize o {0} ele vai de ajudar, e gerar o seu token.',
         'Parcial:',
         'Resultado:',
         'Expirou tempo de entrada',
         'Delay = 0, desabilita a verificação e aceita qualquer sinal dentro do tempo de expiração.',
         'Sinal enviado pelo MT4, não é válido para este robô. Cod.',
         'Sinal enviado pelo servidor não é válido para este robô. Cod.',
         'Aguardando sinais do MetaTrader!',
         'Horários de Operação',
         'Horário de Início',
         'Horário de Término',
         'Horário de início inválido',
         'Horário de término inválido',
         'Excluir o horário selecionado ?',
         'Fora do horário de operação',
         'Somente Digital',
         'Somente Binárias',
         'Nenhuma notícia foi encontrada',
         'Sim',
         'Não',
         'Selecione o Autorizo o envio dos resultados e informe o Chat_ID.',
         'Mostra as opções de comandos do robô',
         'Iniciar as operações do robô',
         'Parar as operações do robô',
         'Configurar meu gerenciamento',
         'Resultado parcial',
         'Notícias de hoje',
         'Menu Principal',
         'Opção inválida.\nUse os botões para sua escolha.',
         'Parâmetros salvo com sucesso!',
         'Robô já está em operação',
         'Robô iniciado com sucesso!',
         'Robô parado com sucesso!',
         'Robô já se encontra parado',
         'Enviar manualmente',
         'Selecione:',
         'Envie sua lista de sinais (txt)',
         'Ocorreu um erro...',
         'Tente novamente...',
         'Qual sua senha?',
         'Qual seu e-mail de login?',
         'Continuar usando este e-mail?',
         'Valor inválido, somente números serão válidos.',
         'Defina sua prioridade:',
         'Defina o delay (seg)',
         'Aguardar por Resultado?',
         'Informe a quantidade de velas:',
         'Qual tipo de tendência vai usar?',
         'Informe seu Stop Loss:',
         'Informe seu Stop Gain:',
         'Selecione o Tipo de Stop:',
         'Quantidade de Gales:',
         'Informe o valor do Gale 2',
         'Informe o valor do Gale 1',
         'Informe o valor da 1ª Entrada:',
         'Informe o nível:',
         'Qual Modelo?',
         'Informe o valor do Ciclo C-{} ({}º Coluna):',
         'Informe o Máx. Delay (seg):',
         'Vai usar qual gerenciamento?',
         'Informe o Saldo Inicial:',
         'Qual Tipo de Valor da Entrada Fixa?',
         'Qual Tipo de Valor do Soros?',
         'Selecione a Origem dos Sinais:',
         'Seu gerenciamento não é <b>{}</b>, configure ele primeiro.',
         'Vai operar com qual conta?',
         'Alerta:',
         'Parabéns',
         'Confirmar',
         'Cancelar',
         'Lista',
         'Deseja configurar os horários de operação?',
         'Deseja inserir mais algum horário de operação?',
         'Informe o Horário de Início (HH:MM)',
         'Informe o Horário de Término (HH:MM)',
         'Horário de início inválido.\nNão pode ser superior/igual ao Horário de Término.',
         'Inserir Horário',
         'Excluir Horário',
         'Nenhum horário foi encontrado',
         'Voltar',
         'Lista de Servidores',
         'Descrição',
         'MT4 - Aceitar sinais no mesmo horário',
         'Não foi selecionado nenhum servidor.',
         'Servidor Sinais',
         'Aguardando sinais do servidor!',
         'Conectado ao servidor de sinais',
         'Opç Notícias',
         'Opç Tendência',
         'Saldo Inicial',
         'Valor em Risco $',
         'Total de Operações',
         'Total Op. com Ganho',
         'o total de operações com ganho não pode ser zero',
         'o total de operações com ganho inválido',
         'O cálculo usará o valor de Stop Loss',
         'Payout 80, previsão valor 1ª entrada $ {}',
         'Idioma',
         'Selecione']
        self.textos_ing = [
         'General',
         'Version',
         'Scheduled',
         'Real',
         'Training',
         'Percent',
         'Value',
         'Aggressive',
         'Moderate',
         'Conservative',
         'Inform your password.',
         'Inform your mail.',
         'List file not found.',
         'Attention',
         'Parameters successfully saved!',
         'Schedules canceled successfully!',
         'File not found in the folder.',
         'List empty or with expired day / time.',
         'Wait, connecting the IQ ...',
         'Management',
         'Account Type:',
         'Initial parameters:',
         'Starting value: $',
         'Number of Steps:',
         'Minimum payout:',
         'Pre-Stop Loss: On',
         'Do not operate on news',
         'Fixed inputs:',
         'Entry: $',
         'Step 1: $',
         'Step 2: $',
         'Model: Aggressive',
         'Model: Moderate',
         'Model: Conservative',
         '1st entry: %',
         'Value: $',
         'Stop trading when you reach: $',
         'Stop trading when you reach: $',
         'Scheduling successful!',
         'Open',
         'Date',
         'Time',
         'Pair',
         'Option',
         'Exp.',
         'Situation',
         'Profit',
         'Coin',
         'News (3 Bulls)',
         'Include News 2 Bulls',
         'Options',
         'Use SorosGale',
         'Use Pre Stop Loss',
         'Do not operate in News',
         'Input Options',
         'Initial Value $',
         'Minimum payout %',
         'Qty. Step',
         'Stop Type',
         'Fixed Entries',
         'Type',
         '1st Entry $',
         'Step 1 $',
         'Step 2 $',
         '1st Entry %',
         'Model',
         'Record',
         'Password',
         'Account',
         'Current Balance $',
         'Assertiveness%',
         'Profit / Loss $',
         'List (txt)',
         'Start',
         'Stop',
         'Close',
         'List of Signs',
         'Settings',
         'Time difference:',
         'Connection problem, check your internet.',
         'Invalid login / password.',
         'Connected account:',
         'Closed',
         'Open',
         'Trend',
         'Canceled',
         'Error ... There was no communication with the server to validate your license. Code',
         'Your license expired day {}',
         "Your license will expire on {}\nDon't forget to renew it!",
         'License: {} to {}',
         'Invalid license. It does not exist for this email or is canceled.',
         'Error ... There was no communication with the server to validate your license.',
         'Internet outage during Operation',
         'Current profit: $',
         'Estimated profit: $',
         'invalid for currency',
         'minimum of $',
         'Against tendency',
         'There is news of 3 bulls',
         'News',
         'Lower payout:',
         'current:',
         '1st Entry',
         'Lost: $',
         'Won: $',
         'Response from IQ:',
         'News',
         'Minutes (Before)',
         'Minutes (After)',
         'Invalid layout.\nCorrect layout: ACTIVE;DAY;TIME;DIRECTION;DURATION',
         'Read Me',
         'Priority',
         'Digital',
         'Binary',
         'Max Payout',
         'Do not Operate Against',
         'Num of Candles',
         'Overlapping schedules will be canceled automatically',
         'Cancel this signal?',
         'Use EMA5 + EMA20',
         'Wait',
         'Result by Fees',
         'Result by IQ',
         'Expiration Unavailable',
         'Opening Balance cannot be zero.',
         'Payout cannot be zero.',
         'Stop Gain value cannot be zero.',
         'Stop Loss value cannot be zero.',
         'Stop Loss value cannot be greater than 100%.',
         'Stop Loss amount cannot be greater than the Opening Balance.',
         'Exceeded entry time',
         'Your version is out of date!\nCurrent version: {0}',
         'the value of the 1st Entry % cannot be zero',
         'the value of the 1st Entry $ cannot be zero',
         'the Level value cannot be zero',
         'Your license is not valid for this robot.',
         'Small candle, wait for IQ result',
         'There was no fee return, wait for IQ result',
         'Invalid email.',
         'Cycles',
         'Cycle',
         'Start',
         'Step',
         'Cycles, no values were entered.',
         'Cycles, cycle 1 value invalid.',
         'Cycles, cycle 2 value invalid.',
         'Cycles, cycle 3 value invalid.',
         "Time difference on your pc with IQ, it's too high!",
         'Origin of the Signs',
         'I authorize the sending of results',
         'Invalid Telegram Chat_ID',
         'Option to discover your Chat_ID, send message to {0}',
         'For the {0} to start sending you a message, he needs to know, say "Hello" to him.',
         'To create your bot on the telegram, locate the {0} it will help, and generate your token.',
         'Partial:',
         'Result:',
         'Expired entry time',
         'Delay = 0, disable verification and accept any signal within the expiration time.',
         'Signal sent by MT4, is not valid for this robot. Cod.',
         'Signal sent by Server, is not valid for this robot. Cod.',
         'Waiting for MetaTrader signals!',
         'Hours of Operation',
         'Start Time',
         'End Time',
         'Invalid start time',
         'Invalid end time',
         'Delete selected time?',
         'Outside business hours',
         'Only Digital',
         'Only Binary',
         'No news was found',
         'Yes',
         'No',
         'Select the Authorize to send the results and inform the Chat_ID.',
         'Shows the robot command options',
         'Start robot operations',
         'Stop robot operations',
         'Set up my management',
         'View partial result',
         'View todays news',
         'Main menu',
         'Invalid option.\nUse the buttons for your choice.',
         'Parameters saved successfully!',
         'Robot is already in operation',
         'Robot started successfully!',
         'Robot stopped successfully!',
         'Robot is already stopped',
         'Submit manually',
         'Select:',
         'Send your list of signals (txt)',
         'An error has occurred...',
         'Try again...',
         'Whats your password?',
         'What is your login email?',
         'Continue using this email?',
         'Invalid value, only numbers will be valid.',
         'Set your priority:',
         'Set the delay (sec)',
         'Wait for Result?',
         'Enter the number of candles:',
         'What kind of trend will you use?',
         'Enter your Stop Loss:',
         'Enter your Stop Gain:',
         'Select the Stop Type:',
         'Number of Wales:',
         'Enter the value of Gale 2',
         'Enter the value of Gale 1',
         'Inform the value of the 1st Entry:',
         'Enter the level:',
         'What model?',
         'Enter the value of Cycle C-{} ({}º Column):',
         'Enter the Max. Delay (sec):',
         'Which management will you use?',
         'Enter the Opening Balance:',
         'What Type of Fixed Entry Amount?',
         'What Type of Value of Soros?',
         'Select Signal Source:',
         'Your management is not <b>{}</b>, set it up first.',
         'Which account will you operate with?',
         'Alert:',
         'Congratulations',
         'Confirm',
         'Cancel',
         'List',
         'Do you want to configure the operating hours?',
         'Do you want to enter any other hours of operation?',
         'Enter the Start Time (HH:MM)',
         'Enter the End Time (HH:MM)',
         'Invalid start time.\nIt cannot be greater than/equal to the End Time.',
         'Insert Schedule',
         'Delete Schedule',
         'No times were found',
         'Return',
         'Server List',
         'Description',
         'MT4 - Accept signals at the same time',
         'No server has been selected.',
         'Server Signs',
         'Waiting for signals from the server!',
         'Connected to the signal server',
         'Option News',
         'Option Trend',
         'Opening Balance',
         'Value at Risk $',
         'Total Operations',
         'Total Gain Operat.',
         'total operations cannot be zero',
         'the total of transactions with gain cannot be zero',
         'the total number of transactions with an invalid gain',
         'The calculation will use the Stop Loss',
         'Payout 80, 1st entry price prediction $ {}',
         'Language',
         'Select']
        self.textos_esp = [
         'General',
         'Versión',
         'Programado',
         'Real',
         'Entrenamiento',
         'Porcentaje',
         'Valor',
         'Agresivo',
         'Moderar',
         'Conservador',
         'Informe su contraseña.',
         'Introduce tu correo electrónico.',
         'No se encontró el archivo de lista.',
         'Aviso',
         'Parámetros guardados con éxito!',
         'Horarios cancelados correctamente!',
         'Archivo no encontrado en carpeta.',
         'Lista vacía o con fecha / hora vencida.',
         'Espera, conectando a IQ ...',
         'Gestión',
         'Tipo de cuenta:',
         'Parámetros iniciales:',
         'Saldo inicial: $',
         'Número de Gales:',
         'Pago mínimo:',
         'Pre-Stop Loss: On',
         'No intercambie noticias',
         'Entradas fijas:',
         'Entrada: $',
         'Vendaval 1: $',
         'Vendaval 2: $',
         'Modelo: agresivo',
         'Modelo: Moderado',
         'Modelo: Conservador',
         '1ª entrada:%',
         'Valor: $',
         'Deje de operar cuando llegue a: $',
         'Deje de operar cuando llegue a: $',
         'Programa realizado con éxito!',
         'Abrir',
         'Fecha',
         'Calend.',
         'Activo',
         'Dirección',
         'Dur.',
         'Situación',
         'Lucro',
         'Moneda',
         'Noticias (3 toros)',
         'Incluir News 2 Bulls',
         'Opciones',
         'Utilice SorosGale',
         'Use Pre Stop Loss',
         'No operar en noticias',
         'Opciones de entrada',
         'Saldo inicial $',
         'Pago mínimo %',
         'Cant. Galés',
         'Tipo de Operaciones',
         'Entradas fijas',
         'Tipo',
         '1ª entrada $',
         'Gale 1 $',
         'Gale 2 $',
         '1ª Entrada %',
         'Modelo',
         'Registro',
         'Contraseña',
         'Cuenta',
         'Saldo actual $',
         'Asertividad%',
         'Beneficio / Pérdida $',
         'Lista (txt)',
         'Iniciar',
         'Detener',
         'Cerrar',
         'Lista de señales',
         'Ajustes',
         'Diferencia horaria:',
         'Problema de conexión, revisa tu internet.',
         'Inicio de sesión / contraseña no válidos',
         'Cuenta conectada:',
         'Cerrado',
         'Abierto',
         'Tendencia',
         'Cancelado',
         'Error ... No hubo comunicación con el servidor para validar su licencia. Código',
         'Su licencia expiró el {} día',
         'Su licencia vencerá el día {}\nNo olvide renovarla!',
         'Licencia: {} a {}',
         'Licencia invalida. No existe para este correo electrónico o está cancelado. ',
         'Error ... No hubo comunicación con el servidor para validar su licencia.',
         'Internet cuelga durante la operación',
         'Ingresos actuales: $',
         'Beneficio previsto: $',
         'inválido para moneda',
         'mínimo de $',
         'Contra la tendencia',
         'Hay noticias de 3 toros',
         'Noticias',
         'Pago menor:',
         'Actual:',
         'Primera entrada',
         'Perdido: $',
         'Ganó: $',
         'Respuesta IQ:',
         'Noticias',
         'Minutos (antes)',
         'Minutos (después)',
         'Diseño no válido.\nDiseño correcto: ACTIVO; DÍA; HORA; DIRECCIÓN; DURACIÓN',
         'Léeme',
         'Prioridad',
         'Digital',
         'Binario',
         'Mayor pago',
         'No operar contra',
         'Quant. Velas ',
         'Los horarios superpuestos se cancelarán automáticamente',
         'Cancelar esta señal?',
         'Utilice EMA5 + EMA20',
         'Esperar',
         'Resultado por tarifas',
         'Resp. Yo Q ',
         'Caducidad no disponible',
         'El saldo inicial no puede ser cero.',
         'El pago no puede ser cero.',
         'El valor de Stop Gain no puede ser cero.',
         'El valor de Stop Loss no puede ser cero.',
         'El valor de Stop Loss no puede ser superior al 100%.',
         'El valor de Stop Loss no puede ser mayor que el Saldo Inicial.',
         'Tiempo de entrada excedido',
         'Tu versión está desactualizada!\nVersión actual: {0}',
         'el valor del% de la 1.a entrada no puede ser cero.',
         'el valor de la 1ra entrada $ no puede ser cero.',
         'El valor de nivel no puede ser cero.',
         'Su licencia no es válida para este robot.',
         'Vela pequeña, espera el resultado de IQ',
         'No hubo devolución de tarifas, espere el resultado de IQ',
         'Email inválido',
         'Ciclos',
         'Ciclo',
         'Aporte',
         'Galera',
         'Ciclos, no se ha introducido ningún valor.',
         'Ciclos, valor de ciclo 1 no válido.',
         'Ciclos, valor de ciclo 2 no válido.',
         'Ciclos, valor de ciclo 3 no válido.',
         'La diferencia de tiempo de su PC con el IQ es demasiado alta!',
         'Señales de origen',
         'Autorizo \u200b\u200bel envío de resultados',
         'Chat_ID de Telegram no válido',
         'Opción para averiguar su Chat_ID, enviar mensaje a {0}',
         'Para que {0} comience a enviarte mensajes, necesita saberlo, decirle "Hola".',
         'Para crear su bot en el telegrama, busque el {0} que le ayudará y genere su token.',
         'Parcial:',
         'Resultado:',
         'Tiempo de entrada vencido',
         'Retraso = 0, deshabilite la verificación y acepte cualquier señal dentro del tiempo de vencimiento.',
         'Señal enviada por MT4, no válida para este robot. Bacalao.',
         'La señal enviada por el servidor no es válida para este robot. Bacalao.',
         'Esperando señales de MetaTrader!',
         'Horas de funcionamiento',
         'Hora de inicio',
         'Hora de finalización',
         'Hora de inicio no válida',
         'Hora de finalización no válida',
         'Eliminar la hora seleccionada?',
         'Fuera del horario de funcionamiento',
         'Solo digital',
         'Solo binario',
         'No se encontraron noticias',
         'Sí',
         'No',
         'Seleccione Autorizar el envío de resultados e ingrese el Chat_ID.',
         'Mostrar opciones de comando del robot',
         'Iniciar operaciones del robot',
         'Detener las operaciones del robot',
         'Configurar mi gestión',
         'Resultado parcial',
         'Noticias de hoy',
         'Menú principal',
         'Opción no válida.\nUtilice los botones para su elección.',
         'Parámetros guardados con éxito!',
         'El robot ya está en funcionamiento',
         'El robot se inició con éxito!',
         'El robot se detuvo correctamente!',
         'El robot ya está detenido',
         'Enviar manualmente',
         'Seleccione:',
         'Envía tu lista de señales (txt)',
         'Ocurrio un error...',
         'Inténtalo de nuevo...',
         'Cuál es tu contraseña?',
         'Cuál es su correo electrónico de inicio de sesión?',
         'Continuar usando este correo electrónico?',
         'Valor no válido, solo los números serán válidos.',
         'Establezca su prioridad:',
         'Establecer el retraso (seg)',
         'Esperar el resultado?',
         'Ingrese el número de velas:',
         'Qué tipo de tendencia vas a utilizar?',
         'Ingrese su Stop Loss:',
         'Ingrese su Stop Gain:',
         'Seleccionar tipo de parada:',
         'Cantidad de Gales:',
         'Introduzca el valor de Gale 2',
         'Introduzca el valor de Gale 1',
         'Introduzca el valor de la primera entrada:',
         'Ingrese el nivel:',
         'Cuál modelo?',
         'Ingrese el valor del Ciclo C- {} ({} a Columna):',
         'Introduzca el retardo máximo (seg):',
         'Qué gestión utilizará?',
         'Ingrese el saldo inicial:',
         'Qué tipo de valor de entrada fijo?',
         'Qué tipo de valor del suero?',
         'Seleccione la fuente de las señales:',
         'Tu administración no es <b> {} </b>, configúrala primero.',
         'Con qué cuenta operarás?',
         'Alerta:',
         'Felicidades',
         'Confirmar',
         'Cancelar',
         'Lista',
         'Quieres configurar el horario de funcionamiento?',
         'Quieres ingresar más horas de operación?',
         'Introduzca la hora de inicio (HH: MM)',
         'Introduzca la hora de finalización (HH: MM)',
         'Hora de inicio no válida.\nNo puede ser mayor o igual que la hora de finalización.',
         'Insertar hora',
         'Eliminar programa',
         'No se encontró tiempo',
         'Vuelve',
         'Lista de servidores',
         'Descripción',
         'MT4 - Acepta señales al mismo tiempo',
         'Ningún servidor seleccionado.',
         'Servidor de señales',
         'Esperando señales del servidor!',
         'Conectado al servidor de señales',
         'Option News',
         'Tendencia de opciones',
         'Saldo inicial',
         'Valor en riesgo $',
         'Operaciones totales',
         'Total Op. With Gain',
         'el total de operaciones con ganancia no puede ser cero',
         'el total de operaciones con ganancia inválida',
         'El cálculo utilizará el valor de Stop Loss',
         'Pago 80, valor de previsión 1.ª entrada $ {}',
         'Idioma',
         'Seleccione']

    def setlang(self, lang: str='pt-br'):
        self.lang = lang.lower()

    def traducao(self, texto: str):
        try:
            ret = texto
            if self.lang == 'ing':
                idx = 0
                for txt in self.textos_pt_br:
                    if str(txt).lower() == texto.lower():
                        ret = self.textos_ing[idx]
                        break
                    else:
                        idx += 1

                return ret
            if self.lang == 'esp':
                idx = 0
                for txt in self.textos_pt_br:
                    if str(txt).lower() == texto.lower():
                        ret = self.textos_esp[idx]
                        break
                    else:
                        idx += 1

                return ret
            return ret
        except:
            return ret

    def traducaoLeiame(self):
        texto = ''
        if self.lang == 'ing':
            texto += '\n*** Important ***\n'
            texto += 'We are an entry automation robot in Binary/Digital Operations. The execution of entry orders is completely linked to your signal list and the number of Wales requested. The gain and loss are the users responsibility. Take into account in your risk management, all the possibilities that can occur during a Trader.\n\n'
            texto += '*** List Layout Template ***\n'
            texto += 'PAIR + DAY + HOURS + DIRECTION + EXPIRATION TIME\n'
            texto += 'EX. EURUSD; 10; 15: 00; CALL; 5\n\n'
            texto += '*** Access ***\n'
            texto += 'Access to operations must be with IQ Option email and password. The access data provided is not visible to us. They are restricted to your computer only.\n\n'
            texto += '*** Options ***\n'
            texto += 'Management:\n'
            texto += '- Fixed Entries: When activating this option you should be aware that the entries and Wales will be according to the options in the Fixed Entries box on the side.\n'
            texto += '- SorosGale: When activating this option you should be aware that the entries and Wales will be according to the options in the SorosGale box on the side.\n'
            texto += '- Soros: When activating this option you should be aware that the entries and Welsh will be according to the options in the Soros box on the side.\n'
            texto += '- Cycles: When activating this option, you should be aware that the entries and galleys will be according to the options in the Cycles box beside.\n\n'
            texto += '*** Use Pre Stop Loss ***\n'
            texto += 'When activating the Pre Stop Loss option in a situation where you are close to the Stop Loss margin, the robot interrupts operations, avoiding exceeding the stipulated Stop Loss.\n\n'
            texto += '*** Wait for Result ***\n'
            texto += 'BY FEES - We have the result by the closing rate, with this we have a smaller delay, but with the risk of the result being different from the final IQ, because in the last second it happens to change the direction of the candle.\n'
            texto += 'BY IQ RESPONSE - We have the result for the IQ response, so we have a longer delay, but the result will be 100% equal to that of IQ.\n\n'
            texto += '*** Delay ***\n'
            texto += 'You will be able to inform at what moment in a fraction of a second your order will enter. Anticipating or delaying entry.\n'
            texto += 'OBS. This option will only be valid for the first entry. From the second, it will depend on the response time of the IQ Option.\n\n'
            texto += '*** Priority ***\n'
            texto += '- Highest Payout: The robot will check if the asset is open in digital / binary and decide which is the highest payout.\n'
            texto += '- Digital: The robot will check if the asset is open in digital first, if not, it will also test in binary.\n'
            texto += '- Binary: The robot will check if the asset is open in binary first, if not, it will also test in digital.\n\n'
            texto += '*** Signal Origin ***\n'
            texto += '- Signal List: The robot will receive and operate by signal list (txt) according to the layout.\n'
            texto += '- MetaTrader: The robot will receive and trade signals from MetaTrader4.\n\n'
            texto += '*** MetaTrader ***\n'
            texto += 'Max. Delay (sec) - Used to define a maximum time limit for the signal coming from MetaTrader4.\n\n'
            texto += '*** News ***\n'
            texto += 'In this, the robot will filter your entries freeing them from the news of 3 bulls listed on Investing.com\n'
            texto += 'You will also have control of how long before and after the news the robot will return to operation.\n\n'
            texto += '*** Trend ***\n'
            texto += 'Do not operate against by Quantity of Candles - By quantity. set it will check if the signal is 55% against it will block the signal.\n'
            texto += 'Do not operate against by EMA5 + EMA20 - By moving averages he will check and block the signal only when the 2 averages are against.\n\n'
            texto += '*** Telegram ***\n'
            texto += 'If it authorizes the sending of the results, the robot will send a message to each signal to its personal telegram.\n\n'
            texto += '*** Entrance Options ***\n'
            texto += 'Initial Value: Current value of your broker or an amount you wish to work on your operations.\n'
            texto += 'Minimum Payout (%): Which acceptable minimum to carry out the operations.\n'
            texto += 'Step Qty: How many Wales do you want to make in your operations\n'
            texto += 'Stop Loss Type:\n'
            texto += '- Percentage: The numbers in the Stop Loss and Take Profit fields will be a multiplication in percentage times the value entered in the Initial Value field.\n'
            texto += '- Value: The numbers in the Stop Loss and Take Profit fields will be fixed regardless of the value entered in the Initial Value field.\n\n'
            texto += '*** Fixed Entries ***\n'
            texto += 'Type:\n'
            texto += '- Percentage: The values \u200b\u200bof the Input 1, Step 1, Step 2 fields will be a multiplication in percentage times the value entered in the Value field\n'
            texto += '- Value: The values \u200b\u200bof the Input 1, Step 1, Step 2 fields will be fixed regardless of the value entered in the Initial Value field.\n\n'
            texto += '*** SorosGale ***\n'
            texto += '1st Entry%, set the percentage of the 1st entry. Calculation: (Opening Balance $ * Percentage)\n'
            texto += 'Models:\n'
            texto += '- Conservative: Only makes recovery in Wales.\n'
            texto += '- Moderate: In the recovery of Wales, apply factor 0.25 to make a profit.\n'
            texto += '- Aggressive: In the recovery of Wales, apply the factor 0.50 to obtain a greater profit with greater risk.\n\n'
            texto += '*** Serums ***\n'
            texto += 'Type:\n'
            texto += '- Percentage: The value of the 1st Entry will be a percentage increase over the Starting Balance $\n'
            texto += '- Amount: The amount of the 1st Entry will be fixed regardless of the amount entered in the Opening Balance field.\n'
            texto += '1st Entry $, set the percentage of the 1st entry.\n'
            texto += 'Level, set the maximum serum level, after this level the value returns to the initial level.\n\n'
            texto += '*** Cycles ***\n'
            texto += 'The cycles will obey the field Qty. Step (Input Options)\n'
            texto += 'Qty. Step = 0, cycles can be filled sequentially up to the last column, making entries by signal.\n'
            texto += 'Qty. Step = 1, for each cycle, if you fill in the 1st column (1st entry), you should also fill in the 2nd column (Step1)\n'
            texto += 'Qty. Step = 2, for each cycle, if you fill in the 1st column (1st entry), you should also fill in the 2nd and 3rd column (Step1, Step2)\n\n'
            texto += '*** Record button ***\n'
            texto += 'The information entered and / or adjusted must be saved when clicking on the SAVE Button.\n\n'
            texto += '*** Close ***\n'
            texto += 'To close operations and the entry robot, the CLOSE button located in the lower right corner must be activated\n'
        elif self.lang == 'esp':
            texto += '\n *** Importante ***\n'
            texto += 'Somos un robot de automatización de entrada en operaciones binarias / digitales. La ejecución de las órdenes de entrada está totalmente vinculada a su lista de señales y la cantidad de galés solicitada. Las ganancias y pérdidas son responsabilidad del usuario. Tenga en cuenta en su gestión de riesgos, todas las posibilidades que pueden ocurrir durante un Trader.\n\n '
            texto += '*** Plantilla de diseño de lista !!\n'
            texto += 'PAR + DÍA + HORA + DIRECCIÓN + HORA DE VENCIMIENTO\n'
            texto += 'EX. EURUSD;10;15:00;CALL;5\n\n'
            texto += '*** Acceso ***\n'
            texto += 'El acceso a las operaciones debe ser con el correo electrónico y la contraseña de IQ Option. Los datos de acceso proporcionados no son visibles para nosotros. Están restringidos solo a su computadora.\n\n '
            texto += '*** Opciones ***\n'
            texto += 'Gestión:\n'
            texto += '- Entradas fijas: Al activar esta opción debes tener en cuenta que las entradas y vendavales estarán de acuerdo con las opciones del cuadro Entradas fijas al lado.\n'
            texto += '- SorosGale: Al activar esta opción debes tener en cuenta que las entradas y vendavales estarán de acuerdo con las opciones en el cuadro SorosGale al lado.\n'
            texto += '- Seros: Al activar esta opción debes tener en cuenta que las entradas y vendavales estarán de acuerdo con las opciones en el cuadro Seros al lado.\n'
            texto += '- Ciclos: Al activar esta opción debes tener en cuenta que las entradas y vendavales serán de acuerdo a las opciones en el cuadro Ciclos al lado.\n\n'
            texto += '*** Usar Pre Stop Loss ***\n'
            texto += 'Al activar la opción Pre Stop Loss en una situación en la que está cerca del margen de Stop Loss, el robot interrumpe las operaciones, evitando exceder el Stop Loss estipulado.\n\n'
            texto += '*** Esperar el resultado ***\n'
            texto += 'POR TASAS - Tenemos el resultado por la tasa de cierre, con esto tenemos un retraso menor, pero con el riesgo de que el resultado sea diferente en el IQ final, porque en el último segundo pasa a cambiar la dirección de la vela .\norte'
            texto += 'POR LA RESPUESTA DEL IQ - Tenemos el resultado por la respuesta del IQ, con eso tenemos un retraso mayor, pero el resultado será 100% igual al IQ.\n\n'
            texto += '*** Retraso ***\n'
            texto += 'Podrás informar cuando en una fracción de segundo se realizará tu pedido. Anticipar o retrasar la entrada.\n'
            texto += 'NOTA. Esta opción solo será válida para la primera entrada. A partir del segundo, dependerá del tiempo de respuesta de IQ Option.\n\n '
            texto += '*** Prioridad ***\n'
            texto += '- Mayor pago: el robot verificará si el activo está abierto en digital / binario y decidirá cuál es el mayor pago.\n'
            texto += '- Digital: el robot verificará si el activo está abierto primero en digital, si no, también lo probará en binario.\n'
            texto += '- Binario: el robot verificará si el activo está abierto primero en binario, si no, también lo probará en digital.\n\n'
            texto += '*** Señales de origen ***\n'
            texto += '- Lista de señales: el robot recibirá y operará por lista de señales (txt) de acuerdo con el diseño.\n'
            texto += '- MetaTrader: el robot recibirá y operará mediante señales provenientes de MetaTrader4.\n\n'
            texto += '*** MetaTrader ***\n'
            texto += 'Máx. Retraso (seg): se utiliza para establecer un límite de tiempo máximo para la señal procedente de MetaTrader4.\n\n '
            texto += '*** Noticias ***\n'
            texto += 'En esto, el robot filtrará sus entradas liberándolas de las noticias de 3 toros listados en Investing.com\n'
            texto += 'También tendrás control de cuánto tiempo antes y después de la noticia el robot volverá a funcionar.\n\n'
            texto += '*** Tendencia ***\n'
            texto += 'No opere contra por Cantidad de velas - Por la cantidad. establecerlo comprobará si la señal es del 55% en contra bloqueará la señal.\n'
            texto += 'No opere en contra por EMA5 + EMA20 - Mediante promedios móviles, comprobará y bloqueará la señal solo cuando los 2 promedios estén en contra.\n\n'
            texto += '*** Telegrama ***\n'
            texto += 'Si autoriza el envío de resultados, el robot enviará un mensaje a su telegrama personal en cada señal.\n\n'
            texto += '*** Opciones de entrada ***\n'
            texto += 'Saldo inicial: valor actual de su corredor o un valor en el que desea realizar sus operaciones.\n'
            texto += 'Pago mínimo (%): Qué mínimo aceptable para realizar las operaciones.\n'
            texto += 'Cant. de vendaval: cuántos países de Gales quieres realizar en tus operaciones\n'
            texto += 'Tipo de Stop Loss:\n'
            texto += '- Porcentaje: Los números en los campos Stop Loss y Take Profit serán una multiplicación porcentual por el valor ingresado en el campo Saldo inicial.\n'
            texto += '- Valor: Los números de los campos y los Stop Loss Take Profit se fijará independientemente del valor ingresado en el campo Saldo inicial.\n\n '
            texto += '*** Entradas fijas ***\n'
            texto += 'Tipo:\n'
            texto += '- Porcentaje: Los valores en los campos Entrada 1, Vendaval 1, Vendaval 2 serán una multiplicación porcentual por el valor ingresado en el campo Valor\n'
            texto += '- Valor: Los valores en los campos Entrada 1, Vendaval 1, Vendaval 2 serán fijos independientemente del valor ingresado en el campo Saldo inicial.\n\n'
            texto += '*** SorosGale ***\n'
            texto += '1st Entry%, establezca el porcentaje de la primera entrada. Cálculo: (Saldo inicial $ * Porcentaje)\n'
            texto += 'Plantillas:\n'
            texto += '- Conservador: solo se recupera en Gales.\n'
            texto += '- Moderado: en la recuperación de la cocina, aplique el factor 0.25 para obtener una ganancia.\n'
            texto += '- Agresivo: En la recuperación de Gales, aplique el factor 0.50 para obtener una mayor ganancia con mayor riesgo.\n\n'
            texto += '*** Soros ***\n'
            texto += 'Tipo:\n'
            texto += '- Porcentaje: el valor de la 1.ª entrada será una multiplicación porcentual del saldo inicial $\n'
            texto += '- Valor: El valor de la 1.a entrada será fijo independientemente del valor ingresado en el campo Saldo inicial.\n\n'
            texto += '1ª entrada $, establecer el porcentaje de la 1ª entrada.\n'
            texto += 'Nivel, establece el nivel máximo de suero, después de este nivel el valor vuelve al inicial.\n\n'
            texto += '*** Ciclos ***\n'
            texto += 'Los ciclos obedecerán al campo Cant. Vendaval (Opciones de entrada)\n'
            texto += 'Cant. Gales = 0, los ciclos se pueden completar secuencialmente hasta la última columna, haciendo entradas con el signo.\n'
            texto += 'Cant. Gales = 1, para cada ciclo, si completa la primera columna (primera entrada), también debe completar la segunda columna (Gale1)\n'
            texto += 'Cant. Gales = 2, para cada ciclo, si completa la primera columna (primera entrada), también debe completar la segunda y la tercera columna (Gale1, Gale2)\n\n '
            texto += '*** Botón Guardar ***\n'
            texto += 'La información ingresada y / o ajustada debe guardarse obligatoriamente haciendo clic en el botón GRABAR.\n\n'
            texto += '*** Cerrar ***\n'
            texto += 'Para cerrar las operaciones y el robot de entrada, se debe activar el botón CERRAR ubicado en la esquina inferior derecha\n'
        else:
            texto += '\n*** Importante ***\n'
            texto += 'Somos um robô de automatização de entradas em Operações Binária/Digital. A execução das ordens de entrada está totalmente ligada à sua lista de sinais e à quantidade de Gales solicitados. O ganho e perda são de responsabilidade do usuário. Leve em consideração no seu gerenciamento de risco, todas as possibilidades que podem ocorrer durante um Trader.\n\n'
            texto += '*** Modelo de Layout da Lista!!\n'
            texto += 'PAR+DIA+HORÁRIO+DIREÇÃO+TEMPO DE EXPIRAÇÃO\n'
            texto += 'EX. EURUSD;10;15:00;CALL;5\n\n'
            texto += '*** Acesso ***\n'
            texto += 'O acesso às operações deverá ser com o email e senha da IQ Option. Os dados fornecidos de acesso não são visíveis para nós. Estão restritos apenas ao seu computador.\n\n'
            texto += '*** Opções ***\n'
            texto += 'Gerenciamento:\n'
            texto += '- Entradas Fixas: Ao ativar esta opção você deverá estar ciente que as entradas e gales serão de acordo com as opções da caixa Entradas Fixas ao lado.\n'
            texto += '- SorosGale: Ao ativar esta opção você deverá estar ciente que as entradas e gales serão de acordo com as opções da caixa SorosGale ao lado.\n'
            texto += '- Soros: Ao ativar esta opção você deverá estar ciente que as entradas e gales serão de acordo com as opções da caixa Soros ao lado.\n'
            texto += '- Ciclos: Ao ativar esta opção você deverá estar ciente que as entradas e gales serão de acordo com as opções da caixa Ciclos ao lado.\n\n'
            texto += '*** Usar Pré Stop Loss ***\n'
            texto += 'Ao ativar a opção Pré Stop Loss numa situação em que você esteja perto da margem do Stop Loss, o robô interrompe as operações, evitando a ultrapassagem do Stop Loss estipulado.\n\n'
            texto += '*** Aguardar Resultado ***\n'
            texto += 'POR TAXAS - Temos o resultado pela taxa de fechamento, com isso temos um delay menor, mas com o risco do resultado ser diferente final IQ, porque no último segundo por acontecer de mudar a direção da vela.\n'
            texto += 'PELA RESPOSTA IQ - Temos o resultado pela resposta da IQ, com isso temos um delay maior, mas o resultado será 100% igual ao da IQ.\n\n'
            texto += '*** Delay ***\n'
            texto += 'Você poderá informar em que momento em fração de segundo entrará a sua ordem. Antecipando ou retardando a entrada.\n'
            texto += 'OBS. Essa opção será válida apenas para a primeira entrada. A partir da segunda dependerá do tempo de resposta da IQ Option.\n\n'
            texto += '*** Prioridade ***\n'
            texto += '- Maior Payout: O robô vai verificar se o ativo está aberto na digital/binária e decidir qual maior payout.\n'
            texto += '- Digital: O robô vai verificar se o ativo está aberto primeiro na digital, se não estiver testará também na binária.\n'
            texto += '- Binária: O robô vai verificar se o ativo está aberto primeiro na binária, se não estiver testará também na digital.\n\n'
            texto += '*** Origem Sinais ***\n'
            texto += '- Lista de Sinais: O robô vai receber e operar por lista de sinais (txt) de acordo com o layout.\n'
            texto += '- MetaTrader: O robô vai receber e operar por sinais vindos do MetaTrader4.\n\n'
            texto += '*** MetaTrader ***\n'
            texto += 'Máx. Delay (seg) - Serve para definir um limite máximo de tempo do sinal vindo do MetaTrader4.\n\n'
            texto += '*** Notícias ***\n'
            texto += 'Nesta, o robô filtrará as suas entradas livrando-as das notícias de 3 touros listadas no Investing.com\n'
            texto += 'Você também terá controle de quanto tempo antes e depois da notícia o robô voltará a operar.\n\n'
            texto += '*** Tendência ***\n'
            texto += 'Não operar contra por Quantidade de Velas - Pela quant. definida ele vai verificar se o sinal ficar 55% contra ele vai bloquear o sinal.\n'
            texto += 'Não operar contra por EMA5 + EMA20 - Pelas médias móveis ele vai verificar e bloquear o sinal somente quando as 2 médias estiverem contra.\n\n'
            texto += '*** Telegram ***\n'
            texto += 'Se autorizar o envio dos resultados, o robô enviará a cada sinal uma mensagem para seu telegram pessoal.\n\n'
            texto += '*** Opções de Entradas ***\n'
            texto += 'Saldo Inicial: Valor atual da sua corretora ou um valor em que deseja trabalhar as suas operações.\n'
            texto += 'Payout Mínimo (%): Qual mínimo aceitável para realizar as operações.\n'
            texto += 'Qtd de Gale: Quantos Gales deseja realizar em suas operações\n'
            texto += 'Tipo de Stop Loss:\n'
            texto += '- Percentual: Os números dos campos de Stop Loss e Take Profit serão uma multiplicação em porcentagem vezes o valor inserido no campo Saldo Inicial.\n'
            texto += '- Valor: Os números dos campos Stop Loss e Take Profit serão fixo independentemente do valor inserido no campo Saldo Inicial.\n\n'
            texto += '*** Entradas Fixas ***\n'
            texto += 'Tipo:\n'
            texto += '- Percentual: Os valores dos campos de Entrada 1, Gale 1, Gale 2 serão uma multiplicação em porcentagem vezes o valor inserido no campo Valor\n'
            texto += '- Valor: Os valores dos campos de Entrada 1, Gale 1, Gale 2 serão fixos independentemente do valor inserido no campo Saldo Inicial.\n\n'
            texto += '*** SorosGale ***\n'
            texto += '1ª Entrada %, defina o percentual da 1ª entrada. Cálculo: (Saldo Inicial $ * Percentual)\n'
            texto += 'Modelos:\n'
            texto += ' - Conservador: Só faz recuperação nos gales.\n'
            texto += ' - Moderado: Na recuperação dos gales, aplica o fator 0.25 para obter um lucro.\n'
            texto += ' - Agressivo: Na recuperação dos gales, aplica o fator 0.50 para obter um maior lucro com maior risco.\n\n'
            texto += '*** Soros ***\n'
            texto += 'Tipo:\n'
            texto += '- Percentual: O valor da 1ª Entrada será uma multiplicação em porcentagem sobre o Saldo Inicial $\n'
            texto += '- Valor: O valor da 1ª Entrada será fixo independentemente do valor inserido no campo Saldo Inicial.\n\n'
            texto += '1ª Entrada $, defina o percentual da 1ª entrada.\n'
            texto += 'Nível, defina o nível máximo do soros, após este nível o valor volta ao inicial.\n\n'
            texto += '*** Ciclos ***\n'
            texto += 'Os ciclos obedecerá o campo Qtd. Gale (Opções de Entrada)\n'
            texto += 'Qtd. Gales = 0, os ciclos poderá ser preenchos sequencialmente até a última coluna, fazendo entradas por sinal.\n'
            texto += 'Qtd. Gales = 1, pra cada ciclo, se preenchear a 1ª coluna (1ª entrada), deverá preenchear também a 2ª coluna (Gale1)\n'
            texto += 'Qtd. Gales = 2, pra cada ciclo, se preenchear a 1ª coluna (1ª entrada), deverá preenchear também a 2ª e 3ª coluna (Gale1,Gale2)\n\n'
            texto += '*** Botão Gravar ***\n'
            texto += 'As informações inseridas e/ou ajustadas deverão ser obrigatoriamente salvas ao clicar no Botão GRAVAR.\n\n'
            texto += '*** Fechar ***\n'
            texto += 'Para fechar as operações e o robô de entrada, o botão FECHAR localizado no canto inferior direito deverá ser acionado\n'
        return texto