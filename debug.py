import pygame as pg
from PIL import Image


class Square:
    size = 100

    def __init__(self, color, figure=None):
        self.color = color
        self.figure = figure

    def draw_square(self, sc, x, y):
        surf = pg.Surface((self.size, self.size))
        pg.draw.rect(surf, self.color, [0, 0, self.size, self.size])
        if self.figure is not None:
            figure_pic = pg.image.load('pics/' + self.figure + '.png')
            figure_pic = pg.transform.scale(figure_pic, (100, 100))
            surf.blit(figure_pic, (0, 0))
        sc.blit(surf, (self.size * y, self.size * x))


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
    FPS = 15
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
        pos = ''
        row = ''
        column = ''
        pg.mixer.music.load('pics/nigga_song.mp3')
        pg.mixer.music.play()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
                elif event.type == pg.MOUSEBUTTONDOWN:
                    pos = pg.mouse.get_pos()
                    column = pos[0] // 100
                    row = pos[1] // 100
                    print("Click ", pos, "Grid coordinates: ", row, column)
            for x in range(8):
                for y in range(8):
                    self.board_matrix[x][y].draw_square(self.sc, x, y)
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
