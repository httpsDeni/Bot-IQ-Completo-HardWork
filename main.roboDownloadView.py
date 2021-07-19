import PySimpleGUI as sg
from main.roboUtils import *

class JobsViewDownload:

    def __init__(self):
        self.headings = [
         Idioma.traducao('Data'),
         Idioma.traducao('Lista')]
        self.data = [['' for _ in range(len(self.headings))]]
        self.layout = [
         [
          sg.Text((Idioma.traducao('Lista de Sinais')), size=(20, 0), key='cabec', justification='l', font=('Helvetica',
                                                                                                  8,
                                                                                                  'bold'), text_color=(sg.theme_text_color()),
            background_color=(sg.theme_background_color()))],
         [
          sg.Table(values=(self.data), headings=(self.headings), background_color='white',
            text_color='black',
            selected_row_colors=('white', 'black'),
            header_font=('Helvetica', 8, 'bold'),
            font=('Helvetica', 14),
            justification='center',
            auto_size_columns=False,
            col_widths=(10, 30),
            num_rows=5,
            pad=(0, 0),
            key='-TABLELISTA-')],
         [
          sg.Button((Idioma.traducao('Confirmar')), size=(20, 1), key='-ConfLista-'),
          sg.Button((Idioma.traducao('Cancelar')), size=(20, 1), key='-CancLista-')]]

    def Show(self):
        sg.set_options(text_element_background_color=(sg.theme_input_text_color()), element_background_color=(sg.theme_input_background_color()),
          input_elements_background_color=(sg.theme_input_background_color()),
          enable_treeview_869_patch=False)
        self.janela = sg.Window((Idioma.traducao('Lista de Sinais')), (self.layout), font=('Helvetica',
                                                                                           8),
          margins=(0, 0),
          text_justification='r',
          finalize=True,
          return_keyboard_events=True,
          no_titlebar=True,
          modal=True,
          grab_anywhere=False)

    def atualizaGrid(self, datalista):
        data = []
        for item in datalista:
            data.append([item['data'], item['nome']])

        self.janela['-TABLELISTA-'].update(values=data)
        self.janela.refresh()