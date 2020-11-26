import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def update_screen(sb,ai_settings, screen,stats, ship,aliens,bullets, play_button):
    """Update images on the screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.fill(ai_settings.bg_color)

    # Redraw all bullets behind ship and aliens.
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # Drawing
    ship.blitme() # drawing the ship
    aliens.draw(screen) # while in Group() the command .draw() automatically draws each element from the group at his defined position

    # Draw the score information
    sb.prep_score()
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()


    # Make the most recently drawn screen visible.
    pygame.display.flip()

"""KEYS"""
# if the close button is pressed close the game
def check_events(ai_settings, screen, ship,stats,play_button, bullets,sb):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos() # Return the mouse X & Y coordinates
            check_play_button(stats, play_button, mouse_x, mouse_y,ai_settings,sb)

def check_play_button(stats, play_button,mouse_x, mouse_y,ai_settings,sb):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active: # If the game INACTIVE and the play button pressed
        stats.count += 1
        # Reset the game statistics.
        stats.reset_stats()

        if stats.count > 1: # BUG FIX
            stats.ships_left = ai_settings.ship_limit + 1

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)
        # Start the game
        stats.game_active = True
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

def check_keydown_events(event,ai_settings,screen ,ship,bullets):
    """respond to keys pressed"""
    if event.type == pygame.KEYDOWN: # if key is pressed

        if event.key == pygame.K_q:
            sys.exit()

        # ship movements
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True # ship move right
        if event.key == pygame.K_LEFT:
            ship.moving_left = True # ship move left

        # adjust ship speed
        if event.key == pygame.K_UP:
            if ship.speed != 2.5:
                ship.speed += 0.25
        if event.key == pygame.K_DOWN:
            if ship.speed != 0.5:
                ship.speed -= 0.25

        if event.key == pygame.K_SPACE:
            fire_bullets(ai_settings,screen,ship,bullets)

def check_keyup_events(event, ship):
    """respong to keys released"""
    if event.type == pygame.KEYUP: # if key is released
        if event.key == pygame.K_RIGHT:
            # the ship stop moving
            ship.moving_right = False
        if event.key == pygame.K_LEFT:
            ship.moving_left = False

"""BULLETS"""
def fire_bullets(ai_settings,screen,ship,bullets):
    """fire a bullet if limit not reached yet."""
    if len(bullets) < ai_settings.bullets_allowed:
    # Create a new bullet and add it to the bullets group.
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_bullets(sb,stats,ai_settings, screen, ship, aliens, bullets):
    """Update position of bullets and get rid of old bullets."""
    # update bullet positions
    bullets.update()

    # get rid of bullets that have disappeared
    for bullet in bullets.copy():  # we use .copy because bullets is Group object which is not callable
        if bullet.rect.bottom <= 0:  # check if bullet have disappeared from the screen
            bullets.remove(bullet)  # remove bullet

    # Check for alien & bullet collisions
    check_bullet_alien_collisions(sb,stats,ai_settings, screen, ship, aliens, bullets)

def check_bullet_alien_collisions(sb,stats,ai_settings, screen, ship, aliens, bullets):
    """RESPOND TO ALIEN & BULLET COLLISIONS"""
    # Check for any bullets that have hit aliens.
    # Remove and bullets and aliens that have collided
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score
            check_high_score(stats, sb)

    """Repopulating the Fleet"""
    if len(aliens) == 0:
        # Destroy existing bullets, speed up game, and create new fleet
        bullets.empty()
        ai_settings.increase_speed()
        stats.level += 1 # Increase level by 1
        sb.prep_level() # Prepare level img

        create_fleet(ai_settings,screen,ship,aliens,bullets)

"""ALIENS"""
def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - 2 * alien_width # Horizontal space available - 2 aliens (we want 2 empty alien slots [1 at each side] )
    number_aliens_x = int(available_space_x / (2 * alien_width)) # Between each alien there should be one alien empty slot + we use int so we wont end up with partial aliens (rect only take int arguments)
    return number_aliens_x # Number of aliens that fits in a Line

def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - 2 * alien_height - ship_height) # Vertical space available - 2 aliens - ship (we want 2 empty alien slots between the fleet and the ship)
    number_rows = int(available_space_y / (2 * alien_height)) # Between each alien there should be one alien empty slot + we use int so we wont end up with partial aliens (rect only take int arguments)
    return number_rows # Number of aliens that fits in a Row

def create_alien(ai_settings,screen,aliens,alien_number,row_number):
    """Create an alien and place it in the row"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number  # Each alien is pushed to the right side of the alien before him
    alien.rect.x = alien.x # CHECK
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number # Each alien is placed beneath an alien while keeping a space (of an alien) between each alien
    aliens.add(alien)  # Adding the alien to the group

def create_fleet(ai_settings, screen,ship, aliens,bullets):
    """Create a full fleet of aliens."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width) # Call the get_number_aliens_x to determine how many aliens in a line
    number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height) # Call the get_number_rows to determine how many aliens in a row

    # Create the first row of aliens.
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            # Create an alien and place it in the row.
            create_alien(ai_settings, screen, aliens, alien_number,row_number) # Call the create_alien function

def check_fleet_egdes(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break

def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

"""Respond to ship being hit by alien."""
def ship_hit(ai_settings, stats, screen, ship, aliens, bullets,sb):
    # IF there is any ship left (LIVES)
    if stats.ships_left > 1:

        # Decrement ships_left.
        stats.ships_left -= 1

        # Empty the list of aliens and bullets.
        aliens.empty()
        bullets.empty()

        # Create a new fleet and center the ship.
        create_fleet(ai_settings, screen, ship, aliens,bullets)
        ship.center_ship()

        # Update ships left in scoreboard
        sb.prep_ships()

        # Pause.
        sleep(0.5)


    else:
        # IF there is no ships left (LIVES)
        # Close the game
        stats.game_active = False
        # Mouse is visible
        pygame.mouse.set_visible(True)


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets,sb):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets,sb)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets,sb):
    """
    Check if the fleet is at an edge.
    and then Update the positions of all aliens in the fleet
    """
    check_fleet_egdes(ai_settings, aliens)
    aliens.update()

    """DETECTING ALIEN & SHIP COLLISIONS"""
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets,sb)


    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets,sb)

def check_high_score(stats,sb):
    """Check to see if there's a new high score"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()