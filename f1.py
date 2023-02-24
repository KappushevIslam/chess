from colorama import init, Fore


def make_board():  # формируем игровое поле
    board = []
    rows = 8
    columns = 8
    init(autoreset=True)
    for i in range(rows):
        row = []
        for j in range(columns):
            if i == 1 or i == 6:
                row.append('p')
            elif (i == 0 or i == 7) and (j == 0 or j == 7):
                row.append('R')
            elif (i == 0 or i == 7) and (j == 1 or j == 6):
                row.append('N')
            elif (i == 0 or i == 7) and (j == 2 or j == 5):
                row.append('B')
            elif (i == 0 or i == 7) and j == 3:
                row.append('Q')
            elif (i == 0 or i == 7) and j == 4:
                row.append('K')
            else:
                row.append('.')
        board.append(row)
    for i in range(rows):
        for j in range(columns):
            if i == 0 or i == 1:
                board[i][j] = Fore.LIGHTYELLOW_EX + board[i][j]
            elif i == 6 or i == 7:
                board[i][j] = Fore.RED + board[i][j]
            else:
                board[i][j] = Fore.WHITE + board[i][j]
    return board


def display_board(field):  # Вывод графической части
    letters = ' ABCDEFGH '
    letters = f'{Fore.LIGHTWHITE_EX} '.join(letters)
    a = ''
    a += f"{' ' + letters}\n"
    for i, row in enumerate(field):
        if i + 1 == 10:
            a += f"{Fore.LIGHTWHITE_EX + str(8 - i)} {' '.join(row)}\n"
            break
        a += f" {Fore.LIGHTWHITE_EX + str(8 - i)} {' '.join(row)}\n"
    return a


# Координаты: столбец + строка
initial_board = make_board()
move_counter = 0
dct_coords = {'a': '0', 'b': '1', 'c': '2', 'd': '3', 'e': '4', 'f': '5', 'g': '6', 'h': '7'}
lst_figures = ['R', 'B', 'N', 'Q', 'K']
figure_coords = ''
while True:
    print(display_board(initial_board))
    pawn_col = ''
    flag = 0
    if move_counter % 2 == 0:
        move = input('Ход красных: ')
    else:
        move = input('Ход желтых: ')
    if 'x' in move:
        flag = 1
        move = move.replace('x', '')
        if move[0] not in lst_figures:
            pawn_col = dct_coords[move[0]]
            move = move.replace(move[0], '')
    if move[0] == 'N':
        n_changes_flag = 0
        move = move.replace(move[0], '')
        move = move.replace(move[0], dct_coords[move[0]])
        row = int(move[1])
        col = int(move[0])
        if move_counter % 2 == 0:
            if '[93m' in initial_board[8 - row][col] and flag == 0:
                print('Невозможный ход конем. Сделайте другой ход')
                continue
            if 8 - row + 2 < 9 and col + 1 < 9:
                if 'N' in initial_board[8 - row + 2][col + 1] and '[31m' in initial_board[8 - row + 2][col + 1]:
                    initial_board[8 - row + 2][col + 1] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row + 2 < 9 and col - 1 > -1:
                if 'N' in initial_board[8 - row + 2][col - 1] and '[31m' in initial_board[8 - row + 2][col - 1]:
                    initial_board[8 - row + 2][col - 1] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row - 2 > -1 and col + 1 < 9:
                if 'N' in initial_board[8 - row - 2][col + 1] and '[31m' in initial_board[8 - row - 2][col + 1]:
                    initial_board[8 - row - 2][col + 1] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row - 2 > -1 and col - 1 > -1:
                if 'N' in initial_board[8 - row - 2][col - 1] and '[31m' in initial_board[8 - row - 2][col - 1]:
                    initial_board[8 - row - 2][col - 1] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row + 1 < 9 and col + 2 < 9:
                if 'N' in initial_board[8 - row + 1][col + 2] and '[31m' in initial_board[8 - row + 1][col + 2]:
                    initial_board[8 - row + 1][col + 2] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row + 1 < 9 and col - 2 > -1:
                if 'N' in initial_board[8 - row + 1][col - 2] and '[31m' in initial_board[8 - row + 1][col - 2]:
                    initial_board[8 - row + 1][col - 2] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row - 1 > -1 and col + 2 < 9:
                if 'N' in initial_board[8 - row - 1][col + 2] and '[31m' in initial_board[8 - row - 1][col + 2]:
                    initial_board[8 - row - 1][col + 2] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row - 1 > -1 and col - 2 > -1:
                if 'N' in initial_board[8 - row - 1][col - 2] and '[31m' in initial_board[8 - row - 1][col - 2]:
                    initial_board[8 - row - 1][col - 2] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if n_changes_flag == 0:
                print('Невозможный ход конём. Сделайте другой ход')
                continue
            initial_board[8 - row][col] = Fore.RED + 'N' + Fore.RESET
        else:
            if '[31m' in initial_board[8 - row][col] and flag == 0:
                print('Невозможный ход конем. Сделайте другой ход')
                continue
            if 8 - row + 2 < 9 and col + 1 < 9:
                if 'N' in initial_board[8 - row + 2][col + 1] and '[93m' in initial_board[8 - row + 2][col + 1]:
                    initial_board[8 - row + 2][col + 1] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row + 2 < 9 and col - 1 > -1:
                if 'N' in initial_board[8 - row + 2][col - 1] and '[93m' in initial_board[8 - row + 2][col - 1]:
                    initial_board[8 - row + 2][col - 1] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row - 2 > -1 and col + 1 < 9:
                if 'N' in initial_board[8 - row - 2][col + 1] and '[93m' in initial_board[8 - row - 2][col + 1]:
                    initial_board[8 - row - 2][col + 1] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row - 2 > -1 and col - 1 > -1:
                if 'N' in initial_board[8 - row - 2][col - 1] and '[93m' in initial_board[8 - row - 2][col - 1]:
                    initial_board[8 - row - 2][col - 1] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row + 1 < 9 and col + 2 < 9:
                if 'N' in initial_board[8 - row + 1][col + 2] and '[93m' in initial_board[8 - row + 1][col + 2]:
                    initial_board[8 - row + 1][col + 2] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row + 1 < 9 and col - 2 > -1:
                if 'N' in initial_board[8 - row + 1][col - 2] and '[93m' in initial_board[8 - row + 1][col - 2]:
                    initial_board[8 - row + 1][col - 2] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row - 1 > -1 and col + 2 < 9:
                if 'N' in initial_board[8 - row - 1][col + 2] and '[93m' in initial_board[8 - row - 1][col + 2]:
                    initial_board[8 - row - 1][col + 2] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if 8 - row - 1 > -1 and col - 2 > -1:
                if 'N' in initial_board[8 - row - 1][col - 2] and '[93m' in initial_board[8 - row - 1][col - 2]:
                    initial_board[8 - row - 1][col - 2] = Fore.WHITE + '.'
                    n_changes_flag = 1
            if n_changes_flag == 0:
                print('Невозможный ход конём. Сделайте другой ход')
                continue
            initial_board[8 - row][col] = Fore.LIGHTYELLOW_EX + 'N' + Fore.RESET
    elif move[0] == 'B':
        b_changes_flag = 0
        move = move.replace(move[0], '')
        move = move.replace(move[0], dct_coords[move[0]])
        row = int(move[1])
        col = int(move[0])
        if move_counter % 2 == 0:
            if '[93m' in initial_board[8 - row][col] and flag == 0:
                print('Невозможный ход ладьёй. Сделайте другой ход')
                continue
            for i in range(1, 8):
                if 8 - row + i < 8 and col + i < 8:
                    if '[31m' in initial_board[8 - row + i][col + i] and 'B' in initial_board[8 - row + i][col + i]:
                        initial_board[8 - row + i][col + i] = Fore.WHITE + '.'
                        b_changes_flag = 1
                    elif '.' not in initial_board[8 - row + i][col + i]:
                        break
            for i in range(1, 8):
                if 8 - row - i >= 0 and col - i >= 0:
                    if '[31m' in initial_board[8 - row - i][col - i] and 'B' in initial_board[8 - row - i][col - i]:
                        initial_board[8 - row - i][col - i] = Fore.WHITE + '.'
                        b_changes_flag = 1
                    elif '.' not in initial_board[8 - row - i][col - i]:
                        break
            for i in range(1, 8):
                if 8 - row + i < 8 and col - i >= 0:
                    if '[31m' in initial_board[8 - row + i][col - i] and 'B' in initial_board[8 - row + i][col - i]:
                        initial_board[8 - row + i][col - i] = Fore.WHITE + '.'
                        b_changes_flag = 1
                    elif '.' not in initial_board[8 - row + i][col - i]:
                        break
            for i in range(1, 8):
                if 8 - row - i >= 0 and col + i < 8:
                    print(8 - row, col, 8 - row - i, col + i)
                    if '[31m' in initial_board[8 - row - i][col + i] and 'B' in initial_board[8 - row - i][col + i]:
                        initial_board[8 - row - i][col + i] = Fore.WHITE + '.'
                        b_changes_flag = 1
                    elif '.' not in initial_board[8 - row - i][col + i]:
                        break
            if b_changes_flag == 0:
                print('Невозможный ход слоном. Сделайте другой ход')
                continue
            initial_board[8 - row][col] = Fore.RED + 'B' + Fore.RESET
        else:
            if '[31m' in initial_board[8 - row][col] and flag == 0:
                print('Невозможный ход ладьёй. Сделайте другой ход')
                continue
            for i in range(1, 8):
                if 8 - row + i < 8 and col + i < 8:
                    if '[93m' in initial_board[8 - row + i][col + i] and 'B' in initial_board[8 - row + i][col + i]:
                        initial_board[8 - row + i][col + i] = Fore.WHITE + '.'
                        b_changes_flag = 1
                    elif '.' not in initial_board[8 - row + i][col + i]:
                        break
            for i in range(1, 8):
                if 8 - row - i >= 0 and col - i >= 0:
                    print(8 - row, col, 8 - row - i, col - i)
                    if '[93m' in initial_board[8 - row - i][col - i] and 'B' in initial_board[8 - row - i][col - i]:
                        initial_board[8 - row - i][col - i] = Fore.WHITE + '.'
                        b_changes_flag = 1
                    elif '.' not in initial_board[8 - row - i][col - i]:
                        break
            for i in range(1, 8):
                if 8 - row + i < 8 and col - i >= 0:
                    print(8 - row, col, 8 - row + i, col - i)
                    if '[93m' in initial_board[8 - row + i][col - i] and 'B' in initial_board[8 - row + i][col - i]:
                        initial_board[8 - row + i][col - i] = Fore.WHITE + '.'
                        b_changes_flag = 1
                    elif '.' not in initial_board[8 - row + i][col - i]:
                        break
            for i in range(1, 8):
                if 8 - row - i >= 0 and col + i < 8:
                    print(8 - row, col, 8 - row - i, col + i)
                    if '[93m' in initial_board[8 - row - i][col + i] and 'B' in initial_board[8 - row - i][col + i]:
                        initial_board[8 - row - i][col + i] = Fore.WHITE + '.'
                        b_changes_flag = 1
                    elif '.' not in initial_board[8 - row - i][col + i]:
                        break
            if b_changes_flag == 0:
                print('Невозможный ход слоном. Сделайте другой ход')
                continue
            initial_board[8 - row][col] = Fore.LIGHTYELLOW_EX + 'B' + Fore.RESET
    elif move[0] == 'R':
        r_changes_flag = 0
        move = move.replace(move[0], '')
        move = move.replace(move[0], dct_coords[move[0]])
        row = int(move[1])
        col = int(move[0])
        if move_counter % 2 == 0:
            if '[93m' in initial_board[8 - row][col] and flag == 0:
                print('Невозможный ход ладьёй. Сделайте другой ход')
                continue
            for i in range(8 - row + 1, 9):
                print(i, col)
                try:
                    if 'R' in initial_board[i][col] and '[31m' in initial_board[i][col]:
                        initial_board[i][col] = Fore.WHITE + '.'
                        r_changes_flag = 1
                    elif '.' not in initial_board[i][col] and 'R' not in initial_board[i][col]:
                        break
                except IndexError:
                    break
            for i in range(8 - row - 1, -1, -1):
                try:
                    if 'R' in initial_board[i][col] and '[31m' in initial_board[i][col]:
                        initial_board[i][col] = Fore.WHITE + '.'
                        r_changes_flag = 1
                    elif '.' not in initial_board[i][col] and 'R' not in initial_board[i][col]:
                        break
                except IndexError:
                    break
            for i in range(col + 1, 9):
                try:
                    if 'R' in initial_board[8 - row][i] and '[31m' in initial_board[8 - row][i]:
                        initial_board[8 - row][i] = Fore.WHITE + '.'
                        r_changes_flag = 1
                    elif '.' not in initial_board[8 - row][i] and 'R' not in initial_board[8 - row][i]:
                        break
                except IndexError:
                    break
            for i in range(col - 1, -1, -1):
                try:
                    if 'R' in initial_board[8 - row][i] and '[31m' in initial_board[8 - row][i]:
                        initial_board[8 - row][i] = Fore.WHITE + '.'
                        r_changes_flag = 1
                    elif '.' not in initial_board[8 - row][i] and 'R' not in initial_board[8 - row][i]:
                        break
                except IndexError:
                    break
            if r_changes_flag == 0:
                print('Невозможный ход ладьёй. Сделайте другой ход 1')
                continue
            initial_board[8 - row][col] = Fore.RED + 'R' + Fore.RESET
        else:
            if '[31m' in initial_board[8 - row][col] and flag == 0:
                print('Невозможный ход ладьёй. Сделайте другой ход')
                continue
            for i in range(8 - row + 1, 9):
                try:
                    if 'R' in initial_board[i][col] and '[93m' in initial_board[i][col]:
                        initial_board[i][col] = Fore.WHITE + '.'
                        r_changes_flag = 1
                    elif '.' not in initial_board[i][col] and 'R' not in initial_board[i][col]:
                        break
                except IndexError:
                    break
            for i in range(8 - row - 1, -1, -1):
                try:
                    if 'R' in initial_board[i][col] and '[93m' in initial_board[i][col]:
                        initial_board[i][col] = Fore.WHITE + '.'
                        r_changes_flag = 1
                    elif '.' not in initial_board[i][col] and 'R' not in initial_board[i][col]:
                        break
                except IndexError:
                    break
            for i in range(col + 1, 9):
                try:
                    if 'R' in initial_board[8 - row][i] and '[93m' in initial_board[8 - row][i]:
                        initial_board[8 - row][i] = Fore.WHITE + '.'
                        r_changes_flag = 1
                    elif '.' not in initial_board[8 - row][i] and 'R' not in initial_board[8 - row][i]:
                        break
                except IndexError:
                    break
            for i in range(col - 1, -1, -1):
                try:
                    if 'R' in initial_board[8 - row][i] and '[93m' in initial_board[8 - row][i]:
                        initial_board[8 - row][i] = Fore.WHITE + '.'
                        r_changes_flag = 1
                    elif '.' not in initial_board[8 - row][i] and 'R' not in initial_board[8 - row][i]:
                        break
                except IndexError:
                    break
            if r_changes_flag == 0:
                print('Невозможный ход ладьёй. Сделайте другой ход')
                continue
            initial_board[8 - row][col] = Fore.LIGHTYELLOW_EX + 'R' + Fore.RESET
    elif move[0] == 'Q':
        q_changes_flag = 0
        move = move.replace(move[0], '')
        move = move.replace(move[0], dct_coords[move[0]])
        row = int(move[1])
        col = int(move[0])
        if move_counter % 2 == 0:
            if '[93m' in initial_board[8 - row][col] and flag == 0:
                print('Невозможный ход Ферзем. Сделайте другой ход')
                continue
            for i in range(8 - row + 1, 9):
                print(i, col)
                try:
                    if 'Q' in initial_board[i][col] and '[31m' in initial_board[i][col]:
                        initial_board[i][col] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[i][col] and 'Q' not in initial_board[i][col]:
                        break
                except IndexError:
                    break
            for i in range(8 - row - 1, -1, -1):
                try:
                    if 'Q' in initial_board[i][col] and '[31m' in initial_board[i][col]:
                        initial_board[i][col] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[i][col] and 'Q' not in initial_board[i][col]:
                        break
                except IndexError:
                    break
            for i in range(col + 1, 9):
                try:
                    if 'Q' in initial_board[8 - row][i] and '[31m' in initial_board[8 - row][i]:
                        initial_board[8 - row][i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row][i] and 'Q' not in initial_board[8 - row][i]:
                        break
                except IndexError:
                    break
            for i in range(col - 1, -1, -1):
                try:
                    if 'Q' in initial_board[8 - row][i] and '[31m' in initial_board[8 - row][i]:
                        initial_board[8 - row][i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row][i] and 'Q' not in initial_board[8 - row][i]:
                        break
                except IndexError:
                    break
            if '[93m' in initial_board[8 - row][col] and flag == 0:
                print('Невозможный ход ладьёй. Сделайте другой ход')
                continue
            for i in range(1, 8):
                if 8 - row + i < 8 and col + i < 8:
                    if '[31m' in initial_board[8 - row + i][col + i] and 'Q' in initial_board[8 - row + i][col + i]:
                        initial_board[8 - row + i][col + i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row + i][col + i]:
                        break
            for i in range(1, 8):
                if 8 - row - i >= 0 and col - i >= 0:
                    if '[31m' in initial_board[8 - row - i][col - i] and 'Q' in initial_board[8 - row - i][col - i]:
                        initial_board[8 - row - i][col - i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row - i][col - i]:
                        break
            for i in range(1, 8):
                if 8 - row + i < 8 and col - i >= 0:
                    if '[31m' in initial_board[8 - row + i][col - i] and 'Q' in initial_board[8 - row + i][col - i]:
                        initial_board[8 - row + i][col - i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row + i][col - i]:
                        break
            for i in range(1, 8):
                if 8 - row - i >= 0 and col + i < 8:
                    print(8 - row, col, 8 - row - i, col + i)
                    if '[31m' in initial_board[8 - row - i][col + i] and 'Q' in initial_board[8 - row - i][col + i]:
                        initial_board[8 - row - i][col + i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row - i][col + i]:
                        break
            if q_changes_flag == 0:
                print('Невозможный ход Ферзем. Сделайте другой ход')
                continue
            initial_board[8 - row][col] = Fore.RED + 'Q' + Fore.RESET
        else:
            if '[31m' in initial_board[8 - row][col] and flag == 0:
                print('Невозможный ход Ферзем. Сделайте другой ход')
                continue
            for i in range(8 - row + 1, 9):
                print(row, i, 8 - row)
                try:
                    if 'Q' in initial_board[i][col] and '[93m' in initial_board[i][col]:
                        initial_board[i][col] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[i][col] and 'Q' not in initial_board[i][col]:
                        break
                except IndexError:
                    break
            for i in range(8 - row - 1, -1, -1):
                try:
                    if 'Q' in initial_board[i][col] and '[93m' in initial_board[i][col]:
                        initial_board[i][col] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[i][col] and 'Q' not in initial_board[i][col]:
                        break
                except IndexError:
                    break
            for i in range(col + 1, 9):
                try:
                    if 'Q' in initial_board[8 - row][i] and '[93m' in initial_board[8 - row][i]:
                        initial_board[8 - row][i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row][i] and 'Q' not in initial_board[8 - row][i]:
                        break
                except IndexError:
                    break
            for i in range(col - 1, -1, -1):
                try:
                    if 'Q' in initial_board[8 - row][i] and '[93m' in initial_board[8 - row][i]:
                        initial_board[8 - row][i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row][i] and 'Q' not in initial_board[8 - row][i]:
                        break
                except IndexError:
                    break
            for i in range(1, 8):
                if 8 - row + i < 8 and col + i < 8:
                    if '[93m' in initial_board[8 - row + i][col + i] and 'Q' in initial_board[8 - row + i][col + i]:
                        initial_board[8 - row + i][col + i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row + i][col + i]:
                        break
            for i in range(1, 8):
                if 8 - row - i >= 0 and col - i >= 0:
                    print(8 - row, col, 8 - row - i, col - i)
                    if '[93m' in initial_board[8 - row - i][col - i] and 'Q' in initial_board[8 - row - i][col - i]:
                        initial_board[8 - row - i][col - i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row - i][col - i]:
                        break
            for i in range(1, 8):
                if 8 - row + i < 8 and col - i >= 0:
                    print(8 - row, col, 8 - row + i, col - i)
                    if '[93m' in initial_board[8 - row + i][col - i] and 'Q' in initial_board[8 - row + i][col - i]:
                        initial_board[8 - row + i][col - i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row + i][col - i]:
                        break
            for i in range(1, 8):
                if 8 - row - i >= 0 and col + i < 8:
                    print(8 - row, col, 8 - row - i, col + i)
                    if '[93m' in initial_board[8 - row - i][col + i] and 'Q' in initial_board[8 - row - i][col + i]:
                        initial_board[8 - row - i][col + i] = Fore.WHITE + '.'
                        q_changes_flag = 1
                    elif '.' not in initial_board[8 - row - i][col + i]:
                        break
            if q_changes_flag == 0:
                print('Невозможный ход Ферзем. Сделайте другой ход')
                continue
            initial_board[8 - row][col] = Fore.LIGHTYELLOW_EX + 'Q' + Fore.RESET
    elif move[0] == 'K':
        k_changes_flag = 0
        move = move.replace(move[0], '')
        move = move.replace(move[0], dct_coords[move[0]])
        row = int(move[1])
        col = int(move[0])
        if move_counter % 2 == 0:
            if '[93m' in initial_board[8 - row][col] and flag == 0:
                print('Невозможный ход Ферзем. Сделайте другой ход')
                continue
            if 8 - row < 8:
                if 'K' in initial_board[8 - row + 1][col] and '[31m' in initial_board[row + 1][col]:
                    initial_board[8 - row + 1][col] = Fore.WHITE + '.'
                    k_changes_flag = 1
            if 8 - row < 8 and col >= 1:
                if 'K' in initial_board[8 - row + 1][col - 1] and '[31m' in initial_board[row + 1][col]:
                    initial_board[8 - row + 1][col - 1] = Fore.WHITE + '.'
                    k_changes_flag = 1
            if col >= 1:
                if 'K' in initial_board[8 - row][col - 1] and '[31m' in initial_board[row + 1][col]:
                    initial_board[8 - row][col - 1] = Fore.WHITE + '.'
                    k_changes_flag = 1
            if 8 - row >= 1 and col >= 1:
                if 'K' in initial_board[8 - row - 1][col - 1] and '[31m' in initial_board[row + 1][col]:
                    initial_board[8 - row - 1][col - 1] = Fore.WHITE + '.'
                    k_changes_flag = 1
            if 8 - row < 8:
                if 'K' in initial_board[8 - row + 1][col] and '[31m' in initial_board[row + 1][col]:
                    initial_board[8 - row + 1][col] = Fore.WHITE + '.'
                    k_changes_flag = 1
            if 8 - row < 8 and col < 8:
                if 'K' in initial_board[8 - row + 1][col + 1] and '[31m' in initial_board[row + 1][col]:
                    initial_board[8 - row + 1][col + 1] = Fore.WHITE + '.'
                    k_changes_flag = 1
            if col < 8:
                if 'K' in initial_board[8 - row][col + 1] and '[31m' in initial_board[row + 1][col]:
                    initial_board[8 - row][col + 1] = Fore.WHITE + '.'
                    k_changes_flag = 1
            if 8 - row < 8 and col < 8:
                if 'K' in initial_board[8 - row + 1][col + 1] and '[31m' in initial_board[row + 1][col]:
                    initial_board[8 - row + 1][col + 1] = Fore.WHITE + '.'
                    k_changes_flag = 1
            if k_changes_flag == 0:
                print('Невозможный ход Ферзем. Сделайте другой ход')
                continue
            initial_board[8 - row][col] = Fore.RED + 'K' + Fore.RESET
    else:
        move = move.replace(move[0], dct_coords[move[0]])
        row = int(move[1])
        col = int(move[0])
        if 'p' in initial_board[8 - row][col] and flag == 0:
            print('Невозможный ход пешкой. Сделайте другой ход')
            continue
        if move_counter % 2 == 0:
            if 'p' in initial_board[8 - row + 2][col] and move[1] == '4':
                initial_board[8 - row + 2][col] = Fore.WHITE + '.'
            elif 'p' in initial_board[8 - row + 1][col] and '[31m' in initial_board[8 -
                                                            row + 1][col] and '[93m' not in initial_board[8 - row][col]:
                initial_board[8 - row + 1][col] = Fore.WHITE + '.'
            elif flag == 1 and '[93m' not in initial_board[8 - row + 1][col]:
                initial_board[8 - row + 1][int(pawn_col)] = Fore.WHITE + '.'
            else:
                print('Неккоректный ввод. Сделайте другой ход')
                continue
            initial_board[8 - row][col] = Fore.RED + 'p' + Fore.RESET
        else:
            if 'p' in initial_board[8 - row - 2][col] and move[1] == '5':
                initial_board[8 - row - 2][col] = Fore.WHITE + '.'
            elif 'p' in initial_board[8 - row - 1][col] and '[93m' in initial_board[8 - \
            row - 1][int(move[0])] and '[31m' not in initial_board[8 - row][col]:
                initial_board[8 - row - 1][col] = Fore.WHITE + '.'
            elif flag == 1 and '[31m' not in initial_board[8 - row + 1][col]:
                initial_board[8 - row - 1][int(pawn_col)] = Fore.WHITE + '.'
            else:
                print('Неккоректный ввод. Сделайте другой ход')
                continue
            initial_board[8 - row][col] = Fore.LIGHTYELLOW_EX + 'p' + Fore.RESET
    move_counter += 1
