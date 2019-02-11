"""
Define most classes and functions
"""
import pygame as pg
from os import path
pg.display.set_mode()
img_dir = path.join(path.dirname(__file__), 'assests_img')

WIDTH = 675
HEIGHT = 225

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLATFORM_BLUE = (64, 202, 201)
BLUE = (0, 0, 250)
# the main player (dino) sprite


class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        # size in pixels
        # 41x43 for standing
        # 40x43 for running
        # 55x26 for ducking
        # load all images of sprite
        self.player_jump = pg.image.load(path.join(img_dir, "dino_jump.png")).convert()
        self.player_run1 = pg.image.load(path.join(img_dir, "dino_run_1.png")).convert()
        self.player_run2 = pg.image.load(path.join(img_dir, "dino_run_2.png")).convert()
        self.player_duck1 = pg.image.load(path.join(img_dir, "dino_duck_1.png")).convert()
        self.player_duck2 = pg.image.load(path.join(img_dir, "dino_duck_2.png")).convert()
        self.image = self.player_jump
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT - 38)
        self.acc = 9.5  # 8 for small jump(adding later)
        self.y_vel = 0
        self.gravity = 0.5
        self.last_update = 0
        self.duck = False
        self.current_frame = 0
        self.now = 0
    # make player jump

    def jump(self):
        self.y_vel -= self.acc

    def update(self):
        # for changing frame
        prev_x = self.rect.centerx
        prev_y = self.rect.bottom
        # check if player is ducking
        keystate = pg.key.get_pressed()
        if keystate[pg.K_DOWN]:
            self.duck = True
        else:
            self.duck = False
        # check if player is in air
        if self.rect.bottom < HEIGHT - 30:
            # if already high enough, check for duck
            if self.duck:
                self.y_vel += (self.acc - 7)
        elif self.rect.bottom < HEIGHT - 16:
            # change sprite if just jumped
            self.image = pg.transform.scale(self.player_jump, (41, 43))
        else:
            # make player look like running
            self.now = pg.time.get_ticks()
            if self.duck:
                if self.now - self.last_update > 100:
                    self.last_update = self.now
                    self.current_frame += 1
                    if self.current_frame % 2 == 0:
                        self.image = pg.transform.scale((self.player_duck1), (55, 26))
                    else:
                        self.image = pg.transform.scale((self.player_duck2), (55, 26))
            else:
                if self.now - self.last_update > 100:
                    self.last_update = self.now
                    self.current_frame += 1
                    if self.current_frame % 2 == 0:
                        self.image = pg.transform.scale((self.player_run1), (40, 43))
                    else:
                        self.image = pg.transform.scale((self.player_run2), (40, 43))
        # whatever image changed to, change rect
        self.rect = self.image.get_rect()
        self.rect.centerx = prev_x
        self.rect.bottom = prev_y
        # check if player jumps
        if not self.duck:
            if keystate[pg.K_UP] or keystate[pg.K_SPACE]:
                if not self.rect.bottom < HEIGHT - 16:
                    self.jump()
        # make the player fall down
        if self.rect.bottom < HEIGHT - 16:
            self.y_vel += self.gravity
        # change positon of player based on y_vel
        self.rect.y += self.y_vel
        # keep the player above the ground
        if self.rect.bottom > HEIGHT - 16:
            self.rect.bottom = HEIGHT - 16
            self.y_vel = 0

# the plant enemy. contains all sizes


class Plant(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image1 = pg.image.load(path.join(img_dir, 'small_plant_1.png')).convert()
        self.image2 = pg.image.load(path.join(img_dir, 'small_plant_2.png')).convert()
        self.image3 = pg.image.load(path.join(img_dir, 'small_plant_3.png')).convert()
        self.image4 = pg.image.load(path.join(img_dir, 'big_plant_1.png')).convert()
        self.image5 = pg.image.load(path.join(img_dir, 'big_plant_2.png')).convert()
        self.image6 = pg.image.load(path.join(img_dir, 'big_plant_3.png')).convert()

# the bird enemy. contains all heights


class Birds(pg.sprite.Sprite):
    def __init__(self, level, x):
        pg.sprite.Sprite.__init__(self)
        self.image1 = pg.image.load(path.join(img_dir, 'bird_1.png')).convert()
        self.image2 = pg.image.load(path.join(img_dir, 'bird_2.png')).convert()
        # variables to animate birds
        self.speed = 3
        self.prev_update = 0
        self.level = level
        self.image = self.image1
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.x = x
        # to see which image the sprite is currently
        self.current_frame = 0
        # set x coordinate based on input
        self.rect.centerx = self.x
        # decide the y coordinate (level) of the bird
        if self.level == 0:
            self.rect.centery = HEIGHT - 35
        elif self.level == 1:
            self.rect.centery = HEIGHT - 75
        else:
            self.rect.centery = HEIGHT - 125

    def update(self):
        # delete bird if out of screen
        if self.rect.right < -1:
            self.kill()
        else:
            # make the bird move to the left
            self.rect.x -= self.speed
            # make the bird 'flap'
            now = pg.time.get_ticks()
            if now - self.prev_update > 300:
                self.prev_update = now
                self.current_frame += 1
                prev_x = self.rect.centerx
                prev_y = self.rect.y
                if self.current_frame % 2 == 0:
                    self.image = self.image2
                else:
                    self.image = self.image1
                self.rect = self.image.get_rect()
                self.rect.centerx = prev_x
                self.rect.y = prev_y


# platform png to show
platform_img = pg.image.load(path.join(img_dir, 'platform.png')).convert()
platform_img.set_colorkey(PLATFORM_BLUE)

# the main platform


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((3000, 3))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.scrollx = 0
        self.speed = 3
# fuction to display text on the screen


def text(window, text, size, x, y, color='black', ufont='arial'):
    # set font to what user wants, else default font
    font_name = pg.font.match_font(ufont)
    # set parameters of the text
    text_surface = font_name.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    # blit(display) the text on the given screen
    window.blit(text_surface, text_rect)
