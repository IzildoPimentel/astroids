# import the pygame library
import pygame
from constants import *


def main():
    pygame.get_init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_mode = True

    while game_mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_mode = False
            
    pygame.quit()

if __name__ == "__main__":
    main()