"""
main .py script to run to play the game
consists of the main game loop
"""
import os
# import other scripts
from allobj import *
# basic settings
WIDTH = 750
HEIGHT = 350
FPS = 20


# set up the pygame window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
screen.fill(WHITE)
clock = pygame.time.Clock()
# set caption
pygame.display.set_caption('T-REX Run')
# set icon for game
game_icon = pygame.image.load('game_icon.ico')
pygame.display.set_icon(game_icon)

# make a group that has all sprites
all_sprites = pygame.sprite.Group()
# the platform sprite
main_platform = Platform()

# start the main game loop
running = True
alive = False
# display start screen stuff
screen.blit(main_platform.image, (0, HEIGHT - 20))
while running:

    # check for inputs
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
        # check if player starts game
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_UP:
                alive = True
    if alive:
        # white screen to draw on next frame
        screen.fill(WHITE)
        # keep the platform scrolling
        rel_x = main_platform.scrollx % main_platform.rect.width
        if rel_x < WIDTH:
            screen.blit(main_platform.image, (rel_x, HEIGHT - 20))
        main_platform.scrollx -= main_platform.speed
        screen.blit(main_platform.image, (rel_x - main_platform.rect.width, HEIGHT - 20))

    #  Update
    all_sprites.update()
    #  Draw / render
    all_sprites.draw(screen)
    #  keep loop running at the right speed
    clock.tick(FPS)
    print(str(clock.get_fps()))
    # flip the dislay
    pygame.display.flip()
# quit pygame
pygame.quit()
quit()
