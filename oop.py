class Board:
    dct_coords = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7'}
    lst_figures = ['R', 'B', 'N', 'Q', 'K']
    figure_coords = ''
    initial_board = [
        ['bR', 'bN', 'bB', 'bQ', 'bK', 'bB', 'bN', 'bR'],
        ['bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP', 'bP'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['wR', 'wN', 'wB', 'wQ', 'wK', 'wB', 'wN', 'wR'],
        ['wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP', 'wP']
    ]

    def display_board(self, field):  # Вывод графической части
        letters = ' ABCDEFGH '
        letters = f' '.join(letters)
        a = ''
        a += f"{' ' + letters}\n"
        for i, row in enumerate(field):
            if i + 1 == 10:
                a += f"{str(8 - i)} {' '.join(row)}\n"
                break
            a += f" {str(8 - i)} {' '.join(row)}\n"
        return a

"""    def make_move(self, row, col, fig): НЕ ДОДЕЛАЛ, НЕ ТРОГАТЬ ПОКА
        if fig == 'R':

        self.initial_board[row][col] = fig"""

