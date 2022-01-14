import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self,ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__() #
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/salt_shaker.bmp') # salt IMAGE
        self.image = pygame.transform.scale(self.image, (80, 100)) # adjust ship size
        self.rect = self.image.get_rect() # the ship attribute as a rectangles
        self.screen_rect = screen.get_rect() # variable for screen dimensions
        # Ship start location
        self.rect.centerx = self.screen_rect.centerx # ship is at the middle of the screen length
        self.rect.bottom = self.screen_rect.bottom # ship is at the bottom of the screen

        self.moving_right = False  # Movement flag
        self.moving_left = False   # Movement flag

        # adjusting speed
        self.speed = self.ai_settings.ship_speed_factor
        # Store a decimal value for the ship's center.
        self.center = float(self.rect.centerx)

    def update(self):
        """Update the ship's position based on the movement flag."""
        # if the right key is pressed AND the ship right side is in the boundries of the screen
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.speed
        # if the left key is pressed AND the ship left side is in the boundries of the screen
        if self.moving_left and self.rect.left > 0:
            self.center -= self.speed

        # Update rect object from self.center.
        self.rect.centerx = self.center


    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect) #.blit takes 2 arguments (image ,p osition)

    def center_ship(self):
        """Center the ship on the screen."""
        self.center = self.screen_rect.centerx