from pygame import *
from pygame.locals import *
from BaseObject import BaseObject
from Zither import Zither

class Note(BaseObject):
    def __init__(self, x, y, color):
        BaseObject.__init__(self, x, y, color)
        self.isAlive = False
        self.index = -1
    def getAlive(self):
        return self.isAlive
    def getIndex(self):
        return self.index
    def setAlive(self, alive):
        self.isAlive = alive
    def setIndex(self, index):
        self.index = index
    def setColor(self, color):
        self.color = color
        self.surface.fill(self.color)
    def update(self, dt):
        if self.isAlive:
            self.y += 0.25 * dt
            self.AABB.left = self.x
            self.AABB.top = self.y
            if (self.y >= 560):
                self.isAlive = False

class NoteManager():
    def __init__(self):
        self.Notes = []
        for count in range(0, 13):
            self.Notes.append(Note(0, 0, Color(0, 0, 0)))
    def render(self, screen):
        for note in self.Notes:
            if note.getAlive():
                note.render(screen)
    def spawn(self, x, color, index):
        for note in self.Notes:
            if not note.getAlive():
                note.setX(x)
                note.setY(0)
                note.setColor(color)
                note.setIndex(index)
                note.setAlive(True)
                return None         
    def update(self, dt, zither):
        scoreupdate = 0
        for note in self.Notes:
            note.update(dt)
            if (note.getAlive()):
                if (note.getAABB().colliderect(zither.getButton(note.getIndex()).getAABB()) and zither.getButton(note.getIndex()).getDown()):
                    scoreupdate += int(abs(note.getY() - zither.getButton(note.getIndex()).getY()))
                    note.setAlive(False)
        return scoreupdate
