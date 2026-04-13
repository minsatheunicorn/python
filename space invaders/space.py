import random
import pygame
import math

SCREEN_WIDTH=800
SCREEN_HEIGHT=500
PLAYER_START_X=370
PLAYER_START_Y=380
ENEMY_START_Y_MIN=50
ENEMY_START_Y_MAX=150
ENEMY_SPEED_X=4
ENEMY_SPEED_Y=40
BULLET_SPEED_Y=10
COLISION_DISTANCE=27

pygame.init()
screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
background=pygame.image.load("background1.png")

pygame.display.set_caption("space invaders")
icon=pygame.image.load("ufo.png")
playerimg=pygame.image.load("space-invaders.png")
playerx=PLAYER_START_X
playery=PLAYER_START_Y
playerx_change=0

enemyimg=[]
enemyx=[]
enemyy=[]
enemyx_change=[]
enemyy_change=[]
num_off_enemys=6

for i in range(num_off_enemys):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyy.append(random.randint(ENEMY_START_Y_MIN,ENEMY_START_Y_MAX))
    enemyx.append(random.randint(0,SCREEN_WIDTH-64))