import pygame as pg
import random
import time

FPS = 60
WIDTH, HEIGHT = 1400, 700
WIDTHP = 1045
HEIGHTH, HEIGHTL = 100, 300
SPEEDO, SPEEDT = 10, 15
WHITE = (255, 255, 255)
SILVER = (164, 164, 164)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BRASS = (204, 147, 117)
tick = 0
a = 3
x, y = WIDTH / 2, HEIGHT / 2
r = 30
colorR = 255
colorG = 150
colorB = 100
color = (colorR, colorG, colorB)
# class Ball:
#     def __init__(self):
#         red = random.randint(1, 255)
#         green = random.randint(1, 255)
#         blue = random.randint(1, 255)
#         self.rad = random.randint(15, 49)
#         self.surf = pg.Surface((100, 100))
#         self.rect = self.surf.get_rect(topleft=(0, 100))
#         color = (red, green, blue)
#         self.surf.fill((0, 0, 0, 0))
#         pg.draw.circle(self.surf, (color), (50, 50), self.rad)
#
#     def move(self):
#         if self.rect.right <= WIDTHP and self.rect.top == HEIGHTH:
#             self.rect.right += self.speed
#         if self.rect.right >= WIDTHP and self.rect.top == HEIGHTH:
#             self.rect.top = HEIGHTL
#         if self.rect.right >= -100 and self.rect.top == HEIGHTL:
#             self.rect.right -= self.speed
#         if self.rect.right <= -100 and self.rect.top == HEIGHTL:
#             self.rect.top = HEIGHTH
#
#     def draw(self, screen):
#         screen.blit(self.surf, self.rect)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.Surface((WIDTH, HEIGHT))
background.fill(SILVER)


# balls = [Ball(), Ball()]
# for elem in balls:
#     elem.draw(screen)
screen.blit(background, (0, 0))
pg.draw.circle(screen, color, (x, y), r)
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

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and x >= 0 + r:
        x -= a
    if keys[pg.K_RIGHT] and x <= WIDTH - r:
        x += a
    if keys[pg.K_UP] and y >= 0 + r:
        y -= a
    if keys[pg.K_DOWN] and y <= HEIGHT - r:
        y += a



    pg.draw.circle(screen, color, (x, y), r)



    # pressed = pg.mouse.get_pressed()
    # if pressed[0] and tick >= 40:
    #     balls.append(Ball())
    #     tick = 0
    #
    # for elem in balls:
    #     elem.move()
    #
    # screen.blit(background, (0, 0))
    # for elem in balls:
    #     elem.draw(screen)
    pg.display.update()
