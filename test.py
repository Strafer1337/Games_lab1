# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         # Создаем кнопку
#         self.button = QPushButton('Открыть окно', self)

#         # Привязываем событие нажатия на кнопку к методу open_dialog
#         self.button.clicked.connect(self.open_dialog)

#     def open_dialog(self):
#         # Создаем новое диалоговое окно
#         dialog = QDialog(self)

#         # Устанавливаем заголовок диалогового окна
#         dialog.setWindowTitle('Новое окно')

#         # Показываем диалоговое окно и закрываем текущую форму
#         dialog.exec_()
#         self.close()

# if __name__ == '__main__':
#     app = QApplication([])
#     window = MainWindow()
#     window.show()
#     app.exec_()
