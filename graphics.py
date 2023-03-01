import pygame as pg


class Board:
    pg.init()

    RES = WEDTH, HEIGHT = 800, 800

    sc = pg.display.set_mode(RES)
    pg.display.set_caption('Chess')
    icon = pg.image.load('pics/big floppa.jpg')
    pg.display.set_icon(icon)
    floppa = pg.transform.scale(icon, (800, 800))
    floppa.set_alpha(100)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    BLEDZOLOT = (238, 232, 170)
    OHRA = (160, 82, 45)
    FPS = 60
    size = 100

    def draw_board(self):
        clock = pg.time.Clock()
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()

            for x in range(8):
                for y in range(8):
                    if (x + y) % 2 == 0:
                        pg.draw.rect(self.sc, self.BLEDZOLOT, [self.size * x, self.size * y, self.size, self.size])
                    else:
                        pg.draw.rect(self.sc, self.OHRA, [self.size * x, self.size * y, self.size, self.size])
            self.sc.blit(self.floppa, (0, 0))
            pg.display.update()
            clock.tick(self.FPS)
