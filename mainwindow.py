from gui_menu import *
import PySimpleGUI as gui
import sys

TITLE = "Лабораторная работа 1"

def mainwindow():
    layout =[
        [gui.Text(TITLE, justification='center', font=("Helvetica", 24))],
        [gui.Text('_' * 47)],
        [gui.Text('Какие игры исследуем? ',justification='center', font=("Helvetica", 16))],
        [gui.Button('Матричные'), gui.Button("Биматричные")],
        [gui.Text('_' * 47)],
        [gui.Cancel('Выход')]     
    ]

    window = gui.Window(TITLE, layout)
    while True:
        event, values = window.read(timeout=400)
        if event in (None, gui.WIN_CLOSED):
            window.close()
            return None
        if event == "Матричные":
            matrix_gui()
            window.close()
        if event == "Биматричные":
            bimatrix_gui()
            window.close()
        if event == "Выход":
            gui.popup_ok("Заверншение работы программы\nДо новых встреч!")
            window.close()     
            return None

if __name__ == '__main__':
    mainwindow()
    sys.exit