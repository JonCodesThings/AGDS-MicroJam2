from pygame import *
from pygame.locals import *

class BaseObject():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.surface = Surface((60, 60))
        self.AABB = Rect(x, y, 60, 60)
        self.color = color
    def getColor(self):
        return self.color
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def getAABB(self):
        return self.AABB
    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
