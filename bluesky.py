import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
from hot_dog import Hotdog
from game_stats import GameStats
from button import Button
from kimchi import Kimchi

def run_game():
	# Initialize pygame, settings, and screen object.
	pygame.init()
	# pygame.mixer.pre_init(44100, -16, 2, 2048)
	bs_settings = Settings()
	screen = pygame.display.set_mode(
		(bs_settings.screen_width, bs_settings.screen_height))
	pygame.display.set_caption("Blue Sky")

	# Make the Play button
	play_button = Button(bs_settings, screen, 'Play')

	# Create an instance to store stats.
	stats = GameStats(bs_settings)

	# Make a ship, a group of bullets, and a group of hot_dogs.
	ship = Ship(bs_settings, screen)
	hot_dogs = Group()
	kimchis = Kimchi(bs_settings, screen, ship)

	# Create the fleet of hot_dogs.
	gf.create_fleet(bs_settings, screen, ship, hot_dogs)

	# Create kimchi. 

	gf.create_kimchi(bs_settings, screen, ship, kimchis)


	# Start the main loop for the game. 
	while True: 
		gf.check_events(bs_settings, screen, stats, play_button, ship, hot_dogs, kimchis)		
		
		if stats.game_active:	
			ship.update()
			gf.update_hot_dogs(bs_settings, hot_dogs, ship, screen)
			gf.update_kimchis(bs_settings, kimchis, ship, screen)
		
		gf.update_screen(bs_settings, screen, stats, ship, hot_dogs, play_button, kimchis)


run_game()