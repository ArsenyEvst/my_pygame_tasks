import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 600, 600
MINT = (230, 254, 212)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Игра")
clock = pg.time.Clock()

a = 3
x, y = WIDTH / 2, HEIGHT / 2
r = 30
colorR = 255
colorG = 150
colorB = 100
color = (colorR, colorG, colorB)
pg.draw.circle(screen, color, (x, y), r)
pg.display.update()

cnt_time = 0
flag_play = True
while flag_play:
    clock.tick(FPS)
    cnt_time += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x >= 0+r:
        x -= a
    if keys[pg.K_RIGHT] and x <= WIDTH-r:
        x += a
    if keys[pg.K_UP] and y >= 0+r:
        y -= a
    if keys[pg.K_DOWN] and y <= HEIGHT-r:
        y += a

    if keys[pg.K_SPACE] and cnt_time >= 30:
        colorR = random.randint(0, 255)
        colorG = random.randint(0, 255)
        colorB = random.randint(0, 255)
        color = (colorR, colorG, colorB)
        cnt_time = 0


    screen.fill(MINT)
    pg.draw.circle(screen, color, (x, y), r)

    pg.display.update()
