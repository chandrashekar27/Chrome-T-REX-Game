"""
main .py script to run to play the game
consists of the main game loop
"""
import os
import random
import time
# import other scripts
from allobj import *
# fps
FPS = 60


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
main_platform = Platform(WIDTH / 2, HEIGHT - 17)
all_sprites.add(main_platform)
# player sprite
the_player = Player()
#print(the_player.rect.bottom)
all_sprites.add(the_player)
# start the main game loop
running = True
alive = False
platform_img = pygame.image.load(path.join(img_dir, "platform.png")).convert()
platform_img.set_colorkey(PLATFORM_BLUE)
# display start screen stuff
screen.blit(platform_img, (0, HEIGHT - 20))
all_sprites.draw(screen)
# flip the dislay
pygame.display.flip()
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
        rel_x = main_platform.scrollx % 1189
        if rel_x < WIDTH:
            screen.blit(platform_img, (rel_x, HEIGHT - 20))
        main_platform.scrollx -= main_platform.speed
        screen.blit(platform_img, (rel_x - 1189, HEIGHT - 20))
        #  Update
        all_sprites.update()
        #  Draw / render
        all_sprites.draw(screen)
        # flip the dislay
        pygame.display.flip()
    #  keep loop running at the right speed
    clock.tick(FPS)
    # print(str(clock.get_fps()))
    print(pygame.sprite.collide_rect_ratio(1)(main_platform, the_player))
# quit pygame
pygame.quit()
quit()
