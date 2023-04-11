from bimatrix import BiMatrix
from matrix import Matrix
import PySimpleGUI as gui

MATRIX_STR = "Матричные игры"
BIMATRIX_STR = "Биматричные игры"

def matrix_gui():
    layout = [
        [gui.Text(MATRIX_STR, justification='center', font=("Helvetica", 24))],
        [gui.Text('_' * 47)],
        [gui.Text('Доступные виды действий: ',justification='center', font=("Helvetica", 16))],
        [gui.Button('Матричные'), gui.Button("Биматричные")], # action buttons
        [gui.Text('_' * 47)],
        [gui.Text('_' * 47)],
        [gui.Text('_' * 47)],
        [gui.Text('_' * 47)],
        [gui.Text('_' * 47)],
        [gui.Cancel('Выход')]     
    ]

    m_window = gui.Window(MATRIX_STR, layout)
    while True:
        event, values = m_window.read(timeout=400)
        if event in (None, gui.WIN_CLOSED):
            m_window.close()
            return None
        if event == "Выход":
            gui.popup_ok("Заверншение работы программы\nДо новых встреч!")
            m_window.close()     
            return None

def bimatrix_gui():
    pass