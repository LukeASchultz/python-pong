import pygame, sys, random, Paddle, Ball
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((600, 400), 0, 32)
pygame.display.set_caption('Pong')
fpsClock = pygame.time.Clock()
pygame.font.init()
font = pygame.font.SysFont('Arial', 50)
fps = 30

points1 = 0
points2 = 0

p1 = Paddle.Paddle(screen, 20, 175) #screen, xpos, ypos
p2 = Paddle.Paddle(screen, 580, 175) #screen, xpos, ypos
b1 = Ball.Ball(screen, 300, 190, random.randint(0, 1), random.randint(0, 1), p1, p2, points1, points2) #screen, xpos, ypos, xdirection, ydirection, paddle objects, point variables

while True:
    screen.fill((0, 0, 0))
    keys = pygame.key.get_pressed()
    text1 = font.render(str(b1.points1), False, (255, 255, 255)) #sets up the point displays
    text2 = font.render(str(b1.points2), False, (255, 255, 255))

    screen.blit(text1, (225, 10)) #shows each players points
    screen.blit(text2, (345, 10))
    pygame.draw.line(screen, (255, 255, 255), (300, 0), (300, 400))

    if keys[K_w]: #checks which keys are held down
        p1.move(True)
    elif keys[K_s]:
        p1.move(False)
    if keys[K_UP]:
        p2.move(True)
    elif keys[K_DOWN]:
        p2.move(False)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    p1.show()
    p2.show()
    b1.show()
    b1.move()

    pygame.display.update()
    fpsClock.tick(fps)