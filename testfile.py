import pygame
pygame.init()

size = width, height = 1000, 500
speed = [2, 2]
white = 255, 255, 255

screen = pygame.display.set_mode(size)

loadghost = pygame.image.load("ghost.png")
ghost = pygame.Surface.convert_alpha(loadghost)
ghostrect = ghost.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ghostrect = ghostrect.move(speed)
    if ghostrect.left < 0 or ghostrect.right > width:
        speed[0] = -speed[0]
    if ghostrect.top < 0 or ghostrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(white)
    screen.blit(ghost, ghostrect)
    pygame.display.flip()