from pygame import *
from pygame.locals import *

class BaseObject():
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.surface = Surface((60, 60))
        self.AABB = Rect(x, y, 60, 60)
        self.color = color
    def getAABB(self):
        return self.AABB
    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))
