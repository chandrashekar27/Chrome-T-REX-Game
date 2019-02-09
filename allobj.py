"""
Define most classes and functions
"""
import pygame
pygame.display.set_mode()
from os import path
img_dir = path.join(path.dirname(__file__), 'assests_img')

WIDTH = 750
HEIGHT = 275

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLATFORM_BLUE = (64, 202, 201)
BLUE = (0, 0, 250)
# the main player (dino) sprite


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # size in pixels
        # 41x43 for standing
        # 40x43 for running
        # 55x26 for ducking
        # load all images of sprite
        self.player_jump = pygame.image.load(path.join(img_dir, "dino_jump.png")).convert()
        self.player_run1 = pygame.image.load(path.join(img_dir, "dino_run_1.png")).convert()
        self.player_run2 = pygame.image.load(path.join(img_dir, "dino_run_2.png")).convert()
        self.player_duck1 = pygame.image.load(path.join(img_dir, "dino_duck_1.png")).convert()
        self.player_duck2 = pygame.image.load(path.join(img_dir, "dino_duck_2.png")).convert()
        self.image = self.player_jump
        self.rect = self.image.get_rect()
        self.rect.center = (40, HEIGHT - 38)
        self.acc = 9.5  # 8 for small jump(adding later)
        self.y_vel = 0
        self.gravity = 0.5
        self.last_update = 0
        self.duck = False
        self.current_frame = 0
    # make player jump

    def jump(self):
        self.y_vel -= self.acc

    def update(self):
        # check if player is ducking
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_DOWN]:
            self.duck = True
        else:
            self.duck = False
        # check if player is in air
        if self.rect.bottom < HEIGHT - 16:
            self.image = pygame.transform.scale(self.player_jump, (41, 43))
            prev_x = self.rect.centerx
            prev_y = self.rect.bottom
            self.rect = self.image.get_rect()
            self.rect.centerx = prev_x
            self.rect.bottom = prev_y
        else:
            # make player look like running
            now = pygame.time.get_ticks()
            if self.duck:
                if now - self.last_update > 100:
                    self.last_update = now
                    self.current_frame += 1
                    if self.current_frame % 2 == 0:
                        self.image = pygame.transform.scale((self.player_duck1), (55, 26))
                        prev_x = self.rect.centerx
                        prev_y = self.rect.bottom
                        self.rect = self.image.get_rect()
                        self.rect.centerx = prev_x
                        self.rect.bottom = prev_y
                    else:
                        self.image = pygame.transform.scale((self.player_duck2), (55, 26))
                        prev_x = self.rect.centerx
                        prev_y = self.rect.bottom
                        self.rect = self.image.get_rect()
                        self.rect.centerx = prev_x
                        self.rect.bottom = prev_y
            else:
                if now - self.last_update > 100:
                    self.last_update = now
                    self.current_frame += 1
                    if self.current_frame % 2 == 0:
                        self.image = pygame.transform.scale((self.player_run1), (40, 43))
                        prev_x = self.rect.centerx
                        prev_y = self.rect.bottom
                        self.rect = self.image.get_rect()
                        self.rect.centerx = prev_x
                        self.rect.bottom = prev_y
                    else:
                        self.image = pygame.transform.scale((self.player_run2), (40, 43))
                        prev_x = self.rect.centerx
                        prev_y = self.rect.bottom
                        self.rect = self.image.get_rect()
                        self.rect.centerx = prev_x
                        self.rect.bottom = prev_y
        # check if player jumps
        if not self.duck:
            if keystate[pygame.K_UP] or keystate[pygame.K_SPACE]:
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


class Plant(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

# the bird enemy. contains all heights


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)



# platform png to show
platform_img = pygame.image.load(path.join(img_dir, 'platform.png')).convert()
platform_img.set_colorkey(PLATFORM_BLUE)

# the main platform


class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((3000, 3))
        self.image.fill(BLACK)
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.top = y
        self.scrollx = 0
        self.speed = 5
# fuction to display text on the screen


def text(window, text, size, x, y, color='black', font='arial'):
    # set font to what user wants, else default font
    font_name = pygame.font.match_font(font)
    # set parameters of the text
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.centerx = x
    text_rect.centery = y
    # blit(display) the text on the given screen
    window.blit(text_surface, text_rect)
