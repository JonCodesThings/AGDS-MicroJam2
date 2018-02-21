import pygame, Input
from pygame.locals import *

class StringButton():
    def __init__(self, x, y, button, color):
        self.x = x
        self.y = y
        self.button = button
        self.surface = Surface((60, 60))
        self.isDown = False
        self.AABB = Rect(x, y, 60, 60)
        self.color = color
    def setDown(self, state):
        self.isDown = state
    def getDown(self):
        return self.isDown
    def getAABB(self):
        return self.AABB
    def render(self, screen):
        screen.blit(self.surface, (self.x, self.y))
    def update(self, dt):
        if isDown == True:
            self.surface.fill(Color(0, 0, 0))
        else:
            self.surface.fill(self.color)

class Zither():
    def __init__(self):
        self.smallButtonGroup = []
        self.bigButtonGroup = []
        self.inputBind = [K_z, K_x, K_c, K_v, K_b, K_n, K_m]
        self.numpadBind = [K_1, K_2, K_3]
        self.colorBind = [Color(255, 0, 0), Color(255, 165, 0), Color(255, 255, 0), Color(0, 255, 0), Color(0, 0, 255), Color(75, 0, 130), Color(238, 130, 238)]
        self.greyBind = [Color(192, 192, 192), Color(169, 169, 169), Color(128, 128, 128), Color(105, 105, 105)]
        for count in range(0, 7):
            self.bigButtonGroup.append(StringButton(((count+1) * 60), 700, self.inputBind[count], self.colorBind[count]))
        self.bigButtonGroup.append(StringButton(((9 * 60), 400, self.numpadBind[0], self.greyBind[0]))
        self.bigButtonGroup.append(StringButton(((10 * 60), 400, self.numpadBind[1], self.greyBind[1]))
        self.bigButtonGroup.append(StringButton(((11 * 60), 400, self.numpadBind[2], self.greyBind[2]))
    def update(self, dt, input_):
        
