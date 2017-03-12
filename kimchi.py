import pygame
from pygame.sprite import Sprite
import random
import math

class Kimchi(pygame.sprite.Sprite):
	"""A class to represent kimchi."""

	def __init__(self, bs_settings, screen, ship):
		"""Initialize the kimchi and set its starting position."""
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.bs_settings = bs_settings
		self.ship = ship

		# Load the kimchi image and set its rect attribute.
		self.image = pygame.image.load('images/kimchi_t.png')
		self.rect = self.image.get_rect()
		

		# Store the kimchi's exact position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		

	def blitme(self):
		"""Draw the kimchi at its current location."""
		self.screen.blit(self.image, self.rect)

	# def check_edges(self):
	# 	"""Return True if kimchi is at edge of screen."""
	# 	screen_rect = self.screen.get_rect()
	# 	if self.rect.right >= screen_rect.right:
	# 		return True
	# 	elif self.rect.left <= 0:
	# 		return True
	# 	elif self.rect.top <= 0:
	# 		return True
	# 	elif self.rect.bottom >= screen_rect.bottom:
	# 		return True


	def update(self):  #ship
		"""Make kimchi chase the player."""

		# find normalized direction vector (dx, dy) between enemy and player
		dx, dy = self.rect.x - self.ship.rect.x, self.rect.y - self.ship.rect.y
		
		dist = math.hypot(dx, dy)
		dx, dy = (dx / dist) * -2, (dy / dist) * -2
		
		# move along this normalized vector towards the player at current speed
		self.rect.x += dx * self.bs_settings.kimchi_speed_factor
		self.rect.y += dy * self.bs_settings.kimchi_speed_factor
		