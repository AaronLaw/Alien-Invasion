import sys
import pygame
from bullet import Bullet
from alien import Alien
from time import sleep

def check_events(ai_settings, screen, ship, bullets):
    """Respond to keypresses and mouse events."""
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        
        print(event)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key==pygame.K_q:
        sys.exit()

def check_keyup_events(event, ship):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def update_screen(ai_settings, screen, ship, alien, bullets):
    """Update images on the screen and flip to the new screen."""
    screen.fill(ai_settings.bg_color)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    #alien.blitme()
    alien.draw(screen)

    # Make the monst recently drawn screen visible.
    pygame.display.flip()

def update_bullets(ai_settings, screen, bullets, aliens):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    print('Bullets: %s' % len(bullets))

    check_bullet_alien_collisions(ai_settings, screen, bullets, aliens)
    repopulate_aliens(ai_settings, screen, bullets, aliens)

def check_bullet_alien_collisions(ai_settings, screen, bullets, aliens):
    # Check for any bullets that have hit aliens.
    # If so, get rid of the bullet and the alien that havecollided.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

def repopulate_aliens(ai_settings, screen, bullets, aliens):
    # Consider if we need to repopulate the fleet once it has been destroyed.
    # One key feature of Alien Invasion is that the alien are relentless: everytime the fleet is destroyed, a new fleet should appear.
    if len(aliens) == 0:
        bullets.empty()
        create_fleet(ai_settings, screen, aliens)

def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) <= ai_settings.bullet_allowed:
        bullet = Bullet(ai_settings, screen, ship)
        bullets.add(bullet)

def create_fleet(ai_settings, screen, aliens):
    """Create a full fleet of aliens."""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, screen, alien.rect.width)
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number)

    # Create the first row of aliens.
    
def get_number_aliens_x(ai_settings, screen, alien_width):
    """Determint the number of aliens that fit in row."""
    available_space_x = ai_settings.screen_width - 2*alien_width
    number_aliens_x = int(available_space_x / (2*alien_width))
    return number_aliens_x

def create_alien(ai_settings, screen, aliens, alien_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2*alien_width*alien_number
    alien.rect.x = alien.x
    aliens.add(alien)

def update_aliens(ai_settings, stats, screen, aliens, ship, bullets):
    """Check if the fleet is at an edge,
    and then update the positions of all aliens in the fleet."""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, aliens):
        print("Ship hit!!!")
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        stats.ships_left -= 1
        aliens.empty()
        bullets.empty()
        create_fleet(ai_settings, screen, aliens)
        ship.center_ship()
        sleep(0.5)
    else:
        stats.game_active = False

def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """Check if an alien have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
 
def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.is_hit_edges():
            change_fleet_directions(ai_settings, aliens)
            break

def change_fleet_directions(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1
