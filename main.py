# import the pygame library
import pygame
from constants import *

def main():
    from player import Player

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_mode = True

    clock = pygame.time.Clock() 
    dt = 0

    # Instantiate the Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while game_mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_mode = False
            
        dt = clock.tick(60) / 1000  

        player.update(dt)

        screen.fill((0, 0, 0))  
        player.draw(screen)
        pygame.display.flip()  

    pygame.quit()

if __name__ == "__main__":
    main()