import pygame

from circleshape import CircleShape
from constants import *

class Player(CircleShape, pygame.sprite.Sprite):
    def __init__(self, x, y):
        CircleShape.__init__(self, x, y, PLAYER_RADIUS)
        pygame.sprite.Sprite.__init__(self)

        # Create a surface for the sprite
        size = int(PLAYER_RADIUS * 2)  # or even slightly smaller
        self.image = pygame.Surface((size, size))
        # Set black as the transparent color
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect(center=(x, y))
        self.rotation = 0
        self.triangle()  # Draw the initial triangle

    # in the player class
    def triangle(self):
        # Clear the image surface
        self.image.fill((0, 0, 0, 0))
        
        # Convert the triangle points to be relative to the image surface
        center = pygame.Vector2(self.rect.width / 2, self.rect.height / 2)
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 2

        # Calculate points relative to surface center
        a = center + forward * (self.radius / 1.2)
        b = center - forward * (self.radius / 1.2) - right
        c = center - forward * (self.radius / 1.2) + right

        # Draw onto the image surface
        pygame.draw.polygon(self.image, (255, 255, 255), [a, b, c], 2)    

    def rotate(self, angle, dt):
        # Use the angle parameter instead of PLAYER_TURN_SPEED
        self.rotation += angle * dt
        self.triangle()  # Redraw triangle after rotation

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(PLAYER_TURN_SPEED, -dt)
        if keys[pygame.K_d]:
            self.rotate(PLAYER_TURN_SPEED, dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, -1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
        # Update the rect position to match the new position
        self.rect.center = self.position