import pygame
import random

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'top g'
WHITE_COLOR = (255, 255, 255)
BLACK_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption(SCREEN_TITLE)

player_img = pygame.image.load('player.png')
enemy_img = pygame.image.load('enemy.png')

class Player(pygame.sprite.Sprite):
 speed = 10

def __init__(self):
    super().__init__()
    self.image = player_img
    self.rect = self.image.get_rect()
    self.rect.x = SCREEN_WIDTH // 2
    self.rect.bottom = SCREEN_HEIGHT

def move_left(self):
    self.rect.x -= self.speed
    if self.rect.left < 0:
        self.rect.left = 0

def move_right(self):
    self.rect.x += self.speed
    if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH

def shoot(self):
    bullet = Bullet(self.rect.x + self.rect.width // 2, self.rect.y)
    bullets.add(bullet)

class Enemy(pygame.sprite.Sprite):
 speed = 10

def __init__(self):
    super().__init__()
    self.image = enemy_img
    self.rect = self.image.get_rect()
    self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
    self.rect.y = random.randint(-SCREEN_HEIGHT, -100)

def update(self):
    self.rect.y += self.speed

    if self.rect.y > SCREEN_HEIGHT:
        self.rect.y = random.randint(-SCREEN_HEIGHT, -100)
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
