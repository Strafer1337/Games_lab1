import sys
import os.path
from bimatrix import BiMatrix
from matrix import Matrix
from random import randint

# TODO добавить удаление биматриц

def menu():
    print("\t\t---МЕНЮ---\n\tДоступные виды матриц:\n\t1. Матричная игра.",
          "\n\t2. Биматричная игра.\n\t3. Выход из программы. ")
    command = 0
    while command != 3:
        command = int(input("\n\tС какими матрицами работаем? "))
        match command:
            case 1:
                print("\n\tРаботаем с Матричными играми!")
                return 1
            case 2:
                print("\n\tРаботаем с Биматричными играми!")
                return 2 
            case 3:
                print("\nРановато вы...\nДо свидания!")
                sys.exit
            case _:
                print("\n\tНет такой команды!")

def menu_for_matrix():
    print("\n\tДля начала введем матрицу.\n\tДоступные виды ввода:\n\t1. Из консоли.\n\t2. Из файла.",
          "\n\t3. Рандомные числа.\n\t4. Выход из программы.")
    command = 0
    while command != 4:
        command = int(input("\nКак вводим матрицу? "))
        match command:
            case 1:
                n = int(input("\nВведите количество стратегий первого игрока: "))
                m = int(input("Введите количество стратегий второго игрока: "))
                print("\t\tВведите матрицу:")
                in_matrix = [list(map(int, input().split())) for i in range(n)]
                matrix = Matrix(in_matrix)
                print("\n\tВведенная матрица:")
                matrix.outputToConsole()
                return matrix 
            case 2:
                filename = str(input("\nВведите имя файла с матрицей: ")) + ".txt"
                while not os.path.exists(filename):
                    print("\nНеверное имя файла!")
                    filename = input("Введите верное имя файла: ") + ".txt"
                matrix = Matrix([])
                matrix.read_matrix_from_file(filename)
                print("\n\tВведенная матрица:")
                matrix.outputToConsole()
                return matrix
            case 3:
                n = int(input("\nВведите количество стратегий первого игрока: "))
                m = int(input("Введите количество стратегий второго игрока: "))
                low = int(input("Введите минимальное число: "))
                high = int(input("Введите максимальное число: "))
                in_matrix = []
                for i in range(n):
                    row = []
                    for j in range(m):
                        row.append(randint(low, high))
                    in_matrix.append(row)
                matrix = Matrix(in_matrix)
                print("\n\tВведенная матрица:")
                matrix.outputToConsole()
                return matrix
            case 4:
                print("\n\tХоть бы матрицу ввели...\n\tДо свидания!")
                return []
            case _:
                print("\n\tНет такой команды!")

def menu_for_bimatrix():
    print("\n\tДля начала введем матрицу.\n\tДоступные виды ввода:\n\t1. Из консоли.\n\t2. Из файла.",
          "\n\t3. Рандомные числа.\n\t4. Выход из программы.")
    command = 0
    while command != 4:
        command = int(input("\nКак вводим матрицу? "))
        match command:
            case 1:
                n = int(input("\nВведите количество стратегий первого игрока: "))
                m = int(input("Введите количество стратегий второго игрока: "))
                print("\tВведите матрицу:")
                in_matrix = [list(map(str, input().split())) for i in range(n)]
                for i in range(len(in_matrix)):
                    for j in range(len(in_matrix[i])):
                        in_matrix[i][j] =  in_matrix[i][j].split(",")
                        in_matrix[i][j][0] = int(in_matrix[i][j][0])
                        in_matrix[i][j][1] = int(in_matrix[i][j][1])
                matrix = BiMatrix(in_matrix)
                matrix.outputToConsole()
                return matrix 
            case 2:
                filename = input("\nВведите имя файла с матрицей: ") + ".txt"
                while not os.path.exists(filename):
                    print("\nНеверное имя файла!")
                    filename = input("Введите верное имя файла: ") + ".txt"
                matrix = BiMatrix([])
                matrix.read_matrix_from_file(filename)
                print("\n\tВведенная матрица:")
                matrix.outputToConsole()
                return matrix
            case 3:
                n = int(input("\nВведите количество стратегий первого игрока: "))
                m = int(input("Введите количество стратегий второго игрока: "))
                low = int(input("Введите минимальное число: "))
                high = int(input("Введите максмальное число: "))
                in_matrix = []
                for i in range(n):
                    row = []
                    for j in range(m):
                        row.append([randint(low, high), randint(low, high)])
                    in_matrix.append(row)
                matrix = BiMatrix(in_matrix)
                print("\n\tВведенная матрица:")
                matrix.outputToConsole()
                return matrix
            case 4:
                print("\n\tХоть бы матрицу ввели...\n\tДо свидания!")
                return []
            case _:
                print("\n\tНет такой команды!")

def actions_for_matrix(matrix):
    mode = 0
    while mode != 6:
        print("\n\tЧто делаем дальше?\n\t1. Найти максимин и минимакс.\n\t2. Найти строго доминируемые стратегии.\n",
              "\t3. Найти слабо доминируемые стратегии.\n\t4. Найти НЛО-стратегии.\n\t5. Записать матрицу в файл.\n\t6. Завершить работу программы.")
        mode = int(input("\n\tВыберите действие: "))
        match mode:
            case 1:
                maxmin = matrix.maxmin()
                minmax = matrix.minmax()
                print(f'Максимин: {maxmin}\nМинимакс: {minmax}')
                print("Седловой точки нет") if minmax != maxmin else print("Седловая точка есть")
            case 2:
                strictly = matrix.strictly_dominated_strategy()
                print(f"Строго доминируемые для игрока А: {strictly[0]}") if strictly[0] \
                    else print("Нет строго доминируемых для игрока А")
                print(f"Строго доминируемые для игрока B: {strictly[1]}") if strictly[1] \
                    else print("Нет строго доминируемых для игрока B")
            case 3:
                weakly = matrix.weakly_dominated_strategy()
                print(f"Слабо доминируемые игрока А: {weakly[0]}") if weakly[0]\
                    else print("Нет слабо доминируемых игрока А")
                print(f"Слабо доминируемые игрока B: {weakly[1]}") if weakly[1]\
                    else print("Нет слабо доминируемых игрока B")
            case 4:
                nlo = matrix.nlo()
                print(f"НЛО для игрока А: {nlo[0]}") if nlo[0] else print("Нет НЛО-стратегий игрока А")
                print(f"НЛО для игрока B: {nlo[1]}") if nlo[1] else print("Нет НЛО-стратегий игрока B")
            case 5:
                filename = input("\nВведите имя файла для записи: ") + ".txt"
                matrix.write_matrix_to_file(filename)
                print(f'Матрица записана в файл {filename}!')
            case 6:
                print("\n\tЗавершение работы.\n\tДо свидания!")
                sys.exit
            case _:
                print("\n\tНет такой команды!")

def actions_for_bimatrix(matrix):
    mode = 0
    while mode != 7:
        print("\n\tЧто делаем дальше?\n\t1. Найти максимины.\n\t2. Найти строго доминируемые стратегии.\n",
              "\t3. Найти слабо доминируемые стратегии.\n\t4. Найти НЛО-стратегии.",
              "\n\t5. Найти все равновесия по Нешу.\n\t6. Записать матрицу в файл.\n\t7. Завершить работу программы.")
        mode = int(input("\n\tВыберите действие: "))
        match mode:
            case 1:
                maxmin = matrix.maxmin()
                print(f'Максимин для Игрока А: {maxmin[0]}\nМаксимин для Игрока B: {maxmin[1]}')
            case 2:
                strictly = matrix.strictly_dominated_strategy()
                print(f"Строго доминируемые для игрока А: {strictly[0]}") if strictly[0] \
                    else print("Нет строго доминируемых для игрока А")
                print(f"Строго доминируемые для игрока B: {strictly[1]}") if strictly[1] \
                    else print("Нет строго доминируемых для игрока B")            
            case 3:
                weakly = matrix.weakly_dominated_strategy()
                print(f"Слабо доминируемые игрока А: {weakly[0]}") if weakly[0]\
                    else print("Нет слабо доминируемых игрока А")
                print(f"Слабо доминируемые игрока B: {weakly[1]}") if weakly[1]\
                    else print("Нет слабо доминируемых игрока B")
            case 4:
                nlo = matrix.nlo()
                print(f"НЛО для игрока А: {nlo[0]}") if nlo[0] else print("Нет НЛО-стратегий игрока А")
                print(f"НЛО для игрока B: {nlo[1]}") if nlo[1] else print("Нет НЛО-стратегий игрока B")
            case 5:
                nash = matrix.find_all_pure_nash_eq()
                print(f'Все равновесия по Нешу: {nash}') if nash else print("Равновесий по Нешу нет!")
            case 6:
                filename = input("\nВведите имя файла для записи: ") + ".txt"
                matrix.write_matrix_to_file(filename)
                print(f'Матрица записана в файл {filename}!')
            case 7:
                print("\n\tЗавершение работы.\n\tДо свидания!")
                sys.exit