from matrix import Matrix

class BiMatrix(Matrix):
    # matrix = []

    def read_matrix_from_file(self, filename):
        """
        Считывает матрицу из файла
        """
        with open(filename, 'r') as file:
            for line in file:
                # Разбиваем строку на элементы, используя пробел как разделитель
                row = line.strip().split()
                self.matrix.append(row)  # Добавляем строку в матрицу
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] =  self.matrix[i][j].split(",")
                self.matrix[i][j][0] = int(self.matrix[i][j][0])
                self.matrix[i][j][1] = int(self.matrix[i][j][1])
                # self.matrix[i][j] = list(self.matrix[i][j])
                # self.matrix[i][j].pop(1)
                # self.matrix[i][j][0] = int(self.matrix[i][j][0])
                # self.matrix[i][j][1] = int(self.matrix[i][j][1])
        self.size = (len(self.matrix), len(self.matrix[0]))

    def find_all_pure_nash_eq(self):
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        nash_eqs = []
        
        for i in range(rows):
            for j in range(cols):
                is_nash_eq = True
                for k in range(rows):
                    if self.matrix[k][j][0] > self.matrix[i][j][0] and \
                        self.matrix[k][j][1] > self.matrix[i][j][1]:
                        is_nash_eq = False
                        break
                if is_nash_eq:
                    for l in range(cols):
                        if self.matrix[i][l][0] > self.matrix[i][j][0] and \
                            self.matrix[i][l][1] > self.matrix[i][j][1]:
                            is_nash_eq = False
                            break
                if is_nash_eq:
                    nash_eqs.append((f'a{i+1}', f'b{j+1}'))        
        return nash_eqs
    
    def maxmin(self):
        """
        Находит максимин в биматричной игре
        """
        def maxminForA(matrix):
            """Максимин для игрока А"""
            minByRow = []
            mins = []
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    minByRow.append(matrix[i][j][0])
                mins.append(min(minByRow))
            return max(mins)
        
        def maxminForB(matrix):
            """Максимин для игрока B"""
            minByCol = []
            mins = []
            for j in range(len(matrix[0])):
                for i in range(len(matrix)):
                    minByCol.append(matrix[i][j][1])
                mins.append(min(minByCol))
            return max(mins) 
                   
        return (maxminForA(self.matrix), maxminForB(self.matrix))
    
    def strictly_dominated_strategy(self):
        """
        Функция поиска строго доминируемой стратегии в матричной игре.
        """
        rows = len(self.matrix)
        cols = len(self.matrix[0])
        result_for_player_a = []
        result_for_player_b = []
        for i in range(rows):
            # if_strictly_dominated = False
            for k in range(rows):
                if k == i:
                    continue
                elif all(self.matrix[k][j][0] > self.matrix[i][j][0] for j in range(cols)):
                    result_for_player_a.append(f"a{i+1}")
                    break           
        for j in range(cols):
            for k in range(cols):
                if k == j:
                    continue
                elif all(self.matrix[i][k][1] > self.matrix[i][j][1] for i in range(rows)):
                    result_for_player_b.append(f"b{j+1}")
                    break
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
            for k in range(rows):
                if k == i:
                    continue
                elif all(self.matrix[k][j] >= self.matrix[i][j] for j in range(cols)) and \
                        any(self.matrix[k][j] == self.matrix[i][j] for j in range(cols)):
                    result_for_player_a.append(f"a{i+1}")
                    break
        for j in range(cols):
            for k in range(cols):
                if k==j:
                    continue
                elif all(self.matrix[i][k] >= self.matrix[i][j] for i in range(rows)) and \
                    any(self.matrix[i][k] == self.matrix[i][j] for i in range(rows)):
                    result_for_player_b.append(f"b{j+1}")
        return result_for_player_a, result_for_player_b