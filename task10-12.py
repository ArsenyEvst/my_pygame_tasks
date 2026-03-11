import pygame as pg
import random

FPS = 60
WIDTH, HEIGHT = 600, 900
WHITE = (255, 255, 255)
SILVER = (164, 164, 164)
tick = 0


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(r'images/car_orig.png').convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT / 2))
        self.mask = pg.mask.from_surface(self.image)
        self.speed = 3

    def update(self, dx=0, dy=0):
        if (self.rect.left + dx * self.speed) > 0 and (self.rect.right + dx * self.speed) < WIDTH:
            self.rect.x += dx * self.speed
        if (self.rect.top + dy * self.speed) > 0 and (self.rect.bottom + dy * self.speed) < HEIGHT:
            self.rect.y += dy * self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class EnemyCar(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        cars_images = [r'images/car2.png', r'images/car3.png', r'images/car4.png']
        car_is = random.choice(cars_images)
        self.image_small = pg.image.load(car_is)
        self.image = pg.transform.scale(self.image_small, (self.image_small.get_width() * 1.5,
                                                           self.image_small.get_height() * 1.5))
        self.xC = random.randrange(0, 600, 15)
        self.yC = -25
        self.rect = self.image.get_rect(center=(self.xC, self.yC))
        self.mask = pg.mask.from_surface(self.image)
        self.speedC = random.randrange(3, 10)
        self.active = True

    def update(self):
        self.rect.y += self.speedC

    def draw(self, screen):
        screen.blit(self.image, self.rect)


pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
pg.display.set_caption("Игра")
clock = pg.time.Clock()
pg.mixer.music.load("sound/bgs.wav")
acSound = pg.mixer.Sound("sound/accident.wav")
pg.mixer.music.play(-1)

player = Player()
cars = pg.sprite.Group()

background = pg.Surface((WIDTH, HEIGHT))
background.fill(SILVER)
pg.draw.rect(background, WHITE, (190, 0, 20, HEIGHT))
pg.draw.rect(background, WHITE, (390, 0, 20, HEIGHT))

screen.blit(background, (0, 0))
pg.display.update()

flag_play = True
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

    if tick == 90:
        tick = 0
        cars.add(EnemyCar())

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT]:
        player.update(dx=-1)
    if keys[pg.K_RIGHT]:
        player.update(dx=1)
    if keys[pg.K_UP]:
        player.update(dy=-1)
    if keys[pg.K_DOWN]:
        player.update(dy=1)

    if pg.sprite.spritecollideany(player, cars, collided=pg.sprite.collide_mask):
        t = acSound.get_length()
        acSound.play()
        pg.time.wait(int(t) * 1000)
        break

    cars.update()

    screen.blit(background, (0, 0))
    player.draw(screen)
    cars.draw(screen)
    pg.display.update()
