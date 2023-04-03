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
rows = 5
strategy_i = [0] * rows
print(strategy_i)

def nash_equilibrium(matrix):
    """
    Функция поиска равновесия по Нэшу в матричной игре.
    
    matrix - матрица выигрышей игроков.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            strategy_i = [0] * rows
            strategy_j = [0] * cols
            strategy_i[i] = 1
            strategy_j[j] = 1
            if all(matrix[i][k] <= matrix[i][j] for k in range(cols) if k != j) and \
                all(matrix[k][j] <= matrix[i][j] for k in range(rows) if k != i):
                return (strategy_i, strategy_j)
    return None

def find_all_pure_nash_equilibria(matrix):
    m = len(matrix)
    n = len(matrix[0])
    nash_eqs = []
    
    for i in range(m):
        for j in range(n):
            is_nash_eq = True
            for k in range(m):
                if matrix[k][j] > matrix[i][j]:
                    is_nash_eq = False
                    break
            if is_nash_eq:
                for l in range(n):
                    if matrix[i][l] > matrix[i][j]:
                        is_nash_eq = False
                        break
            if is_nash_eq:
                nash_eqs.append((i, j))
    
    return nash_eqs


matrix = [[3, 1, 2], [2, 4, 1], [1, 2, 3]]
nash = nash_equilibrium(matrix)
nash2 = find_all_pure_nash_equilibria(matrix)
if nash:
    print("Найдено равновесие по Нэшу: ", nash)
    print("Найдено равновесие по Нэшу: ", nash2)
else:
    print("Равновесие по Нэшу не найдено")

