import sys
import pygame
from hot_dog import Hotdog
from random import randint
from time import sleep
from kimchi import Kimchi


def check_keydown_events(event, bs_settings, ship, stats, screen, sb, hot_dogs, kimchis):

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
		start_game(bs_settings, screen, stats, ship, sb, hot_dogs, kimchis)


def check_keyup_events(event, ship):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False



def check_events(bs_settings, screen, stats, play_button, ship, sb, hot_dogs, kimchis):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, bs_settings, ship, stats, screen, sb, hot_dogs, kimchis)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos()
			check_play_button(bs_settings, screen, stats, play_button, sb, ship, 
				hot_dogs, kimchis, mouse_x, mouse_y)
		
def check_play_button(bs_settings, screen, stats, play_button, ship, sb, hot_dogs, 
	 kimchis, mouse_x, mouse_y):
	"""Start a new game when the player clicks play."""
	button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
	if button_clicked and not stats.game_active:
		bs_settings.initialize_dynamic_settings()
		start_game(bs_settings, screen, stats, ship, hot_dogs, kimchis)

def start_game(bs_settings, screen, stats, ship, sb, hot_dogs, kimchis):
		# Hide the mouse cursor.
		pygame.mouse.set_visible(False)

		# Reset the game stats.
		stats.reset_stats()
		stats.game_active = True

		# Empty the list of aliens. 
		hot_dogs.empty()
		kimchis.empty()

		# Create new fleet and center ship.
		create_hot_dog_fleet(bs_settings, screen, ship, hot_dogs)
		create_kimchi_fleet(bs_settings, screen, stats, ship, kimchis)
		ship.center_ship()
		
		# Play music
		pygame.mixer.music.load('vivaldi.wav')
		pygame.mixer.music.play(-1)

		# Create random background color. 
		bs_settings.random_bg()

		# Reset scoreboard
		sb.prep_score()
		sb.prep_high_score()
		sb.prep_level()
		#sb.prep_ships()

def update_screen(bs_settings, screen, stats, sb, ship, hot_dogs, play_button, kimchis):
	"""Update images on the screen and flip to a new screen."""	
	
	# Redraw the screen during each pass through the loop. 
	screen.fill(bs_settings.bg_color)
	ship.blitme()
	hot_dogs.draw(screen)
	kimchis.draw(screen)
	# Draw the score info.
	sb.show_score()

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

def create_kimchi(bs_settings, screen, stats, ship, kimchis):
	"""Create kimchi and place it in one of the four corners of the screen."""
	if stats.game_active:
		kimchi = Kimchi(bs_settings, screen, ship)
		kimchi_width = kimchi.rect.width
		kimchi_height = kimchi.rect.height
		kimchi_xy = return_a_corner(bs_settings, screen, ship, kimchis)
		kimchi.x = kimchi_xy[0]
		kimchi.y = kimchi_xy[1]
		kimchi.rect.x = kimchi.x
		kimchi.rect.y = kimchi.y
		kimchis.add(kimchi)

def return_a_corner(bs_settings, screen, ship, kimchis):
	"""Pick a random corner of the screen for generating kimchi."""
	kimchi = Kimchi(bs_settings, screen, ship)
	kimchi_width = kimchi.rect.width
	kimchi_height = kimchi.rect.height
	corner = randint(1,4)
	if corner == 1:
		return (0, 0)
	if corner == 2:
		return (0, bs_settings.screen_height - kimchi_height)
	if corner == 3:
		return (bs_settings.screen_width - kimchi_width, 0)
	if corner == 4: 
		return (bs_settings.screen_width - kimchi_width, bs_settings.screen_height - kimchi_height)

def create_hot_dog_fleet(bs_settings, screen, ship, hot_dogs):
	"""Create a full fleet of hot_dogs."""
	for hot_dog in range(randint(8,15)):	
		create_hot_dog(bs_settings, screen, hot_dogs) 

def create_kimchi_fleet(bs_settings, screen, stats, ship, kimchis):
	"""Create a full fleet of kimchi."""
	kimchi = Kimchi(bs_settings, screen, ship)
	for kimchi in range(bs_settings.kimchi_number):	
		create_kimchi(bs_settings, screen, stats, ship, kimchis) 

def check_fleet_edges(bs_settings, hot_dogs):
	"""Respond if any hot dogs have reached an edge."""
	for hot_dog in hot_dogs.sprites():
		if hot_dog.check_edges():
			hot_dog.hot_dog_direction_factor *= -1
			break

def check_ship_kimchi_collisions(bs_settings, screen, stats, sb, ship,
	 kimchis, hot_dogs):
	"""Respond to kimchi-ship collisions."""
	collisions = pygame.sprite.spritecollide(ship, kimchis, 1)
	if collisions:
		play_scream(bs_settings, screen, stats, sb, ship,
	 		kimchis, hot_dogs)
		ship_hit(bs_settings, stats, screen, ship, kimchis, hot_dogs)


		


def ship_hit(bs_settings, stats, screen, ship, kimchis, hot_dogs):
	"""Respond to ship being hit by kimchi."""
	if stats.ships_left > 0:
		# Decrement ships left.
		stats.ships_left -= 1

		# Empty the list of aliens and bullets.
		hot_dogs.empty()
		kimchis.empty()
		
		# Create a new fleet and center the ship.
		create_hot_dog_fleet(bs_settings, screen, ship, hot_dogs)
		create_kimchi_fleet(bs_settings, screen, stats, ship, kimchis)
		ship.center_ship()

		# Create random background color. 
		bs_settings.random_bg()
		
		# Pause.
		sleep(0.5)
	else:
		stats.game_active = False
		pygame.mouse.set_visible(True)

def update_hot_dogs(bs_settings, screen, stats, sb, ship, hot_dogs, kimchis):
	"""Check if dog is at screen edge, then update the position of all hot 
	dogs in the fleet."""
	check_fleet_edges(bs_settings, hot_dogs)
	
	# Check for ship-hot dog collisions.
	check_ship_hot_dog_collisions(bs_settings, screen, stats, sb, ship,
	 hot_dogs)

	# Check for any hot dogs that player has collided with. 
	# If so, get rid of hot dog.
	
	for hot_dog in pygame.sprite.spritecollide(ship, hot_dogs, 1):
		
		hot_dog.kill()
	
	if len(hot_dogs) == 0:
		# Destroy kimchis, speed up game, and create new fleet.
		kimchis.empty()
		bs_settings.increase_speed()
		create_hot_dog_fleet(bs_settings, screen, ship, hot_dogs)
		create_kimchi_fleet(bs_settings, screen, stats, ship, kimchis)	

		# Increase level
		stats.level += 1 
		sb.prep_level()

		# Create random background color. 
		bs_settings.random_bg()

	hot_dogs.update()

def update_kimchis(bs_settings, screen, stats, sb, ship, kimchis, hot_dogs):
	"""Update the position of all kimchi
	in the fleet"""
	check_ship_kimchi_collisions(bs_settings, screen, stats, sb, ship,
	 kimchis, hot_dogs)

	kimchis.update()

def play_chomp(bs_settings, screen, stats, sb, ship,
	 hot_dogs):
	"""Play chomp sound."""
	if stats.game_active:
		chomp_sound = pygame.mixer.Sound('chomp.wav')
		chomp_sound.play()

def play_scream(bs_settings, screen, stats, sb, ship,
	 kimchis, hot_dogs):
	"""Play chomp sound."""
	if stats.game_active:
		scream_sound = pygame.mixer.Sound('scream.wav')
		scream_sound.play()


def check_ship_hot_dog_collisions(bs_settings, screen, stats, sb, ship,
	 hot_dogs):
	"""Respond to hot_dog-ship collisions."""
	collisions = pygame.sprite.spritecollide(ship, hot_dogs, 1)
	if collisions:
		play_chomp(bs_settings, screen, stats, sb, ship,
	 hot_dogs)
		for hot_dogs in collisions:
			stats.score += bs_settings.hot_dog_points 
			sb.prep_score()
		check_high_score(stats, sb)


def check_high_score(stats, sb):
	"""Check to see if there's a new high score."""
	if stats.score > stats.high_score:
		stats.high_score = stats.score
		sb.prep_high_score()
	

