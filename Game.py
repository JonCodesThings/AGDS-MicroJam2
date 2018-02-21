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
        self.timer = 0
        self.font = pygame.font.Font(None, 64)
        self.score = 0
    def render(self, screen):
        score_ = self.font.render("Score: " + str(self.score), 0, pygame.Color(255, 255, 255))
        screen.blit(score_, (0, 0))
        self.zither.render(screen)
        self.notemanager.render(screen)
    def update(self, dt):
        self.timer += dt
        if (self.timer >= 1000):
            random_ = random.randint(0, 10)
            if (random_ < 7):
                button = self.zither.getBigButton(random_)
            else:
                button = self.zither.getSmallButton(random_)
            self.notemanager.spawn(button.getX(), button.getColor(), random_)
            self.timer = 0
        self.input.update()
        self.zither.update(dt, self.input)
        self.score += self.notemanager.update(dt, self.zither)
