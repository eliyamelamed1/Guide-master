import pygame
from pygame.sprite import Sprite

class Alien(Sprite): # sprite module give the option to group related arguments and act on all the grouped elements at once
    """A class to represent a single alien in the fleet"""

    def __init__(self,ai_Settings,screen):
        """Initialize the alien and set its starting position."""
        super(Alien, self).__init__() # inheritance
        self.screen = screen
        self.ai_settings = ai_Settings

        # Load the alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.image = pygame.transform.scale(self.image, (100, 80 ))  # Adjust alien size
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen. (play with the numbers)
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien exact position
        self.x = float(self.rect.x)

    def blitme(self):
        # Draw the alien at its current location
        self.screen.blit(self.image,self.rect)

    def check_edges(self):
        """Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        # Alien is at the right edge
        # if his rect.right atrribute is greater or equal the the screen_rect.right
        if self.rect.right >= screen_rect.right:
            return True
        # Alien is at the left edge
        # if his rect.left atrribute is greater or equal to 0 (left edge of the screen)
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien right or left"""
        # alien_speed_factor = 1 * fleet_direction 1 right / -1 left
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x
