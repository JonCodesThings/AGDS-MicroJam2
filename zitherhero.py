import sys, pygame
from pygame.locals import *
from Input import Input
from Zither import Zither


if __name__ == "__main__":
    timer = 0
    pygame.init()
    clock = pygame.time.Clock()
    input_ = Input()
    zither = Zither()
    screen = pygame.display.set_mode((800, 600))
    clock.tick()
    while (True):
        screen.fill(pygame.Color(135, 206, 235))
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.display.quit()
                sys.exit()
            input_.update()
            if (input_.getKeyPressed(K_ESCAPE)):
                pygame.display.quit()
                sys.exit()
        zither.update(clock.get_time(), input_)
        zither.render(screen)
        pygame.display.update()
        clock.tick()
