import sys
from bullet import Bullet
import pygame

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
		elif event.type ==pygame.KEYDOWN:
			check_keydown_events(event, bs_settings, ship, screen, bullets)
		elif event.type ==pygame.KEYUP:
			check_keyup_events(event, ship)
		
		
		
def update_screen(bs_settings, screen, ship, bullets):
	"""Update images on the screen and flip to a new screen."""	
	
	# Redraw the screen during each pass through the loop. 
	screen.fill(bs_settings.bg_color)
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	ship.blitme()

	# Make the most recently drawn screen visible. 
	pygame.display.flip()

def update_bullets(bullets):
	"""Update position of bullets and get rid of old bullets."""
	#  Update bullet position.
	bullets.update()

	# Get rid of bullets that have left the screen.
	for bullet in bullets.copy():
		if bullet.rect.bottom <= 0:
			bullets.remove(bullet)
