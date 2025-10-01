import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 600

BLACK = (0, 0, 0)
CYAN = (39, 214, 199)
BROWN = (125, 62, 0)
BROWNN = (145, 114, 15)
BLUE = (57, 105, 219)
GREEN = (122, 196, 88)
pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

screen.fill(CYAN)
pg.draw.rect(screen, GREEN, (275, 350, 450, 250))
pg.draw.rect(screen, BROWN, (475, 500, 50, 147))
pg.draw.polygon(screen, BROWNN, [[275, 350], [500, 250], [725, 350]])
# pg.draw.circle(screen, BLUE, ())

pg.display.update()

flag_play = True
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    pg.display.update()
