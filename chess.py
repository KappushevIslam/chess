import pygame as pg
from PIL import Image


class Square:
    size = 100
    is_clicked = False
    possible_move = False
    GREEN = (49, 196, 74)
    RED = (255, 17, 0)

    def __init__(self, row, col, back_color, figure='.', color='n'):
        self.figure = figure
        self.color = color
        self.color = str(color)
        self.row = row
        self.row = int(self.row)
        self.col = col
        self.col = int(self.col)
        self.back_color = back_color
        if figure == 'K':
            self.move_c = 0

    def __str__(self):
        return str(self.figure)

    def draw_square(self, sc, x, y):
        surf = pg.Surface((self.size, self.size))
        convert_dct = {'R': 'Rook', 'P': 'Pawn', 'Q': 'Queen', 'B': 'Bishop', 'N': 'Knight', 'K': 'King'}
        if self.is_clicked:
            pg.draw.rect(surf, self.GREEN, [0, 0, self.size, self.size])
        else:
            pg.draw.rect(surf, self.back_color, [0, 0, self.size, self.size])
        if self.figure != '.':
            figure_pic = pg.image.load('pics/' + self.color + convert_dct[self.figure] + '.png')
            figure_pic = pg.transform.scale(figure_pic, (100, 100))
            surf.blit(figure_pic, (0, 0))
        if self.possible_move:
            if self.figure != '.':
                pg.draw.circle(surf, self.RED, [50, 50], 15)
            else:
                pg.draw.circle(surf, self.GREEN, [50, 50], 15)
        sc.blit(surf, (self.size * y, self.size * x))

    def get_possible_moves(self, board):
        if board[self.row][self.col].color == 'w':
            is_white = True
            board = list(reversed([list(reversed(i)) for i in board]))
            self.row = 7 - self.row
            self.col = 7 - self.col
        else:
            is_white = False
        piece = str(board[self.row][self.col])
        moves = []
        if piece == '.':
            return moves
        if piece == 'P':
            if self.row != 7 and board[self.row + 1][self.col].figure == '.':
                moves += [(self.row + 1, self.col)]
            if self.row == 4 and self.col - 1 > -1:
                if board[self.row][self.col-1].figure == 'P' and board[self.row][self.col-1].color != board[self.row][self.col].color:
                    moves += [(self.row+1, self.col-1), 'en pess']
            if self.row == 4 and self.col + 1 < 8:
                if board[self.row][self.col+1].figure == 'P' and board[self.row][self.col+1].color != board[self.row][self.col].color:
                    moves += [(self.row+1, self.col+1), 'en pess']
            if self.row == 1 and board[self.row + 2][self.col].figure == '.':
                moves += [(self.row + 2, self.col)]
            if self.row + 1 < 8 and self.col + 1 < 8:
                if board[self.row + 1][self.col + 1].color == 'b' if is_white else board[self.row + 1][self.col + 1].color == 'w':
                    moves += [(self.row + 1, self.col + 1)]
            if self.row + 1 < 8 and self.col - 1 > -1:
                if board[self.row + 1][self.col - 1].color == 'b' if is_white else board[self.row + 1][self.col - 1].color == 'w':
                    moves += [(self.row + 1, self.col - 1)]
        if piece == 'N':
            if self.row < 6 and self.col < 7 and (board[self.row + 2][self.col + 1].figure == '.' or (
            board[self.row + 2][self.col + 1].color == 'b' if is_white else board[self.row + 2][self.col + 1].color == 'w')):
                moves += [(self.row + 2, self.col + 1)]
            if self.row < 7 and self.col < 6 and (board[self.row + 1][self.col + 2].figure == '.' or (
            board[self.row + 1][self.col + 2].color == 'b' if is_white else board[self.row + 1][
                                                                              self.col + 2].color == 'w')):
                moves += [(self.row + 1, self.col + 2)]
            if self.row < 6 and self.col > 0 and (board[self.row + 2][self.col - 1].figure == '.' or (
            board[self.row + 2][self.col - 1].color == 'b' if is_white else board[self.row + 2][
                                                                              self.col - 1].color == 'w')):
                moves += [(self.row + 2, self.col - 1)]
            if self.row < 7 and self.col > 1 and (board[self.row + 1][self.col - 2].figure == '.' or (
            board[self.row + 1][self.col - 2].color == 'b' if is_white else board[self.row + 1][
                                                                              self.col - 2].color == 'w')):
                moves += [(self.row + 1, self.col - 2)]
            if self.row > 1 and self.col < 7 and (board[self.row - 2][self.col + 1].figure == '.' or (
            board[self.row - 2][self.col + 1].color == 'b' if is_white else board[self.row - 2][
                                                                              self.col + 1].color == 'w')):
                moves += [(self.row - 2, self.col + 1)]
            if self.row > 0 and self.col < 6 and (board[self.row - 1][self.col + 2].figure == '.' or (
            board[self.row - 1][self.col + 2].color == 'b' if is_white else board[self.row - 1][
                                                                              self.col + 2].color == 'w')):
                moves += [(self.row - 1, self.col + 2)]
            if self.row > 1 and self.col > 0 and (board[self.row - 2][self.col - 1].figure == '.' or (
            board[self.row - 2][self.col - 1].color == 'b' if is_white else board[self.row - 2][
                                                                              self.col - 1].color == 'w')):
                moves += [(self.row - 2, self.col - 1)]
            if self.row > 0 and self.col > 1 and (board[self.row - 1][self.col - 2].figure == '.' or (
            board[self.row - 1][self.col - 2].color == 'b' if is_white else board[self.row - 1][
                                                                              self.col - 2].color == 'w')):
                moves += [(self.row - 1, self.col - 2)]
        if piece == 'B' or piece == 'Q':
            right_down_flag = 0
            right_up_flag = 0
            left_down_flag = 0
            left_up_flag = 0
            for i in range(1, 8):
                if self.row + i < 8 and self.col + i < 8 and right_down_flag == 0:
                    if board[self.row + i][self.col + i].figure == '.':
                        moves += [(self.row + i, self.col + i)]
                    elif board[self.row + i][self.col + i].color == 'b' if is_white else board[self.row + i][
                                                                                           self.col + i].color == 'w':
                        moves += [(self.row + i, self.col + i)]
                        right_down_flag = 1
                    else:
                        right_down_flag = 1
                if self.row + i < 7 and self.col - i > -1 and left_down_flag == 0:
                    if board[self.row + i][self.col - i].figure == '.':
                        moves += [(self.row + i, self.col - i)]
                    elif board[self.row + i][self.col - i].color == 'b' if is_white else board[self.row + i][
                                                                                           self.col - i].color == 'w':
                        moves += [(self.row + i, self.col - i)]
                        left_down_flag = 1
                    else:
                        left_down_flag = 1
                if self.row - i > -1 and self.col + i < 8 and right_up_flag == 0:
                    if board[self.row - i][self.col + i].figure == '.':
                        moves += [(self.row - i, self.col + i)]
                    elif board[self.row - i][self.col + i].color == 'b' if is_white else board[self.row - i][
                                                                                           self.col + i].color == 'w':
                        moves += [(self.row - i, self.col + i)]
                        right_up_flag = 1
                if self.row - i > -1 and self.col - i > -1 and left_up_flag == 0:
                    if board[self.row - i][self.col - i].figure == '.':
                        moves += [(self.row - 1, self.col - i)]
                    elif board[self.row - i][self.col - i].color == 'b' if is_white else board[self.row - i][
                                                                                           self.col - i].color == 'w':
                        moves += [(self.row - i, self.col - i)]
                        left_up_flag = 1
                    else:
                        left_up_flag = 1
        if piece == 'R' or piece == 'Q':
            up_flag = 0
            down_flag = 0
            left_flag = 0
            right_flag = 0
            for i in range(1, 8):
                if self.row + i < 8 and down_flag == 0:
                    if board[self.row + i][self.col].figure == '.':
                        moves += [(self.row + i, self.col)]
                    elif board[self.row + i][self.col].color == 'b' if is_white else board[self.row + i][
                                                                                       self.col].color == 'w':
                        moves += [(self.row + i, self.col)]
                        down_flag = 1
                    else:
                        down_flag = 1
                if self.row - i > -1 and up_flag == 0:
                    if board[self.row - i][self.col].figure == '.':
                        moves += [(self.row - i, self.col)]
                    elif board[self.row - i][self.col].color == 'b' if is_white else board[self.row - i][
                                                                                       self.col].color == 'w':
                        moves += [(self.row - i, self.col)]
                        up_flag = 1
                    else:
                        up_flag = 1
                if self.col + i < 8 and right_flag == 0:
                    if board[self.row][self.col + i].figure == '.':
                        moves += [(self.row, self.col + i)]
                    elif board[self.row][self.col + i].color == 'b' if is_white else board[self.row][
                                                                                       self.col + i].color == 'w':
                        moves += [(self.row, self.col + i)]
                        right_flag = 1
                    else:
                        right_flag = 1
                if self.col - i > -1 and left_flag == 0:
                    if board[self.row][self.col - i].figure == '.':
                        moves += [(self.row, self.col - i)]
                    elif board[self.row][self.col - i].color == 'b' if is_white else board[self.row][
                                                                                       self.col - i].color == 'w':
                        moves += [(self.row, self.col - i)]
                        left_flag = 1
                    else:
                        left_flag = 1
        if piece == 'K':
            moves_c = 0  # если король походил хоть раз, то рокировка невозможна
            if self.row + 1 < 8 and self.col + 1 < 8 and (board[self.row + 1][self.col + 1].figure == '.' or
                                                          (board[self.row + 1][self.col + 1].color == 'b' if is_white else
                                                          board[self.row + 1][self.col + 1].color == 'w')):
                moves += [(self.row + 1, self.col + 1)]
            if self.row + 1 < 8 and (board[self.row + 1][self.col].figure == '.' or
                                     (board[self.row + 1][self.col].color == 'b' if is_white else board[self.row + 1][
                                                                                                    self.col].color == 'w')):
                moves += [(self.row + 1, self.col)]
            if self.row + 1 < 8 and self.col - 1 > -1 and (board[self.row + 1][self.col - 1].figure == '.' or
                                                           (
                                                           board[self.row + 1][self.col - 1].color == 'b' if is_white else
                                                           board[self.row + 1][self.col - 1].color == 'w')):
                moves += [(self.row + 1, self.col - 1)]
            if self.col - 1 > -1 and (board[self.row][self.col - 1].figure == '.' or
                                      (board[self.row][self.col - 1].color == 'b' if is_white else board[self.row][
                                                                                                     self.col - 1].color == 'w')):
                moves += [(self.row, self.col - 1)]
            if self.row - 1 > -1 and self.col - 1 > -1 and (board[self.row - 1][self.col - 1].figure == '.' or
                                                            (board[self.row - 1][
                                                                 self.col - 1].color == 'b' if is_white else
                                                            board[self.row - 1][self.col - 1].color == 'w')):
                moves += [(self.row - 1, self.col - 1)]
            if self.row - 1 > -1 and (board[self.row - 1][self.col].figure == '.' or
                                      (board[self.row - 1][self.col].color == 'b' if is_white else board[self.row - 1][
                                                                                                     self.col].color == 'w')):
                moves += [(self.row - 1, self.col)]
            if self.row - 1 > -1 and self.col + 1 < 8 and (board[self.row - 1][self.col + 1].figure == '.' or
                                                           (
                                                           board[self.row - 1][self.col + 1].color == 'b' if is_white else
                                                           board[self.row - 1][self.col + 1].color == 'w')):
                moves += [(self.row - 1, self.col + 1)]
            if self.col + 1 < 8 and (board[self.row][self.col + 1].figure == '.' or
                                     (board[self.row][self.col + 1].color == 'b' if is_white else board[self.row][
                                                                                                    self.col + 1].color == 'w')):
                moves += [(self.row, self.col + 1)]
            if self.move_c == 0 and board[self.row][self.col+1].figure == '.' and board[self.row][self.col+2].figure \
                == '.' and self.move_c == 0 and board[self.row][self.col+3].figure == 'R':
                moves += [(self.row, self.col + 2), '0-0']

        if is_white:
            moves = list(map(lambda x: (7 - x[0], 7 - x[1]) if type(x) == tuple else x, moves))
            self.row = 7 - self.row
            self.col = 7 - self.col
        return moves

    def make_move(self, x_to, y_to, board):
        moves_lst = board[self.row][self.col].get_possible_moves(board)
        print(moves_lst, (x_to, y_to))
        if (x_to, y_to) in moves_lst:
            board[x_to][y_to] = Square(x_to, y_to, board[x_to][y_to].back_color, board[self.row][self.col].figure, board[self.row][self.col].color)
            board[self.row][self.col] = Square(self.row, self.col, board[self.row][self.col].back_color)
        if 'en pess' in moves_lst:
            if board[x_to][y_to].color == 'w':
                board[x_to+1][y_to] = Square(self.row, self.col, board[x_to+1][y_to].back_color)
            else:
                board[x_to-1][y_to] = Square(self.row, self.col, board[x_to-1][y_to].back_color)
        if '0-0' in moves_lst:
            board[x_to][y_to+1] = Square(x_to, y_to+1, board[x_to][y_to+1].back_color)
            board[x_to][y_to-1] = Square(x_to, y_to-1, board[x_to][y_to-1].back_color, 'R', board[x_to][y_to].color)
        if (x_to == 7 or x_to == 0) and board[x_to][y_to].figure == 'P':
            board[x_to][y_to] = Square(x_to, y_to, board[x_to][y_to].back_color, 'Q', board[x_to][y_to].color)
        if board[x_to][y_to].figure == 'k':
            board[x_to][y_to].move_c += 1


class Board:
    pg.init()
    RES = WEDTH, HEIGHT = 800, 800
    BLEDZOLOT = (238, 232, 170)
    OHRA = (160, 82, 45)
    FORMAT = "RGBA"
    sc = pg.display.set_mode(RES)
    pg.display.set_caption('Chess')
    icon = pg.image.load('pics/big floppa.jpg')
    pg.display.set_icon(icon)
    last_piece_coords = []
    FPS = 15
    board = [
        [Square(0, 0, BLEDZOLOT, 'R', 'b'), Square(0, 1, OHRA, 'N', 'b'), Square(0, 2, BLEDZOLOT, 'B', 'b'), Square(0, 3, OHRA, 'Q', 'b'), Square(0, 4, BLEDZOLOT, 'K', 'b'), Square(0, 5, OHRA, 'B', 'b'), Square(0, 6, BLEDZOLOT, 'N', 'b'), Square(0, 7, OHRA, 'R', 'b')],
        [Square(1, 0, OHRA, 'P', 'b'), Square(1, 1, BLEDZOLOT, 'P', 'b'), Square(1, 2, OHRA, 'P', 'b'), Square(1, 3, BLEDZOLOT, 'P', 'b'), Square(1, 4, OHRA, 'P', 'b'), Square(1, 5, BLEDZOLOT, 'P', 'b'), Square(1, 6, OHRA, 'P', 'b'), Square(2, 6, BLEDZOLOT, 'P', 'b')],
        [Square(2, 0, BLEDZOLOT), Square(2, 1, OHRA), Square(2, 2, BLEDZOLOT), Square(2, 3, OHRA),
         Square(2, 4, BLEDZOLOT), Square(2, 5, OHRA), Square(2, 6, BLEDZOLOT), Square(2, 7, OHRA)],
        [Square(3, 0, OHRA), Square(3, 1, BLEDZOLOT), Square(3, 2, OHRA), Square(3, 3, BLEDZOLOT), Square(3, 4, OHRA),
         Square(3, 5, BLEDZOLOT), Square(3, 6, OHRA), Square(3, 7, BLEDZOLOT)],
        [Square(4, 0, BLEDZOLOT), Square(4, 1, OHRA), Square(4, 2, BLEDZOLOT), Square(4, 3, OHRA),
         Square(4, 4, BLEDZOLOT), Square(4, 5, OHRA), Square(4, 6, BLEDZOLOT), Square(4, 7, OHRA)],
        [Square(5, 0, OHRA), Square(5, 1, BLEDZOLOT), Square(5, 2, OHRA), Square(5, 3, BLEDZOLOT), Square(5, 4, OHRA),
         Square(5, 5, BLEDZOLOT), Square(5, 6, OHRA), Square(5, 7, BLEDZOLOT)],
        [Square(6, 0, BLEDZOLOT, 'P', 'w'), Square(6, 1, OHRA, 'P', 'w'), Square(6, 2, BLEDZOLOT, 'P', 'w'),
         Square(6, 3, OHRA, 'P', 'w'), Square(6, 4, BLEDZOLOT, 'P', 'w'), Square(6, 5, OHRA, 'P', 'w'),
         Square(6, 6, BLEDZOLOT, 'P', 'w'), Square(6, 7, OHRA, 'P', 'w')],
        [Square(7, 0, OHRA, 'R', 'w'), Square(7, 1, BLEDZOLOT, 'N', 'w'), Square(7, 2, OHRA, 'B', 'w'),
         Square(7, 3, BLEDZOLOT, 'Q', 'w'), Square(7, 4, OHRA, 'K', 'w'), Square(7, 5, BLEDZOLOT, 'B', 'w'),
         Square(7, 6, OHRA, 'N', 'w'), Square(7, 7, BLEDZOLOT, 'R', 'w')]
    ]

    def pil_to_game(self, img):
        data = img.tobytes("raw", self.FORMAT)
        return pg.image.fromstring(data, img.size, self.FORMAT)

    def get_gif_frame(self, img, frame):
        img.seek(frame)
        return img.convert(self.FORMAT)

    def draw_board(self):
        gif_img = Image.open('pics/floppa.gif')
        current_frame = 0
        clock = pg.time.Clock()
        move_counter = 0
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    column = pos[0] // 100
                    row = pos[1] // 100
                    available_moves = self.board[row][column].get_possible_moves(self.board)
                    if self.board[row][column].possible_move:
                        self.board[self.last_piece_coords[0]][self.last_piece_coords[1]].make_move(row, column, self.board)
                        move_counter += 1
                        self.last_piece_coords = []
                        self.board[row][column].is_clicked = False
                        for r in range(8):
                            for c in range(8):
                                self.board[r][c].possible_move = False
                        continue
                    print(self.board[row][column].get_possible_moves(self.board))
                    for r in range(8):
                        for c in range(8):
                            self.board[r][c].is_clicked = False
                            if (r, c) in available_moves:
                                self.board[r][c].possible_move = True
                            else:
                                self.board[r][c].possible_move = False
                    if self.board[row][column].figure != '.':
                        if move_counter % 2 == 0 and self.board[row][column].color != 'w':
                            available_moves = []
                            for r in range(8):
                                for c in range(8):
                                    self.board[r][c].possible_move = False
                            continue
                        elif move_counter % 2 == 1 and self.board[row][column].color != 'b':
                            available_moves = []
                            for r in range(8):
                                for c in range(8):
                                    self.board[r][c].possible_move = False
                            continue
                        self.board[row][column].is_clicked = True
                        self.last_piece_coords = [row, column]
                    else:
                        self.last_piece_coords = []
                    print("Click ", pos, "Grid coordinates: ", row, column)
            for x in range(8):
                for y in range(8):
                    self.board[x][y].draw_square(self.sc, x, y)
            frame = self.pil_to_game(self.get_gif_frame(gif_img, current_frame))
            frame = pg.transform.scale(frame, (800, 800))
            frame.set_alpha(120)
            self.sc.blit(frame, (0, 0))
            current_frame = (current_frame + 1) % gif_img.n_frames
            pg.display.flip()
            pg.display.update()
            clock.tick(self.FPS)


board = Board()
board.draw_board()
