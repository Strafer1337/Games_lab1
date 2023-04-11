from bimatrix import BiMatrix
from matrix import Matrix
import PySimpleGUI as gui

MATRIX_STR = "Матричные игры"
BIMATRIX_STR = "Биматричные игры"

def matrix_gui():
    gui.theme('SandyBeach')

    layout = [
        [gui.Stretch(), gui.Text(MATRIX_STR, font=("Helvetica", 20)), gui.Stretch()],
        [gui.Text('Выберите файл с матрицей', font=("Helvetica", 16))],
        [gui.InputText(size = (38,1), key = 'file_path'), gui.FileBrowse('Открыть файл', button_color='SlateGray', size=(11,1))], 
        [gui.Button('Загрузить', button_color='SlateGray', size = (46, 1))],
        [gui.Text('Доступные виды действий: ', font=("Helvetica", 16))],
        [gui.Button('Найти максимин и минимакс', size=(22,1)), gui.Button("Найти строго доминируемые", size=(22,1))], # action buttons
        [gui.Button("Найти слабо доминируемые", size=(22,1)), gui.Button('Найти НЛО стратегии', size=(22,1))],
        [gui.Text('Введенная матрица:', font=("Helvetica", 16))],           
        [gui.Output(size = (52,7), key = 'output')],
        [gui.Text('Вывод:', font=("Helvetica", 16))],
        [gui.Multiline(key = 'text', size=(52, 7))],
        [gui.Text('Укажите имя файла для вывода', font=("Helvetica", 16))],
        [gui.InputText(size = (35,1), key = 'out_path'), gui.Stretch(), gui.Button('Записать в файл', button_color='SlateGray', size=(13,1))], 
        # [gui.Text('_' * 65)],
        [gui.Cancel('Выход', button_color="tomato2", size = (47, 1))]    
    ]

    matrix = Matrix([])
    m_window = gui.Window(MATRIX_STR, layout)
    ready = False
    while True:
        event, values = m_window.read(timeout=400)
        if event in (None, gui.WIN_CLOSED):
            m_window.close()
            return None
        if event == 'Загрузить' and not ready:
            m_window['output'].Update('')
            matrix.read_matrix_from_file(values.get('file_path'))
            matrix.outputToConsole()
            ready = True
        if event == 'Найти максимин и минимакс' and matrix.matrix != []:
            tmp = ''
            maxmin = matrix.maxmin()
            minmax = matrix.minmax()
            tmp += f'Максимин: {maxmin}\nМинимакс: {minmax}' + "\n"
            if minmax != maxmin:
                tmp += "Седловой точки нет" + '\n'
            else:
                tmp += "Седловая точка есть" + '\n'
            m_window['text'].Update(tmp)
        if event == 'Найти строго доминируемые' and matrix.matrix != []:
            tmp = ''
            strictly = matrix.strictly_dominated_strategy()
            if strictly[0]: tmp += f"Строго доминируемые для игрока А: {strictly[0]}" + '\n'
            else: tmp += "Нет строго доминируемых для игрока А" + '\n'
            if strictly[1]: tmp += f"Строго доминируемые для игрока B: {strictly[1]}" + '\n'
            else: tmp += "Нет строго доминируемых для игрока B" + '\n'
            m_window['text'].update(tmp)
        if event == 'Найти слабо доминируемые' and matrix.matrix != []:
            tmp = ''
            weakly = matrix.weakly_dominated_strategy()
            if weakly[0]: tmp += f"Cлабо доминируемые для игрока А: {weakly[0]}" + '\n'
            else: tmp += "Нет слабо доминируемых для игрока А" + '\n'
            if weakly[1]: tmp += f"Слабо доминируемые для игрока B: {weakly[1]}" + '\n'
            else: tmp += "Нет слабо доминируемых для игрока B" + '\n'
            m_window['text'].update(tmp)
        if event == 'Найти НЛО стратегии' and matrix.matrix != []:
            tmp = ''
            nlo = matrix.nlo()
            if nlo[0]: tmp += f"НЛО для игрока А: {nlo[0]}" + '\n'
            else: tmp += "Нет НЛО-стратегий игрока А" + '\n'
            if nlo[1]: tmp += f"НЛО для игрока B: {nlo[1]}" + '\n'
            else: tmp += "Нет НЛО-стратегий игрока B" + '\n'
            m_window['text'].update(tmp)
        if event == "Выход":
            gui.popup_ok("Завершение работы программы\nДо новых встреч!")
            m_window.close()     
            return None

def bimatrix_gui():
    gui.theme('Material1')

    layout = [
        [gui.Stretch(), gui.Text(BIMATRIX_STR, font=("Helvetica", 20)), gui.Stretch()],
        [gui.Text('Выберите файл с матрицей', font=("Helvetica", 16))],
        [gui.InputText(size = (38,1), key = 'file_path'), gui.Stretch(), gui.FileBrowse('Открыть файл', button_color='SlateGray', size=(10,1))], 
        [gui.Button('Загрузить', button_color='SlateGray', size = (46, 1))],
        [gui.Text('Доступные виды действий: ', font=("Helvetica", 16))],
        [gui.Button('Найти максимин и минимакс', size=(22,1)), gui.Button("Найти строго доминируемые", size=(22,1))], # action buttons
        [gui.Button("Найти слабо доминируемые", size=(22,1)), gui.Button('Найти НЛО стратегии', size=(22,1))],
        [gui.Button("Найти равновесия по Нешу", size=(22,1))],
        [gui.Text('Введенная матрица:', font=("Helvetica", 16))],           
        [gui.Output(size = (51,7), key = 'output')],
        [gui.Text('Вывод:', font=("Helvetica", 16))],
        [gui.Multiline(key = 'text', size=(51, 7))],
        [gui.Text('Укажите имя файла для вывода', font=("Helvetica", 16))],
        [gui.InputText(size = (36,1), key = 'out_path'), gui.Stretch(), gui.Button('Записать в файл', button_color='SlateGray')], 
        # [gui.Text('_' * 65)],
        [gui.Cancel('Выход', button_color="tomato2", size = (46, 1))]    
    ]

    bimatrix = BiMatrix([])
    m_window = gui.Window(BIMATRIX_STR, layout)
    ready = False
    while True:
        event, values = m_window.read(timeout=400)
        if event in (None, gui.WIN_CLOSED):
            m_window.close()
            return None
        if event == 'Загрузить' and not ready:
            m_window['output'].Update('')
            bimatrix.read_matrix_from_file(values.get('file_path'))
            bimatrix.outputToConsole()
            ready = True
        if event == 'Найти максимин и минимакс' and bimatrix.matrix != []:
            tmp = ''
            maxmin = bimatrix.maxmin()
            tmp += f'Максимин для Игрока А: {maxmin[0]}\nМаксимин для Игрока B: {maxmin[1]}' + "\n"
            m_window['text'].Update(tmp)
        if event == 'Найти строго доминируемые' and bimatrix.matrix != []:
            tmp = ''
            strictly = bimatrix.strictly_dominated_strategy()
            if strictly[0]: tmp += f"Строго доминируемые для игрока А: {strictly[0]}" + '\n'
            else: tmp += "Нет строго доминируемых для игрока А" + '\n'
            if strictly[1]: tmp += f"Строго доминируемые для игрока B: {strictly[1]}" + '\n'
            else: tmp += "Нет строго доминируемых для игрока B" + '\n'
            m_window['text'].update(tmp)
        if event == 'Найти слабо доминируемые' and bimatrix.matrix != []:
            tmp = ''
            weakly = bimatrix.weakly_dominated_strategy()
            if weakly[0]: tmp += f"Cлабо доминируемые для игрока А: {weakly[0]}" + '\n'
            else: tmp += "Нет слабо доминируемых для игрока А" + '\n'
            if weakly[1]: tmp += f"Слабо доминируемые для игрока B: {weakly[1]}" + '\n'
            else: tmp += "Нет слабо доминируемых для игрока B" + '\n'
            m_window['text'].update(tmp)
        if event == 'Найти НЛО стратегии' and bimatrix.matrix != []:
            tmp = ''
            nlo = bimatrix.nlo()
            if nlo[0]: tmp += f"НЛО для игрока А: {nlo[0]}" + '\n'
            else: tmp += "Нет НЛО-стратегий игрока А" + '\n'
            if nlo[1]: tmp += f"НЛО для игрока B: {nlo[1]}" + '\n'
            else: tmp += "Нет НЛО-стратегий игрока B" + '\n'
            m_window['text'].update(tmp)
        if event == 'Найти равновесия по Нешу' and bimatrix.matrix != []:
            tmp = ''
            nash = bimatrix.find_all_pure_nash_eq()
            if nash: tmp += f'Все равновесия по Нешу: {nash}' + '\n'
            else: tmp += "Равновесий по Нешу нет!" + '\n'
            m_window['text'].update(tmp)
        if event == "Выход":
            gui.popup_ok("Завершение работы программы\nДо новых встреч!")
            m_window.close()     
            return None
        
if __name__ == '__main__':
    matrix_gui()