import pygame as pg
vec = pg.math.Vector2

# ▁ ▂ ▄ ▅ ▆ ▇ █Parametre du jeu█ ▇ ▆ ▅ ▄ ▂ ▁

# colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BROWN = (106, 55, 5)

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "Tilemap Demo"
BGCOLOR = BROWN

TILESIZE = 64
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

WALL_IMG = 'tileGreen_39.png'

# Player settings
PLAYER_HEALTH = 100
PLAYER_SPEED = 280
PLAYER_ROT_SPEED = 200
PLAYER_IMG = 'manBlue_gun.png'
PLAYER_HIT_RECT = pg.Rect(0, 0, 35, 35)
BARREL_OFFSET = vec(30, 10)

# Gun settings
BULLET_IMG = 'bullet.png'
BULLET_SPEED = 500
BULLET_LIFETIME = 1000
BULLET_RATE = 150
KICKBACK = 200
GUN_SPREAD = 5
BULLET_DAMAGE = 10

# Mob settings
MOB_IMG = 'zombie1_hold.png'
MOB_SPEED = [150, 125, 100, 75]
#TODO si on veut faire spawn + de zombie a 150 de vitesse(norme) rajouter dans le tableau [150]
MOB_HIT_RECT = pg.Rect(0, 0, 30, 30)
MOB_HEALTH = 100
MOB_DAMAGE = 10
MOB_KNOCKBACK = 20
AVOID_RADIUS = 50

#Pnj setting
PNG_IMG = 'soldier1_reload.png'
PNJ_SPEED = 0
PNJ_HEALTH = 1000
PNJ_SPEED = 0
PNG_HIT_RECT = pg.Rect(0, 0, 30, 30)
PNG_DAMAGE = 0

#Boss settings
BOSS_SPEED = 0

#Effect
MUZZLE_FLASHES = ['muzzle1.png', 'muzzle2.png', 'muzzle3.png', 'muzzle4.png']
FLASH_DURATION = 40

#Layers
WALL_LAYER = 1
PLAYER_LAYER = 2
BULLET_LAYER = 3
MOB_LAYER = 2
EFFECT_LAYER = 4
PNJ_LAYER = 2
