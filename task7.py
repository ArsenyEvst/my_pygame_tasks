import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 1000, 500
WIDTHP = 1045
HEIGHTH, HEIGHTL = 100, 300
SPEEDO, SPEEDT = 10, 15
WHITE = (255, 255, 255)
SILVER = (164, 164, 164)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BRASS = (204, 147, 117)
tick = 0


class Ball:
    def __init__(self):
        red = random.randint(1, 255)
        green = random.randint(1, 255)
        blue = random.randint(1, 255)
        alpha = random.randint(150, 255)
        self.speed = random.randint(5, 30)
        self.rad = random.randint(15, 49)
        self.surf = pg.Surface((100, 100), pg.SRCALPHA)
        self.rect = self.surf.get_rect(topleft=(0, 100))
        color = (red, green, blue)
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*color, alpha), (50, 50), self.rad)

    def move(self):
        if self.rect.right <= WIDTHP and self.rect.top == HEIGHTH:
            self.rect.right += self.speed
        if self.rect.right >= WIDTHP and self.rect.top == HEIGHTH:
            self.rect.top = HEIGHTL
        if self.rect.right >= -100 and self.rect.top == HEIGHTL:
            self.rect.right -= self.speed
        if self.rect.right <= -100 and self.rect.top == HEIGHTL:
            self.rect.top = HEIGHTH

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


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

balls = [Ball(), Ball()]
for elem in balls:
    elem.draw(screen)
screen.blit(background, (0, 0))

pg.display.update()

flag_play, flag_draw = True, False
while flag_play:
    clock.tick(FPS)
    tick += 1

    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            flag_play = False
            break
    if not flag_play:
        break

    pressed = pg.mouse.get_pressed()
    if pressed[0] and tick >= 40:
        balls.append(Ball())
        tick = 0

    for elem in balls:
        elem.move()

    screen.blit(background, (0, 0))
    for elem in balls:
        elem.draw(screen)
    pg.display.update()
