import pygame, random

class Ball(object):
    def __init__(self, screen, xpos, ypos, xDirection, yDirection, p1, p2, points1, points2):
        self.screen = screen
        self.xpos = xpos
        self.ypos = ypos
        self.xDirection = xDirection
        self.yDirection = yDirection
        self.p1 = p1
        self.p2 = p2
        self.points1 = points1
        self.points2 = points2

    def show(self):
        pygame.draw.circle(self.screen, (255, 255, 255), (self.xpos, self.ypos), 5)

    def move(self):
        if self.xDirection == 0: #moves the ball left or right
            self.xpos -= 5
        else:
            self.xpos += 5

        if self.yDirection == 0: #moves the ball up or down
            self.ypos -= 2
        else:
            self.ypos += 2

        self.colCheck()

    def reset(self): #resets the position of the ball
        self.xpos = 300
        self.ypos = 190
        self.xDirection = random.randint(0, 1)
        self.yDirection = random.randint(0, 1)

    def colCheck(self):
        if self.xDirection == 0: #checks if the ball touches a paddle
            if ((self.xpos == (self.p1.xpos + 5)) and (self.ypos > self.p1.ypos) and (self.ypos < (self.p1.ypos + 50))):
                self.xDirection = 1
        else:
            if ((self.xpos == self.p2.xpos) and (self.ypos > self.p2.ypos) and (self.ypos < (self.p2.ypos + 50))):
                self.xDirection = 0

        if self.xpos < 2: #checks if the ball touches a wall
            self.points2 += 1
            self.reset()
        elif self.xpos > 598:
            self.points1 += 1
            self.reset()

        if self.yDirection == 0: #checks if the ball hits the top or bottom
            if self.ypos < 0:
                self.yDirection = 1
        else:
            if self.ypos > 395:
                self.yDirection = 0