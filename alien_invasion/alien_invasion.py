import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
import game_functions as gf
from game_stats import GameStats
from button import Button

def run_game():
    
    # Initialize pygame, settings and screen object
    pygame.init()
    main_settings = Settings()
    screen = pygame.display.set_mode((main_settings.screen_width, main_settings.screen_height))
    pygame.display.set_caption("Alien Invasion - Charlie edition")
    
    # Create play button
    play_button = Button(main_settings, screen, "Play")
    
    # Create an instance to store game statistics.
    stats = GameStats(main_settings)
    
    # Make a Ship, a group of aliens and a gropu of bullets.
    ship = Ship(screen, main_settings)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens
    gf.create_fleet(main_settings, screen, ship, aliens)
    
    # Star the main loop for the game
    while True:
        
        # Check for the events happening 
        gf.check_events(main_settings, screen, stats, play_button, ship,aliens, bullets)
        if stats.game_active:
            # Update ship position
            ship.update()
            # Update bullets
            gf.update_bullets(main_settings, screen, ship, aliens, bullets)
            # Update aliens
            gf.update_aliens(main_settings, stats, screen, ship, aliens, bullets)
        # Update screen - it paints the screen
        gf.update_screen(main_settings, screen, stats, ship, aliens, bullets, play_button)
    
run_game()