import pygame as pg

FPS = 60
WIDTH, HEIGHT = 1000, 500
WIDTHP = 1045
HEIGHTH, HEIGHTL = 100, 300
SPEEDO, SPEEDT = 10, 15
RADO, RADT = 45, 35
WHITE = (255, 255, 255)
SILVER = (164, 164, 164)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BRASS = (204, 147, 117)
tick = 0
x1 = 0
x2 = 0
y1 = 100
y2 = 100

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.Surface((WIDTH, HEIGHT))
background.fill(SILVER)
pg.draw.rect(background, BRASS, (0, 0, WIDTH, HEIGHT))
pg.draw.rect(background, SILVER, (0, 100, WIDTH, 100))
pg.draw.rect(background, SILVER, (0, 300, WIDTH, 100))

pipeOne = pg.Surface((100, 100), pg.SRCALPHA)
pipeOne.fill((0, 0, 0, 0))
pg.draw.circle(pipeOne, (*RED, 120), (50, 50), 45)

pipeTwo = pg.Surface((100, 100), pg.SRCALPHA)
pipeTwo.fill((0, 0, 0, 0))
pg.draw.circle(pipeTwo, (*GREEN, 120), (50, 50), 35)

screen.blit(background, (0, 0))
screen.blit(pipeOne, (x1, y1))
screen.blit(pipeTwo, (x2, y2))
pg.display.update()

flag_play, flag_draw = True, False
while flag_play:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    if x1 <= WIDTHP and y1 == HEIGHTH:
        x1 += SPEEDO
    if x1 >= WIDTHP and y1 == HEIGHTH:
        y1 = HEIGHTL
    if x1 >= -100 and y1 == HEIGHTL:
        x1 -= SPEEDO
    if x1 <= -100 and y1 == HEIGHTL:
        y1 = HEIGHTH

    if x2 <= WIDTHP and y2 == HEIGHTH:
        x2 += SPEEDT
    if x2 >= WIDTHP and y2 == HEIGHTH:
        y2 = HEIGHTL
    if x2 >= -100 and y2 == HEIGHTL:
        x2 -= SPEEDT
    if x2 <= -100 and y2 == HEIGHTL:
        y2 = HEIGHTH

    screen.blit(background, (0, 0))
    screen.blit(pipeOne, (x1, y1))
    screen.blit(pipeTwo, (x2, y2))
    pg.display.update()
