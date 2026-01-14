import pygame as pg
import random
import time

FPS = 60
WIDTH, HEIGHT = 1600, 800
WIDTHP = 1045
HEIGHTH, HEIGHTL = 100, 300
SPEEDO, SPEEDT = 10, 15
WHITE = (255, 255, 255)
SILVER = (164, 164, 164)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BRASS = (250, 147, 117)
tick = 0


class Food:
    def __init__(self):
        self.radF = random.randint(15, 75)
        self.xF = random.randint(100, 1500)
        self.yF = random.randint(100, 700)
        self.surf = pg.Surface((150, 150), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(self.xF, self.yF))
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*RED, 255), (self.rect.width / 2, self.rect.height / 2), self.radF)
        self.mask = pg.mask.from_surface(self.surf)
        self.active = True

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


class Player:
    def __init__(self):
        self.r = 30
        self.sp = 3
        self.x, self.y = WIDTH // 2, HEIGHT // 2
        self.surf = pg.Surface((400, 400), pg.SRCALPHA)
        self.rect = self.surf.get_rect(center=(self.x, self.y))
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*BRASS, 255), (self.rect.width / 2, self.rect.height / 2), self.r)
        self.mask = pg.mask.from_surface(self.surf)

    def eat(self, radF):
        global tick
        if radF <= 30 and (self.r + 5) <= 200 and tick >= 15:
            self.r += 5
            tick = 0
        if radF <= 50 and (self.r + 10) <= 200 and tick >= 30:
            self.r += 10
            tick = 0
        if radF <= 100 and (self.r + 15) <= 200 and tick >= 30:
            self.r += 15
            tick = 0
        if radF <= 130 and (self.r + 25) <= 200 and tick >= 30:
            self.r += 25
            tick = 0
        if radF <= 130 and (self.r + 40) <= 200 and tick >= 30:
            self.r += 40
            tick = 0
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*BRASS, 255), (self.rect.width / 2, self.rect.height / 2), self.r)
        self.mask = pg.mask.from_surface(self.surf)

    def move(self, dx=0, dy=0):
        if (self.rect.centerx - self.r + dx * self.sp) > 0 and (self.rect.centerx + self.r + dx * self.sp) < WIDTH:
            self.rect.x += dx * self.sp
        if (self.rect.centery - self.r + dy * self.sp) > 0 and (self.rect.centery + self.r + dy * self.sp) < HEIGHT:
            self.rect.y += dy * self.sp

    def draw(self, screen):
        screen.blit(self.surf, self.rect)


def check_collisions(player, foods):
    for i in range(len(foods)):
        food = foods[i]
        if food.active == False:
            continue
        offset = (food.rect.x - player.rect.x, food.rect.y - player.rect.y)
        if player.mask.overlap(food.mask, offset) is not None:
            player.eat(food.radF)
            food.active = False
            foods.append(Food())
            break

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()

background = pg.Surface((WIDTH, HEIGHT))
background.fill(SILVER)

player = Player()
foods = [Food(), Food(), Food()]
screen.blit(background, (0, 0))
for elem in foods:
    elem.draw(screen)
player.draw(screen)
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
    if keys[pg.K_LEFT]:
        player.move(dx=-1)
    if keys[pg.K_RIGHT]:
        player.move(dx=1)
    if keys[pg.K_UP]:
        player.move(dy=-1)
    if keys[pg.K_DOWN]:
        player.move(dy=1)

    check_collisions(player, foods)

    screen.blit(background, (0, 0))
    for elem in foods:
        if elem.active:
            elem.draw(screen)
    foods = [elem for elem in foods if elem.active]
    player.draw(screen)
    pg.display.update()
