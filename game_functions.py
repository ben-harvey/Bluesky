import sys

import pygame

def check_keydown_events(event, ship):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_UP:
		ship.moving_up = True
	elif event.key == pygame.K_DOWN:
		ship.moving_down = True


def check_keyup_events(event, ship):

	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT:
		ship.moving_left = False
	elif event.key == pygame.K_UP:
		ship.moving_up = False
	elif event.key == pygame.K_DOWN:
		ship.moving_down = False

def check_events(ship):
	"""Respond to keypresses and mouse events."""
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type ==pygame.KEYDOWN:
			check_keydown_events(event, ship)
		elif event.type ==pygame.KEYUP:
			check_keyup_events(event, ship)
		
		
		
def update_screen(bs_settings, screen, ship):
	"""Update images on the screen and flip to a new screen."""	
	
	# Redraw the screen during each pass through the loop. 
	screen.fill(bs_settings.bg_color)
	ship.blitme()

	# Make the most recently drawn screen visible. 
	pygame.display.flip()

