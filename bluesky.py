import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from hot_dog import Hotdog

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	bs_settings = Settings()
	screen = pygame.display.set_mode(
		(bs_settings.screen_width, bs_settings.screen_height))
	pygame.display.set_caption("Blue Sky")

	# Make a ship, a group of bullets, and a group of hot_dogs.
	ship = Ship(bs_settings, screen)
	bullets = Group()
	hot_dogs = Group()

	# Create the fleet of hot_dogs.
	gf.create_fleet(bs_settings, screen, ship, hot_dogs)

	# Start the mbsn loop for the game. 
	while True: 
		gf.check_events(bs_settings, screen, ship, bullets)		
		ship.update()
		gf.update_bullets(bullets)
		gf.update_screen(bs_settings, screen, ship, hot_dogs, bullets)



run_game()