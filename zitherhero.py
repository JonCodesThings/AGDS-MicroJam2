import sys, pygame
from pygame.locals import *
from Input import Input
from Game import Game


if __name__ == "__main__":
    timer = 0
    pygame.init()
    clock = pygame.time.Clock()
    game = Game()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("zither hero")
    clock.tick()
    while (True):
        screen.fill(pygame.Color(135, 206, 235))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                sys.exit()
            if (game.input.getKeyPressed(K_ESCAPE)):
                pygame.display.quit()
                sys.exit()
        game.update(clock.get_time())
        game.render(screen)
        pygame.display.update()
        clock.tick()
