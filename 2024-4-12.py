import random
import pygame

size = [400, 300]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

x = size[0] // 2
y = size[1] // 2

ballX = random.randrange(0, size[0])
ballY = random.randrange(0, size[1])

goalX = size[0] // 2 - 10
goalY = size[1] // 2 - 10
goalW = 20
goalH = 20

points = 0

red = pygame.color.Color('#FF8080')
blue= pygame.color.Color('#8080FF')
white = pygame.color.Color('#FFFFFF')
black = pygame.color.Color('#000000')

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

    if -10 < y -ballY < 10 and -10 < x - ballX < 10:
        pygame.draw.circle(screen, white, [x, y], 15)

        xDiff = x - ballX
        yDiff = y - ballY

        if ballX == 0:
            xDiff -= 5
        elif ballX == size[0]:
            xDiff += 5
        if ballY == 0:
            xDiff -= 5
        elif ballY == size[1]:
            yDiff += 5

        x += xDiff * 2
        ballX -= xDiff * 2

        y += yDiff * 2
        ballY -= yDiff * 2

done = False
while not done:
    screen.fill(black)

    pygame.draw.rect(screen, white, (goalX, goalY, goalW, goalH))

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
    ballY = checkOffScreenX(ballY)

    checkTouching()

    for point in range(points):
        pointX = 0 + point * 5
        pygame.draw.rect(screen, white, (pointX, 3, 4, 7))

    pygame.draw.circle(screen, red, [x, y], 6)

    pygame.draw.circle(screen, blue, [ballX, ballY], 6)

    if goalX <= ballX <= goalX + goalH and goalY <= ballY <= goalY +goalH:
        points += 1
        ballX = random.randrange(0, size[0])
        ballY = random.randrange(0, size[1])

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    clock.tick(72)
pygame.quit()

print("Total points: " + str(points))
