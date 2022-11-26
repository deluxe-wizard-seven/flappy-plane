from os import getcwd
from os.path import exists, join
from functools import reduce

WIDTH = 480
HEIGHT = 800

BG_IMG_URL = reduce(join, [getcwd(), "graphics", "environment", "background.png"])

assert exists(BG_IMG_URL), "Background Image Not Found"

BG_VELOCITY = 275

TERRAIN_IMG_URL = reduce(join, [getcwd(), "graphics", "environment", "ground.png"])

assert exists(BG_IMG_URL), "Terrain (Ground) Image Not Found"

TERRAIN_VELOCITY = 200

AEROPLANE_IMG_URLS = [
    reduce(join, [getcwd(), "graphics", "plane", f"red{i}.png"]) for i in range(3)
]

for aeroplane_img_url in AEROPLANE_IMG_URLS:
    if not exists(aeroplane_img_url):
        raise AssertionError("Aeroplane Images Not Found")

AEROPLANE_IMG_SCALE_FACTOR = 1.2
AEROPLANE_INITIAL_POS = (WIDTH / 12, HEIGHT / 2)
GRAVITY = 600
UP_STEP = 400

ACCELERATION = 1e-9

ANIMATION_RATE = 29.5

ROTO_ZOOM_FACTOR = 0.04

OBSTACLE_IMG_URLS = [
    reduce(join, [getcwd(), "graphics", "obstacles", f"{str(i)}.png"]) for i in range(2)
]

for obstacle_img_url in OBSTACLE_IMG_URLS:
    if not exists(obstacle_img_url):
        raise AssertionError("Obstacle Images Not Found")

OBSTACLE_DIST_LIMITS = 30, 100
OBSTACLE_HEIGHT_LIMITS = 10, 40
OBSTACLE_VELOCITY = 250

SIGHT_LIMIT = -100

PULSE = 1300

FONT_SIZE = 50
FONT_URL = reduce(join, [getcwd(), "graphics", "font", "BD_Cartoon_Shout.ttf"])

assert exists(FONT_URL), "Font File Not Found"

BG_MUSIC_URL = reduce(join, [getcwd(), "sounds", "music.wav"])

assert exists(BG_MUSIC_URL), "Background Music Not Found"

JUMP_MUSIC_URL = reduce(join, [getcwd(), "sounds", "jump.wav"])

assert exists(JUMP_MUSIC_URL), "Jump Music Not Found"

CRASH_MUSIC_URL = reduce(join, [getcwd(), "sounds", "crash.wav"])

assert exists(CRASH_MUSIC_URL), "Crash Music Not Found"

BG_MUSIC_VOLUME = 1
JUMP_MUSIC_VOLUME = 0.5
CRASH_MUSIC_VOLUME = 1
