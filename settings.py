'''
all settings for the game
'''
from os import path
# directory path for all images
img_dir = path.join(path.dirname(__file__), 'assests_img')
audio_dir = path.join(path.dirname(__file__), 'assests_audio')

# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
PLATFORM_BLUE = (64, 202, 201)
BLUE = (0, 0, 250)
YELLOW = (225, 225, 0)

# screen settings
TITLE = 'T-REX Run'
WIDTH = 675
HEIGHT = 225
FPS = 40

# game speed stuff
game_speed = 3
game_speed_change = 1.05
