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