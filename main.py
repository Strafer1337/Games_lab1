from matrix import Matrix

matrix = Matrix([])
matrix.read_matrix_from_file('matr5.txt') # имя файла для загрузки матрицы
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
nash = matrix.find_all_pure_nash_eq()
print(
    f"Строго доминируемые для игрока А: {strictly[0]}\nСтрого доминируемые для игрока B: {strictly[1]}")
print(
    f"Слабо доминируемые для игрока А: {weakly[0]}\nСлабо доминируемые для игрока B: {weakly[1]}")
print(f"НЛО для игрока А: {nlo[0]}\nНЛО для игрока B: {nlo[1]}")
print(f"Список равновесий по нешу {nash}")
