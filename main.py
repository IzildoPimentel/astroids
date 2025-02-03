# import the pygame library
import pygame
from constants import *
from player import Player

def main():
    
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    game_mode = True

    clock = pygame.time.Clock() 
    dt = 0

    # Instantiate the Player object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Create sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Add the player to the sprite groups
    updatable.add(player)
    drawable.add(player)

    while game_mode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_mode = False
            
        dt = clock.tick(60) / 1000  

        # Clear the screen
        screen.fill((0, 0, 0)) 

        # Update and draw the player
        updatable.update(dt)
        drawable.draw(screen)

        # Update the display   
        pygame.display.flip()  

    pygame.quit()

if __name__ == "__main__":
    main()