from gui_menu import *
import PySimpleGUI as gui
import sys

TITLE = "Лабораторная работа 1"
def mainwindow():
    gui.theme('LightGreen6')

    layout =[
        [gui.Text(TITLE, justification='center', font=("Helvetica", 24))],
        [gui.Stretch(), gui.Image(filename='daubi.png', size=(300,300)), gui.Stretch()],
        [gui.Stretch(), gui.Text('Какие игры исследуем? ',justification='center', font=("Helvetica", 16)), gui.Stretch()],
        [gui.Button('Матричные', size = (20, 1)), gui.Button("Биматричные", size = (20, 1))],
        [gui.Button("Dota2", button_color='black', size = (42, 1))],
        # [gui.Text('_' * 47)],
        [gui.Cancel('Выход', button_color="tomato2", size = (42, 1))]     
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