import pygame as pg

FPS = 60
WIDTH, HEIGHT = 750, 250

CYAN = (39, 214, 199)
BROWN = (125, 62, 0)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()
x = 0
a = 2
screen.fill(CYAN)
pg.draw.rect(screen, BROWN, (0, HEIGHT // 2 - 25, 50, 50))

pg.display.update()

leri = True
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

    if leri == True:
        x += a
    elif leri == False:
        x -= a

    if x >= WIDTH - 25:
        leri = False
        a += 3
    elif x <= 0:
        leri = True
        a += 3

    screen.fill(CYAN)
    pg.draw.rect(screen, BROWN, (x, HEIGHT // 2 - 25, 50, 50))
    pg.display.update()
