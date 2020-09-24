import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init() # required for pygame
    ai_settings = Settings() # variable for setting class

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height)) # screen size
    pygame.display.set_caption("THE snailon invasion")
    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings,screen) # varibale for Ship class
    bullets = Group()
    aliens = Group()

    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen,ship, aliens,bullets)

    # Create an instance to store game statistics and create a scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make the Play Button.
    play_button = Button(ai_settings, screen, "Play")

    while True: # Start the main loop for the game.
        gf.check_events(ai_settings, screen, ship,stats,play_button, bullets,sb) # Watch for keyboard and mouse events.

        if stats.game_active:
            ship.update()
            gf.update_bullets(sb,stats,ai_settings, screen, ship, aliens,bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets,sb)

        gf.update_screen(sb,ai_settings, screen,stats , ship, aliens, bullets, play_button) # update: the whole game


run_game()