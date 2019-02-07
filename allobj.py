"""
Define most classes and functions
"""
import pygame
pygame.display.set_mode()
from os import path
img_dir = path.join(path.dirname(__file__), 'assests_img')

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLATFORM_BLUE = (64, 202, 201)
BLUE = (0, 0, 250)
# the main player (dino) sprite


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        # load all images of sprite

# the plant enemy. contains all sizes


class Plant(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

# the bird enemy. contains all levels


class Bird(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

# the main platform


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(path.join(img_dir, 'platform.png')).convert()
        self.image.set_colorkey(PLATFORM_BLUE)
        self.rect = self.image.get_rect()
        self.scrollx = 0
        self.speed = 2
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
