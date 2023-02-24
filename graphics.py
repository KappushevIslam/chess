import pygame as pg

pg.init()

RES = WEDTH, HEIGHT = 800, 800

sc = pg.display.set_mode(RES)
pg.display.set_caption('Chess')
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLEDZOLOT = (238, 232, 170)
OHRA = (160, 82, 45)

FPS = 60

size = 100
y = 0

clock = pg.time.Clock()

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            quit()

    count = 0

    for x in range(8):
        for y in range(8):
            if (x + y) % 2 == 0:
                pg.draw.rect(sc, BLEDZOLOT, [size * x, size * y, size, size])
            else:
                pg.draw.rect(sc, OHRA, [size * x, size * y, size, size])

    pg.display.update()
    clock.tick(FPS)
