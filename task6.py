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

pipeOne_sf = pg.Surface((100, 100), pg.SRCALPHA)
pipeOne_rect = pipeOne_sf.get_rect(topleft=(0, 100))
pipeOne_sf.fill((0, 0, 0, 0))
pg.draw.circle(pipeOne_sf, (*RED, 120), (50, 50), 45)

pipeTwo_sf = pg.Surface((100, 100), pg.SRCALPHA)
pipeTwo_rect = pipeTwo_sf.get_rect(topleft=(0, 100))
pipeTwo_sf.fill((0, 0, 0, 0))
pg.draw.circle(pipeTwo_sf, (*GREEN, 120), (50, 50), 35)

screen.blit(background, (0, 0))
screen.blit(pipeOne_sf, pipeOne_rect)
screen.blit(pipeTwo_sf, pipeTwo_rect)
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

    if pipeOne_rect.right <= WIDTHP and pipeOne_rect.top == HEIGHTH:
        pipeOne_rect.right += SPEEDO
    if pipeOne_rect.right >= WIDTHP and pipeOne_rect.top == HEIGHTH:
        pipeOne_rect.top = HEIGHTL
    if pipeOne_rect.right >= -100 and pipeOne_rect.top == HEIGHTL:
        pipeOne_rect.right -= SPEEDO
    if pipeOne_rect.right <= -100 and pipeOne_rect.top == HEIGHTL:
        pipeOne_rect.top = HEIGHTH

    if pipeTwo_rect.right <= WIDTHP and pipeTwo_rect.top == HEIGHTH:
        pipeTwo_rect.right += SPEEDT
    if pipeTwo_rect.right >= WIDTHP and pipeTwo_rect.top == HEIGHTH:
        pipeTwo_rect.top = HEIGHTL
    if pipeTwo_rect.right >= -100 and pipeTwo_rect.top == HEIGHTL:
        pipeTwo_rect.right -= SPEEDT
    if pipeTwo_rect.right <= -100 and pipeTwo_rect.top == HEIGHTL:
        pipeTwo_rect.top = HEIGHTH

    screen.blit(background, (0, 0))
    screen.blit(pipeOne_sf, pipeOne_rect)
    screen.blit(pipeTwo_sf, pipeTwo_rect)
    pg.display.update()
