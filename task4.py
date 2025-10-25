import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 600, 500
WHITE = (255, 255, 255)
RED = (255, 0, 0)
tick = 0

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

x = random.randint(50, 550)
y = random.randint(50, 450)
r = 30
pg.draw.circle(screen, RED, (x, y), r)
pg.display.update()

flag_play, flag_draw = True, False
while flag_play:
    clock.tick(FPS)
    tick += 1

    pressed = pg.mouse.get_pressed()
    current_pos = pg.mouse.get_pos()
    dist = ((x - current_pos[0]) ** 2 + (y - current_pos[1]) ** 2) ** 0.5

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 4 and r >= dist:
            r += 5
            if r >= 150:
                x = random.randint(50, 550)
                y = random.randint(50, 450)
                screen.fill(WHITE)
                r = 30
                pg.draw.circle(screen, RED, (x, y), r)
                pg.display.update()
                r = 30
            screen.fill(WHITE)
            pg.draw.circle(screen, RED, (x, y), r)
            pg.display.update()
            if tick >= 30:
                print(4)
                tick = 0
            pg.display.update()
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 5 and r >= dist:
            if r >= 10:
                r -= 1
            screen.fill(WHITE)
            pg.draw.circle(screen, RED, (x, y), r)
            pg.display.update()
            if tick >= 30:
                print(5)
                tick = 0
            pg.display.update()
    if not flag_play:
        break



    if pressed[0] and r >= dist:
        r += 1
        if r == 150:
            x = random.randint(50, 550)
            y = random.randint(50, 450)
            screen.fill(WHITE)
            r = 30
            pg.draw.circle(screen, RED, (x, y), r)
            pg.display.update()
            r = 30
        screen.fill(WHITE)
        pg.draw.circle(screen, RED, (x, y), r)
        pg.display.update()
        if tick >= 30:
            print(2)
            tick = 0
        pg.display.update()

    if pressed[2] and r >= dist:
        if r >= 10:
            r -= 1
        screen.fill(WHITE)
        pg.draw.circle(screen, RED, (x, y), r)
        pg.display.update()
        if tick >= 30:
            print(3)
            tick = 0
        pg.display.update()

    if pressed[1] and r >= dist:
        x = random.randint(50, 550)
        y = random.randint(50, 450)
        screen.fill(WHITE)
        r = 30
        pg.draw.circle(screen, RED, (x, y), r)
        pg.display.update()
        if tick >= 30:
            print(1)
            tick = 0
