import pygame
import time
import random
import math
import numpy as np
from pygame import mixer

# init
pygame.init()

# screen
X = 800
Y = 600
screen = pygame.display.set_mode((X, Y))

# clock/ FPS
clock = pygame.time.Clock()

# Background
background = pygame.image.load('background.png')

# Background music

mixer.music.load('background.wav')
mixer.music.play(-1)

# Title and Icon

pygame.display.set_caption('Space Invaders')
ICON = pygame.image.load('ufo.png')
pygame.display.set_icon(ICON)

# Player

PLAYERIMAGE = pygame.image.load('spaceship.png')
playerX = X // 2
playerY = Y - 100
player_XCHANGE = 0

# Enemy
ENEMYIMAGE = np.array([])  # pygame.image.load('enemy.png')
enemyX = np.array([])  # random.randint(0, X)
enemyY = np.array([])  # random.randint(300, Y)
enemy_XCHANGE = np.array([])  # 2
enemy_YCHANGE = np.array([])  # 40
enemies = 4

# Collision
for i in range(enemies):
    ENEMYIMAGE = np.append(ENEMYIMAGE, pygame.image.load('enemy.png'))
    enemyX = np.append(enemyX, random.randint(0, X))
    enemyY = np.append(enemyY, random.randint(300, Y))
    enemy_XCHANGE = np.append(enemy_XCHANGE, 2)
    enemy_YCHANGE = np.append(enemy_YCHANGE, 40)

# Bullet
BULLETIMAGE = pygame.image.load('bullet.png')
bulletX = 0
bulletY = playerY
bullet_XCHANGE = 0
bullet_YCHANGE = 10
bullet_state = 'Ready'

# Score
score = 0
font = pygame.font.Font('Bristone.ttf', 32)

textX = 10
textY = 10

# game over text
over_font = pygame.font.Font('Bristone.ttf', 32*2)


def sscore(x, y):
    global font, score
    scorer = font.render("Score :" + str(score), True, (255, 255, 255))
    screen.blit(scorer, (x, y))


def gameover():
    scorer = font.render("GAME OVER!", True, (255, 255, 255))
    screen.blit(scorer, (200, 250))


def player(x, y):
    screen.blit(PLAYERIMAGE, (x, y))


def enemy(x, y, i):
    screen.blit(ENEMYIMAGE[i], (x, y))


def fire(x, y):
    global bullet_state
    bullet_state = 'fire!'
    screen.blit(BULLETIMAGE, (x + 16, y + 10))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((enemyX - bulletX) ** 2 + (enemyY - bulletY) ** 2)
    if distance < 27:
        return True
    else:
        return False


def render(fnt, what, color, where):
    "Renders the fonts as passed from display_fps"
    text_to_show = fnt.render(what, 0, pygame.Color(color))
    screen.blit(text_to_show, where)


def display_fps():.0
    "Data that will be rendered and blitted in _display"
    render(
        pygame.font.Font('Bristone.ttf', 32),
        what=str(int(clock.get_fps())),
        color="orange",
        where=(700, 0))


# Game Loop
running = True
while running:
    # RGB -Red, Green, Blue
    screen.fill((10, 25, 100))

    # BackG
    screen.blit(background, (0, 0))

    display_fps()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            running = False
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                player_XCHANGE = -2
            elif i.key == pygame.K_RIGHT:
                player_XCHANGE = 2
            elif i.key == pygame.K_SPACE:
                if bullet_state is 'Ready':
                    bullet_sound = mixer.Sound('lazer.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire(bulletX, bulletY)
        elif i.type == pygame.KEYUP:
            if i.key == pygame.K_RIGHT or i.key == pygame.K_LEFT:
                player_XCHANGE = 0

    if playerX <= 0:
        playerX = 0
    elif playerX >= 768:
        playerX = 768

    # Enemy Movement
    for i in range(enemies):

        # # game over
        # if enemyY[i] > 440:
        #     for j in range(enemies):
        #         enemyY[j] = 2000
        #     gameover()
        #     break

        enemyX[i] += enemy_XCHANGE[i]
        if enemyX[i] <= 0:
            enemy_XCHANGE[i] = 2
            enemyY[i] += enemy_YCHANGE[i]
        elif enemyX[i] >= 768:
            enemy_XCHANGE[i] = -2
            enemyY[i] += enemy_YCHANGE[i]
        elif enemyY[i] >= Y - 130:
            enemyY[i] = 0

        # Collision
        collion = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collion:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = playerY
            bullet_state = 'Ready'
            score += 1
            enemyX[i] = random.randint(0, X)
            enemyY[i] = random.randint(300, Y)
        enemy(enemyX[i], enemyY[i], i)

    # Bullet Movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'Ready'
    if bullet_state == 'fire!':
        fire(bulletX, bulletY)
        bulletY -= bullet_YCHANGE

    # Call
    playerX += player_XCHANGE
    enemyX += enemy_XCHANGE

    # Checking for boundaries

    player(playerX, playerY)
    sscore(textX, textY)
    pygame.display.update()
    clock.tick(500)
