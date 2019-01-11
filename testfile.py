import pygame
import math
pygame.init()

f = 1/2 * m * v^2

size = width, height = 1000, 500
white = 255, 255, 255

screen = pygame.display.set_mode(size)

x = 0
y = 0
velx =1
vely = 0
accy = .1
jumping = False

class Player:
# creates player and contains information on qualities
    def __init__(self, name, speed, filename):
        self.name = name
        self.speed = speed
        self.filename = filename

        def moveRight(self, name, speed, file):
            




loadghost = pygame.image.load("ghost.png")
ghostfile = pygame.Surface.convert_alpha(loadghost)
loaddino = pygame.image.load("dino.png")
dinofile = pygame.Surface.convert_alpha(loaddino)
ghost = Player('ghost', 2, ghostfile)
dino = Player('dino', 2, dinofile)
ghostrect = ghostfile.get_rect()
dinorect = dinofile.get_rect()

while True:

    if pygame.key.pygame.key.get_pressed(K_SPACE):



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