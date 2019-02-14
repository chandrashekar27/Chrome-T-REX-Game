"""
main .py script to run to play the game
consists of the main game loop
"""
import os
import random
import time
# import other scripts
from allobj import *
# set up the pygame window
pg.init()
pg.mixer.init()
screen = pg.display.set_mode([WIDTH, HEIGHT])
screen.fill(WHITE)
clock = pg.time.Clock()
# set caption
pg.display.set_caption(TITLE)
# set icon for game
game_icon = pg.image.load('game_icon.ico')
pg.display.set_icon(game_icon)
# the game over image
game_over_img = pg.image.load(path.join(img_dir, "game_over.png")).convert()
game_over_img.set_colorkey(PLATFORM_BLUE)
# make a group that has all sprites
all_sprites = pg.sprite.Group()
# other groups for other objets
all_birds = pg.sprite.Group()
all_plants = pg.sprite.Group()
players = pg.sprite.Group()
running = True
alive = True
game_score = 0
# get the highscore
with open('highscore.txt', 'r+') as hs:
    try:
        highscore = int(hs.read())
    except:
        highscore = 0
while running:
    # for every new_game
    if not all_sprites and alive:
        # the platform sprite
        main_platform = Platform(WIDTH / 2, HEIGHT - 17)
        all_sprites.add(main_platform)
        # player sprite
        the_player = Player()
        all_sprites.add(the_player)
        players.add(the_player)
        # starting obstacles
        start_obs1 = Plant(get_enemy('plant'), WIDTH + 100)
        all_sprites.add(start_obs1)
        all_plants.add(start_obs1)
        # start the main game loop
        running = True
        if game_score == 0:
            alive = False
        game_score = 0
        game_speed = 4.5
        platform_img = pg.image.load(path.join(img_dir, "platform.png")).convert()
        platform_img.set_colorkey(PLATFORM_BLUE)
        # display start screen stuff
        screen.blit(platform_img, (0, HEIGHT - 20))
        all_sprites.draw(screen)
        # flip the dislay
        pg.display.flip()
    # check for inputs
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        # check if player starts game
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE or event.key == pg.K_UP:
                alive = True
        elif event.type == pg.MOUSEBUTTONDOWN:
            mousex, mousey = pg.mouse.get_pos()
            if (WIDTH / 2 - 17 <= mousex <= WIDTH / 2 + 17) and (105 - 15 <= mousey <= 105 + 18):
                alive = True
    if alive and all_sprites:
        # white screen to draw on next frame
        screen.fill(WHITE)
        # make the game speed faster
        game_speed += game_speed_change
        # change the score
        game_score += game_speed / 45
        # display the score
        text(screen, str(int(game_score)), 35, WIDTH - 45, 15)
        # keep the platform scrolling
        rel_x = main_platform.scrollx % 1189
        if rel_x < WIDTH:
            screen.blit(platform_img, (rel_x, HEIGHT - 20))
        main_platform.scrollx -= main_platform.speed
        screen.blit(platform_img, (rel_x - 1189, HEIGHT - 20))
        # make all sprites faster
        for s in all_sprites:
            s.speed = game_speed
        #  Update
        all_sprites.update()
        #  Draw / render
        all_sprites.draw(screen)
        # flip the dislay
        pg.display.flip()
        # check for death
        if pg.sprite.spritecollide(the_player, all_birds, False, pg.sprite.collide_mask) or pg.sprite.spritecollide(the_player, all_plants, False, pg.sprite.collide_mask):
            alive = False
            the_player.image = the_player.dead_dino
            screen.fill(WHITE)
            text(screen, str(int(game_score)), 35, WIDTH - 45, 15)
            screen.blit(platform_img, (rel_x - 1189, HEIGHT - 20))
            screen.blit(replay_img, (WIDTH / 2 - 15, 96))
            all_sprites.update()
            all_sprites.draw(screen)
            pg.display.flip()
            for s in all_sprites:
                s.kill()
            # update highscore, if needed
            if game_score > highscore:
                with open('highscore.txt', 'r+') as hs:
                    hs.write(str(int(game_score)))
                text(screen, 'NEW HIGHSCORE!', 35, WIDTH / 2, 25)
                pg.display.flip()
                #  keep loop running at the right speed
    clock.tick(FPS)
    print(str(clock.get_fps()))
    # print(pg.sprite.collide_rect_ratio(1)(main_platform, the_player))
# quit pygame
pg.quit()
quit()
