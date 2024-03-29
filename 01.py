import random
import pygame
pygame.init()

size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x = size[0]//2
y = size[1]//2

ballX = random.randrange(0, size[0])
ballY = random.randrange(0, size[1])

red = pygame.color.Color("#FF8080")
blue = pygame.color.Color("#8080FF")
white = pygame.color.Color("#FFFFFF")
black = pygame.color.Color("#000000")



def checkOffScreenX(x):
    if x > size[0]:
        x = 0
    elif x < 0:
        x = size[0]
    return x


def checkOffScreenY(y):
    if y > size[1]:
        y = 0
    elif y < 0:
        y = size[1]
    return y

def checkTouching():

    global x
    global ballX
    global y
    global ballY

    if -10 < y - ballY < 10 and -10 < x - ballX < 10:
        pygame.draw.circle(screen, white, [x, y], 15)

        xDiff = x - ballX
        yDiff = y - ballY
        
        if ballX == 0:
            xDiff -= 5
        if ballX == size[0]:
            xDiff += 5
        if ballY == 0:
            yDiff -= 5
        if ballY == size[1]:
            yDiff += 5
        
        
        x += xDiff * 3
        ballX -= xDiff * 3
        
        y += yDiff * 3
        ballY -= yDiff * 3


done = False
while not done:
    screen.fill(black)

    keys = pygame.key.get_pressed()


    if keys[pygame.K_w]:
        y -= 1
    if keys[pygame.K_s]:
        y += 1
    if keys[pygame.K_a]:
        x -= 1
    if keys[pygame.K_d]:
        x += 1

    x = checkOffScreenX(x)
    y = checkOffScreenY(y)
    ballX = checkOffScreenX(ballX)
    ballY = checkOffScreenY(ballY)

    checkTouching()

    pygame.draw.circle(screen, red, [x, y], 6)

    pygame.draw.circle(screen, blue, [ballX, ballY], 6)

    pygame.display.flip()



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(72)
pygame.quit()
