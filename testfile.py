import os
import sys
import pygame
import random
from pygame import *
pygame.init()

scr_size = (width,height) = (600,150)
FPS = 60
gravity = 0.6

black = (0,0,0)
white = (255,255,255)
background_col = (235,235,235)

high_score = 0

screen = pygame.display.set_mode(scr_size)
clock = pygame.time.Clock()


def load_image(
    name,
    sizex=-1,
    sizey=-1,
    colorkey=None,
    ):

    fullname = os.path.join('images', name)
    image = pygame.image.load(fullname)
    image = image.convert()
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)

    if sizex != -1 or sizey != -1:
        image = pygame.transform.scale(image, (sizex, sizey))

    return (image, image.get_rect())

class Player:
# creates player and contains information on qualities
    def __init__(self, name, speed, filename):
        self.name = name
        self.speed = speed
        self.filename = filename
loadghost = pygame.image.load("ghost.png")
ghostfile = pygame.Surface.convert_alpha(loadghost)
loaddino = pygame.image.load("dinosaur.png")
dinofile = pygame.Surface.convert_alpha(loaddino)
ghost = Player('ghost', 2, ghostfile)
dino = Player('dino', 2, dinofile)
ghostrect = ghostfile.get_rect()
dinorect = dinofile.get_rect()

x = 0
y = 0
velx = 2
vely = 0
accy = .1
jumping = False



while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            sys.exit()
        if e.type == pygame.KEYDOWN:
            jumping = True



    for event in pygame.key.get_pressed(K_SPACE):
        if event.type == pygame.QUIT: sys.exit()

    ghostrect = ghostrect.move(speed)
    if ghostrect.left < 0 or ghostrect.right > width:
        speed[0] = -speed[0]
    if ghostrect.top < 0 or ghostrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(white)
    screen.blit(ghost, ghostrect)
    pygame.display.flip()