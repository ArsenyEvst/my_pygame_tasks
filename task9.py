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
YELLOW, DARK_YELLOW = (255, 255, 0), (224, 207, 18)
tick = 0

class Button:
    def __init__(self, text, text_size, text_color, button_color, button_cover_color, button_pos):
        self.button_color = button_color
        self.button_cover_color = button_cover_color
        self.font = pg.font.SysFont(None, text_size)
        # поверхность и Rect текста:
        self.text_surf = self.font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=button_pos)
        # т. к. она прилегает к тексту вплотную, делаем поверхность и Rect кнопки, границы к-рой будут на 50px дальше:
        self.button_surf = pg.Surface((self.text_surf.get_width() + 25, self.text_surf.get_height() + 25))
        self.button_rect = self.button_surf.get_rect(center=button_pos)
        self.button_surf.fill(button_color)
        pg.draw.rect(self.button_surf, GREEN, (0, 0, self.button_rect.width, self.button_rect.height), 3)

    def redraw(self, state):  # state = True, если курсор на кнопке; state = False, если курсор вне кнопки
        if state:
            self.button_surf.fill(self.button_cover_color)
            pg.draw.rect(self.button_surf, GREEN, (0, 0, self.button_rect.width, self.button_rect.height), 3)
        else:
            self.button_surf.fill(self.button_color)
            pg.draw.rect(self.button_surf, GREEN, (0, 0, self.button_rect.width, self.button_rect.height), 3)

    def draw(self, screen):
        screen.blit(self.button_surf, self.button_rect)
        screen.blit(self.text_surf, self.text_rect)


def check_click_on_button(button):
    global player
    if button.button_rect.collidepoint(pg.mouse.get_pos()):
        player.redraw()


def check_mouse_on_button(button):
    if button.button_rect.collidepoint(pg.mouse.get_pos()):
        button.redraw(state=True)
    else:
        button.redraw(state=False)

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

    def redraw(self):
        player.r = 30
        self.surf.fill((0, 0, 0, 0))
        pg.draw.circle(self.surf, (*BRASS, 255), (self.rect.width / 2, self.rect.height / 2), self.r)
        self.mask = pg.mask.from_surface(self.surf)


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

class Text:
    def __init__(self, text, text_size, text_color, text_pos):
        self.font = pg.font.SysFont(None, text_size)
        self.suft = self.font.render(text, True, text_color)
        self.rect = self.suft.get_rect(center=text_pos)

    def draw(self, screen):
        screen.blit(self.suft, self.rect)

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()
player = Player()
foods = [Food(), Food(), Food()]


background = pg.Surface((WIDTH, HEIGHT))
background.fill(SILVER)

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
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            check_click_on_button(my_button)
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

    my_text = Text(f'Радиус игрока:{player.r}', 32, RED, (WIDTH / 2, HEIGHT * 0.2 / 10))
    my_button = Button("Сбросить", 64, GREEN, YELLOW, DARK_YELLOW, (WIDTH - 120, HEIGHT * 0.5 / 11))

    check_collisions(player, foods)
    check_mouse_on_button(my_button)

    screen.blit(background, (0, 0))
    for elem in foods:
        if elem.active:
            elem.draw(screen)
    foods = [elem for elem in foods if elem.active]
    player.draw(screen)
    my_text.draw(screen)
    my_button.draw(screen)
    pg.display.update()

