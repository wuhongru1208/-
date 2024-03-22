import pygame
pygame.init()

windowSize = [400, 300]
screen = pygame.display.set_mode(windowSize)
pygame.display.set_caption("Circles")
colour = pygame.color.Color('#fcba03')
background_color = pygame.color.Color('#292ec4')

done = False
while not done:
    screen.fill(background_color)
    pygame.draw.circle(screen, colour, [200, 150], 50)
    pygame.display.flip()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.quit()
