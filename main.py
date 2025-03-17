import pygame
import random

# Initialize pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# Background
background = pygame.image.load('background.jpg')

# Title and Icon
pygame.display.set_caption("Space Invader")
icon = pygame.image.load('alien.png')
pygame.display.set_icon(icon)

# Player
playerImg = pygame.image.load('space ship.png')
playerX = 370.0
playerY = 480.0
playerX_change = 0.0


def player(x, y):
    screen.blit(playerImg, (x, y))


# Enemy
enemyImg = pygame.image.load('squid.png')
enemyX = random.randint(0, 750)
enemyY = random.randint(50, 150)
enemyX_change = .2
enemyY_change = 40


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# Bullet
# ready - you can not see the bullet on screen
# fire - the bullet is currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 2
bullet_state = "ready"


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))


# Game Loop
running = True
while running:
    # RGB background
    screen.fill((0, 0, 0))
    # Background image
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # if keystroke is pressed check weather it is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.5
                # print("Left arrow is pressed")
            if event.key == pygame.K_RIGHT:
                playerX_change = .5
                # print("Right arrow is pressed")
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0.0
                # print("Keystroke has been released")

    # 5 = 5 + -0.1
    playerX = playerX + playerX_change
    # Checking for boundaries for player and enemy
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX = enemyX + enemyX_change
    if enemyX <= 0:
        enemyX_change = .2
        enemyY = enemyY + enemyY_change
    elif enemyX >= 736:
        enemyX_change = -.2
        enemyY = enemyY + enemyY_change

    # Bullet movement
    if bulletY <= -20:
        bulletY = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY = bulletY - bulletY_change

    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()
