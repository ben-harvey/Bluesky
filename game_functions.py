import sys
from bullet import Bullet
import pygame
from hot_dog import Hotdog
from random import randint


def check_keydown_events(event, bs_settings, ship, screen, bullets):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True
	elif event.key == pygame.K_SPACE:
		fire_bullet(bs_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
			sys.exit()

def fire_bullet(bs_settings, screen, ship, bullets):
	"""Fire bullet if limit not reached yet."""
	# Create a new bullet and add to bullets group. 
	if len(bullets) < bs_settings.bullets_allowed:
		new_bullet = Bullet(bs_settings, screen, ship)
		bullets.add(new_bullet)


def check_keyup_events(event, ship):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False



def check_events(bs_settings, screen, ship, bullets):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			check_keydown_events(event, bs_settings, ship, screen, bullets)
		elif event.type == pygame.KEYUP:
			check_keyup_events(event, ship)
		
		
		
def update_screen(bs_settings, screen, ship, hot_dogs, bullets):
	"""Update images on the screen and flip to a new screen."""	
	
	# Redraw the screen during each pass through the loop. 
	screen.fill(bs_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()
	hot_dogs.draw(screen)

	# Make the most recently drawn screen visible. 
	pygame.display.flip()

def update_bullets(bullets):
	"""Update position of bullets and get rid of old bullets."""
	# Update bullet positions.
	bullets.update()

	# Get rid of bullets that have left the screen.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)

def get_number_hot_dogs_x(bs_settings, hot_dog_width):
	"""Determine the number of hot_dogs that fit in a row."""
	
	number_hot_dogs_x = randint(1,4)
	return number_hot_dogs_x

def get_number_rows(bs_settings, ship_height, hot_dog_height):
	"""Determine the number of rows of hot_dogs that fit on the screen."""
	available_space_y = (bs_settings.screen_height -
							(2 * hot_dog_height) - ship_height)
	number_rows = int(available_space_y / (2 * hot_dog_height))
	return number_rows


def create_hot_dog(bs_settings, screen, hot_dogs, hot_dog_number, row_number):
	"""Create an hot_dog and place it in a row."""
	hot_dog = Hotdog(bs_settings, screen)
	hot_dog_width = hot_dog.rect.width
	available_space_x = bs_settings.screen_width
	hot_dog.x = randint(0, available_space_x)
	hot_dog.rect.x = hot_dog.x
	hot_dog.rect.y = hot_dog.rect.height + 3 * hot_dog.rect.height * row_number
	hot_dogs.add(hot_dog)

def create_fleet(bs_settings, screen, ship, hot_dogs):
	"""Create a full fleet of hot_dogs."""
	# Create an hot_dog and find the number of hot_dogs in a row.
	hot_dog = Hotdog(bs_settings, screen)
	number_hot_dogs_x = get_number_hot_dogs_x(bs_settings, hot_dog.rect.width)
	number_rows = get_number_rows(bs_settings, ship.rect.height, 
		hot_dog.rect.height)
	
	# Create the fleet of hot_dogs. 
	for row_number in range(number_rows):
		for hot_dog_number in range(number_hot_dogs_x):
			create_hot_dog(bs_settings, screen, hot_dogs, hot_dog_number, 
				row_number)
		