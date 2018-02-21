from Input import Input
from Note import Note, NoteManager
from Zither import Zither
import pygame, random
from pygame.locals import *

class Game():
    def __init__(self):
        random.seed()
        self.input = Input()
        self.notemanager = NoteManager()
        self.zither = Zither()
    def render(self, screen):
        self.zither.render(screen)
        self.notemanager.render(screen)
    def update(self, dt):
        self.input.update()
        self.zither.update(dt, self.input)
        self.notemanager.update(dt)
