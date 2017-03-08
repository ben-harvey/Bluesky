import sys
import pygame
from hot_dog import Hotdog
from random import randint
from time import sleep
from kimchi import Kimchi


def check_keydown_events(event, bs_settings, ship, stats, screen, hot_dogs, kimchis):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_q:
			sys.exit()
	elif event.key == pygame.K_p:
		start_game(bs_settings, screen, stats, ship, hot_dogs, kimchis)


def check_keyup_events(event, ship):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False



def check_events(bs_settings, screen, stats, play_button, ship, hot_dogs, kimchis):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, bs_settings, ship, stats, screen, hot_dogs, kimchis)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(bs_settings, screen, stats, play_button, ship, 
				hot_dogs, kimchis, mouse_x, mouse_y)
		
def check_play_button(bs_settings, screen, stats, play_button, ship, hot_dogs, 
	 kimchis, mouse_x, mouse_y):
	"""Start a new game when the player clicks play."""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		start_game(bs_settings, screen, stats, ship, hot_dogs, kimchis)

def start_game(bs_settings, screen, stats, ship, hot_dogs, kimchis):
		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)

		# Reset the game stats.
		stats.reset_stats()
		stats.game_active = True

		# Empty the list of aliens. 
		hot_dogs.empty()
		kimchis.empty()

		# Create new fleet and center ship.
		# create_fleet(bs_settings, screen, ship, hot_dogs)
		create_kimchi(bs_settings, screen, ship, kimchis)
		ship.center_ship()


def update_screen(bs_settings, screen, stats, ship, hot_dogs, play_button, kimchis):
	"""Update images on the screen and flip to a new screen."""	
	
	# Redraw the screen during each pass through the loop. 
	screen.fill(bs_settings.bg_color)
	ship.blitme()
	hot_dogs.draw(screen)
	kimchis.draw(screen)

	# Draw play button if game is inactive.
	if not stats.game_active:
		play_button.draw_button()

	# Make the most recently drawn screen visible. 
	pygame.display.flip()

def create_hot_dog(bs_settings, screen, hot_dogs): 
	"""Create an hot_dog and place it randomly on the screen."""
	hot_dog = Hotdog(bs_settings, screen)
	hot_dog_width = hot_dog.rect.width
	hot_dog_height = hot_dog.rect.height
	available_space_x = bs_settings.screen_width
	available_space_y = bs_settings.screen_height
	hot_dog.x = randint(0, available_space_x - hot_dog_width)
	hot_dog.y = randint(0, available_space_y - hot_dog_height)
	hot_dog.rect.x = hot_dog.x
	hot_dog.rect.y = hot_dog.y
	hot_dogs.add(hot_dog)

def instantiate_kimchi(bs_settings, screen, ship, kimchis):
	"""Create kimchi and place it in one of the four corners of the screen."""
	kimchi = Kimchi(bs_settings, screen, ship)
	kimchi_width = kimchi.rect.width
	kimchi_height = kimchi.rect.height
	kimchi_xy = return_a_corner(bs_settings, screen, kimchis)
	kimchi.x = kimchi_xy[0]
	kimchi.y = kimchi_xy[1]
	kimchi.rect.x = kimchi.x
	kimchi.rect.y = kimchi.y
	kimchis.add(kimchi)

def return_a_corner(bs_settings, screen, kimchis):
	"""Pick a random corner of the screen for generating kimchi."""
	corner = randint(1,4)
	if corner == 1:
		return (0, 0)
	if corner == 2:
		return (0, bs_settings.screen_height)
	if corner == 3:
		return (bs_settings.screen_width, 0)
	if corner == 4: 
		return (bs_settings.screen_width, bs_settings.screen_height)

# def create_fleet(bs_settings, screen, ship, hot_dogs):
# 	"""Create a full fleet of hot_dogs."""
# 	# hot_dog = Hotdog(bs_settings, screen)
# 	for hot_dog in range(randint(8,15)):	
# 		create_hot_dog(bs_settings, screen, hot_dogs) 

def create_kimchi(bs_settings, screen, ship, kimchis):
	instantiate_kimchi(bs_settings, screen, ship, kimchis)

def check_fleet_edges(bs_settings, hot_dogs):
	"""Respond if any hot dogs have reached an edge."""
	for hot_dog in hot_dogs.sprites():
		if hot_dog.check_edges():
			hot_dog.hot_dog_direction_factor *= -1
			break

def ship_hit(bs_settings, stats, screen, ship, hot_dogs):
	"""Respond to ship being hit by kimchi."""
	if stats.ships_left > 0:
		# Decrement ships left.
		stats.ships_left -= 1

		# Empty the list of aliens and bullets.
		hot_dogs.empty()
		

		# Create a new fleet and center the ship.
		create_fleet(bs_settings, screen, ship, hot_dogs)
		ship.center_ship()

		# Pause.
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def update_hot_dogs(bs_settings, hot_dogs, ship, screen):
	"""Check if dog is at screen edge, then update the position of all hot 
	dogs in the fleet."""
	check_fleet_edges(bs_settings, hot_dogs)
	
	# Check for any hot dogs that player has collided with. 
	# If so, get rid of hot dog.
	
	for hot_dog in pygame.sprite.spritecollide(ship, hot_dogs, 1):
		# pygame.mixer.Sound.play(chomp_sound)
		# pygame.mixer.Sound.stop()
		hot_dog.kill()
		
	hot_dogs.update()

def update_kimchis(bs_settings, screen, ship, kimchis):
	"""Update position of kimchi."""

	kimchis.update(ship)

