from gui_menu import *
import PySimpleGUI as gui
import sys

TITLE = "Лабораторная работа 1"

def mainwindow():
    gui.theme('DarkPurple6')

    layout =[
        [gui.Text(TITLE, justification='center', font=("Helvetica", 24))],
        [gui.Text('_' * 47)],
        [gui.Text('Какие игры исследуем? ',justification='center', font=("Helvetica", 16))],
        [gui.Button('Матричные'), gui.Button("Биматричные"), gui.Button("Dota2", button_color='black')],
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
            window.close()
            matrix_gui()
        if event == "Биматричные":
            window.close()
            bimatrix_gui()
        if event == "Dota2":
            gui.popup_error("ДАУБИ ДАУБИ ГАГАГА")
            window.close()
        if event == "Выход":
            gui.popup_ok("Завершение работы программы\nДо новых встреч!")
            window.close()     
            return None

if __name__ == '__main__':
    mainwindow()
    sys.exit