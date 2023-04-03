class Matrix:
    matrix = []
    size = 0

    def __init__(self, matrix):
        self.matrix = matrix
        #self.size(len(self.matrix), len(self.matrix[0]))

    def output(self):
        """
        Выводит матрицу
        """
        print('\n'.join('\t'.join(map(str, row)) for row in self.matrix))

    def maxmin(self):
        """
        Находит максимин в матричной игре
        """
        max_values = []
        for i in range(len(self.matrix)):
            max_values.append(min(self.matrix[i]))

        return max(max_values)
    
    def minmax(self):
        """
        Находит минимакс в матричной игре
        """
        max_values = []
        for i in range(len(self.matrix)):
            max_values.append(max(self.matrix[i]))
        return min(max_values)
    
    def read_matrix_from_file(self, filename):
        """
        Считывает матрицу из файла
        """
        with open(filename, 'r') as file:
            for line in file:
                row = line.strip().split()  # Разбиваем строку на элементы, используя пробел как разделитель
                self.matrix.append(row)  # Добавляем строку в матрицу
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = int(self.matrix[i][j])
        self.size = (len(self.matrix), len(self.matrix[0]))

    def write_matrix_to_file(self, filename):
        """
        Функция записи матрицы в файл
        """
        with open(filename, 'w') as f:
            for row in self.matrix:
                f.write('\t'.join(str(x) for x in row) + '\n')

    def strictly_dominated_strategy(self):
        """
        Функция поиска строго доминируемой стратегии в матричной игре.
        """
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        result_for_player_a = []
        result_for_player_b = []
        for i in range(rows):
            if all(self.matrix[k][j] > self.matrix[i][j] for k in range(rows) if k != i for j in range(cols)):
                result_for_player_a.append(f"Стратерия a{i+1}")
        for j in range(cols):        
            if all(self.matrix[i][k] > self.matrix[i][j] for k in range(cols) if k != j for i in range(rows)):
                result_for_player_b.append(f"Стратерия b{i+1}")            
        return result_for_player_a, result_for_player_b
    
    def weakly_dominated_strategy(self):
        """
        Функция поиска слабо доминируемой стратегии в матричной игре.
        """
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        result_for_player_a = []
        result_for_player_b = []
        for i in range(rows):
            if all(self.matrix[k][j] >= self.matrix[i][j] for k in range(rows) if k != i for j in range(cols)) and \
                any(self.matrix[k][j] == self.matrix[i][j] for k in range(rows) if k != i for j in range(cols)):
                    result_for_player_a.append(f"Стратерия a{i+1}")    
        for j in range(cols):
            if all(self.matrix[i][k] >= self.matrix[i][j] for k in range(cols) if k != j for i in range(rows)) and \
                any(self.matrix[i][k] == self.matrix[i][j] for k in range(cols) if k != j for i in range(rows)):
                    result_for_player_b.append(f"Стратерия b{i+1}")              
        return result_for_player_a, result_for_player_b





    


    






