import random
import pygame
pygame.init()

width = 400
height = 300
windowSite = [ width, height]
screen = pygame.display.set_mode(windowSite)
clock = pygame.time.Clock()

sqrW = int(width / 10)
sqrH = int(height / 10)

done = False
while not done:
    red = random.randrange(0, 256)
    green = random.randrange(0, 256)
    blue = random.randrange(0, 256)
    x = random.randrange(0, width, sqrW)
    y = random.randrange(0, height, sqrH)
    pygame.draw.rect(screen, (red, green, blue), (x, y, sqrW, sqrH))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(10)
pygame.quit()
