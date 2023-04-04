from bimatrix import BiMatrix
from matrix import Matrix

def test_for_solo_matrix():
    matrix = Matrix([])
    matrix.read_matrix_from_file('matr1.txt') # имя файла для загрузки матрицы
    matrix.output()
    print(f'Размер матрицы: {matrix.size}')
    maxmin = matrix.maxmin()
    minmax = matrix.minmax()
    print(f'Максимин: {maxmin}\nМинимакс: {minmax}')
    print("Седловой точки нет") if minmax != maxmin else print("Седловая точка есть")
    # matrix.write_matrix_to_file('out.txt')
    strictly = matrix.strictly_dominated_strategy()
    weakly = matrix.weakly_dominated_strategy()
    nlo = matrix.nlo()
    # nash = matrix.find_all_pure_nash_eq()
    print(
        f"Строго доминируемые для игрока А: {strictly[0]}\nСтрого доминируемые для игрока B: {strictly[1]}")
    print(
        f"Слабо доминируемые для игрока А: {weakly[0]}\nСлабо доминируемые для игрока B: {weakly[1]}")
    print(f"НЛО для игрока А: {nlo[0]}\nНЛО для игрока B: {nlo[1]}")
    # print(f"Список равновесий по нешу {nash}")

def test_for_bimatrix():
    # test_bimatr = [[(1,1), (2,2), (3,3)], [(1,1), (2,2), (3,3)], [(1,1), (2,2), (3,3)]]
    bimatrix = BiMatrix([])
    bimatrix.read_matrix_from_file('prisoners.txt')
    bimatrix.output()
    print(f'Равновесия Неша: {bimatrix.find_all_pure_nash_eq()}')

def test_read(filename):
    matrix = []
    with open(filename, 'r') as file:
        for line in file:
            # Разбиваем строку на элементы, используя пробел как разделитель
            row = line.strip().split()
            matrix.append(row)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] =  matrix[i][j].split(",")
            matrix[i][j][0] = int(matrix[i][j][0])
            matrix[i][j][1] = int(matrix[i][j][1])
    print(matrix)



if __name__ == '__main__':
    test_for_bimatrix()
    # test_read('prisoners.txt')

