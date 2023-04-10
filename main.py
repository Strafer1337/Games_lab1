from bimatrix import BiMatrix
# from pyfiglet import Figlet
from matrix import Matrix
from menu import *

if __name__ == '__main__':
    # prog_name = Figlet(font='big')
    # print(prog_name.renderText('Games LR1'))
    mode = menu()
    match mode:
        case 1:
            matrix = Matrix([])
            matrix = menu_for_matrix()
            if matrix.matrix == [[]]:
                print("\n\tПустая матрица! Пока!")
                sys.exit
            else:
                actions_for_matrix(matrix)
        case 2:
            bimatrix = BiMatrix([])
            bimatrix = menu_for_bimatrix()
            if bimatrix.matrix == [[]]:
                print("\n\tПустая матрица! Пока!")
                sys.exit
            else:
                actions_for_bimatrix(bimatrix)
    # test_for_solo_matrix()

