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
pg.init()
pg.mixer.init()
screen = pg.display.set_mode([WIDTH, HEIGHT])
screen.fill(WHITE)
clock = pg.time.Clock()
# set caption
pg.display.set_caption('T-REX Run')
# set icon for game
game_icon = pg.image.load('game_icon.ico')
pg.display.set_icon(game_icon)

# make a group that has all sprites
all_sprites = pg.sprite.Group()
# other groups for other objets
all_birds = pg.sprite.Group()
# the platform sprite
main_platform = Platform(WIDTH / 2, HEIGHT - 17)
all_sprites.add(main_platform)
# player sprite
the_player = Player()
all_sprites.add(the_player)
# start the main game loop
running = True
alive = False
platform_img = pg.image.load(path.join(img_dir, "platform.png")).convert()
platform_img.set_colorkey(PLATFORM_BLUE)
# display start screen stuff
screen.blit(platform_img, (0, HEIGHT - 20))
all_sprites.draw(screen)
# flip the dislay
pg.display.flip()
while running:

    # check for inputs
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        # check if player starts game
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE or event.key == pg.K_UP:
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
        all_birds.update()
        #  Draw / render
        all_sprites.draw(screen)
        # flip the dislay
        pg.display.flip()
    #  keep loop running at the right speed
    clock.tick(FPS)
    print(str(clock.get_fps()))
    # print(pg.sprite.collide_rect_ratio(1)(main_platform, the_player))
# quit pygame
pg.quit()
quit()
