import pygame

class Paddle(object):
    def __init__(self, screen, xpos, ypos):
        self.screen = screen
        self.xpos = xpos
        self.ypos = ypos

    def show(self):
        pygame.draw.rect(self.screen, (255, 255, 255), (self.xpos, self.ypos, 5, 50))

    def move(self, up): #moves the paddle up or down
        if up == True:
            if self.ypos > 0:
                self.ypos -= 5
        else:
            if self.ypos < 350:
                self.ypos += 5