import pygame as pg


class Square:
    size = 100

    def __init__(self, color, figure=None):
        self.color = color
        self.figure = figure

    def draw_square(self, sc, x, y):
        pg.draw.rect(sc, self.color, [self.size * x, self.size * y, self.size, self.size])


class Board:
    pg.init()
    RES = WEDTH, HEIGHT = 800, 800
    BLEDZOLOT = (238, 232, 170)
    OHRA = (160, 82, 45)
    sc = pg.display.set_mode(RES)
    pg.display.set_caption('Chess')
    icon = pg.image.load('pics/big floppa.jpg')
    pg.display.set_icon(icon)
    floppa = pg.transform.scale(icon, (800, 800))
    floppa.set_alpha(100)
    FPS = 60
    board_matrix = [
        [Square(BLEDZOLOT, 'bRook'), Square(OHRA, 'bKnight'), Square(BLEDZOLOT, 'bBishop'), Square(OHRA, 'bQueen'), Square(BLEDZOLOT, 'bKing'), Square(OHRA, 'bBishop'), Square(BLEDZOLOT, 'bKnight'), Square(OHRA, 'bRook')],
        [Square(OHRA, 'bPawn'), Square(BLEDZOLOT, 'bPawn'), Square(OHRA, 'bPawn'), Square(BLEDZOLOT, 'bPawn'), Square(OHRA, 'bPawn'), Square(BLEDZOLOT, 'bPawn'), Square(OHRA, 'bPawn'), Square(BLEDZOLOT, 'bPawn')],
        [Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT), Square(OHRA)],
        [Square(OHRA), Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT)],
        [Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT), Square(OHRA)],
        [Square(OHRA), Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT), Square(OHRA), Square(BLEDZOLOT)],
        [Square(BLEDZOLOT, 'wPawn'), Square(OHRA, 'wPawn'), Square(BLEDZOLOT, 'wPawn'), Square(OHRA, 'wPawn'), Square(BLEDZOLOT, 'wPawn'), Square(OHRA, 'wPawn'), Square(BLEDZOLOT, 'wPawn'), Square(OHRA, 'wPawn')],
        [Square(OHRA, 'wRook'), Square(BLEDZOLOT, 'wKnight'), Square(OHRA, 'wBishop'), Square(BLEDZOLOT, 'wQueen'), Square(OHRA, 'wKing'), Square(BLEDZOLOT, 'wBishop'), Square(OHRA, 'wKnight'), Square(BLEDZOLOT, 'wRook')]
    ]

    def draw_board(self):
        clock = pg.time.Clock()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            for x in range(8):
                for y in range(8):
                    self.board_matrix[x][y].draw_square(self.sc, x, y)
            self.sc.blit(self.floppa, (0, 0))
            pg.display.update()
            clock.tick(self.FPS)


board = Board()
board.draw_board()
