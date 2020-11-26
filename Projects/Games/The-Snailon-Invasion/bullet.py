import pygame
from pygame.sprite import Sprite

class Bullet(Sprite): # sprite module give the option to group related arguments and act on all the grouped elements at once
    """class that managed bullets that fired from the ship"""
    def __init__(self,ai_settings,screen,ship):
        """create a bullet object at the ship's current position"""
        super(Bullet, self).__init__()
        self.screen = screen

        # create a bullet rect at (0,0) and giving him width and height
        self.rect = pygame.Rect(0 , 0, ai_settings.bullet_width , ai_settings.bullet_height)

        """POSITIONING THE BULLET"""
        self.rect.centerx = ship.rect.centerx # bullet center == ship center
        self.rect.top = ship.rect.top # bullet top == ship top
        # bullet center and top == ship center and top so it will look like the ship shooting it

        self.y = float(self.rect.y) # Store the bullet's position as a decimal value

        self.color = ai_settings.bullet_color # bullet color
        self.speed_factor = ai_settings.bullet_speed_factor # bullet speed

    def update(self):
        """move the bullet up the screen"""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor # as the bullet move up the y position is decreased
        # Update the rect position == float(y) position.
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)