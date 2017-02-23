import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	bs_settings = Settings()
	screen = pygame.display.set_mode(
		(bs_settings.screen_width, bs_settings.screen_height))
	pygame.display.set_caption("Blue Sky")

	# Make a ship.
	ship = Ship(bs_settings, screen)
	# Make a group to store bullets into. 
	#bullets = Group()

	# Start the main loop for the game. 
	while True: 
		gf.check_events(ship) #bullets)	
		ship.update()
		#gf.update_bullets(bullets)	
		gf.update_screen(bs_settings, screen, ship) # bullets)


run_game()