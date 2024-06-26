import pygame
import random
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
clock = pygame.time.Clock()

white = pygame.color.Color("#FFFFFF")
black = pygame.color.Color("#000000")
btnColour = pygame.color.Color("#A45C8F")

btnWidth = 50
btnLength = 20
btnX = (windowSize[0] - btnWidth)/2
btnY = (windowSize[1] - btnLength)/2

toggled = False
pos = (0, 0)
points=0
done = False
while not done:
    if toggled:
        screen.fill(black)
    else:
        screen.fill(white)

    pygame.draw.rect(screen, btnColour, [btnX, btnY, btnWidth, btnLength])

    if btnX <= pos[0] <= btnX + btnWidth and btnY <= pos[1] <= btnY + btnLength:
        toggled = not toggled
        pos = (0, 0)
        points += 1

    btnX += random.randint(-1 - points, 1 + points)
    btnY += random.randint(-1 - points, 1 + points)

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            done = True
    pygame.display.flip()
    clock.tick(10)
pygame.quit()

print(points)
