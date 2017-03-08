import pygame
from pygame.sprite import Sprite
import random
import math
# from ship import Ship

class Kimchi(pygame.sprite.Sprite):
	"""A class to represent kimchi."""

	def __init__(self, bs_settings, screen, ship):
		"""Initialize the kimchi and set its starting position."""
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.bs_settings = bs_settings
		self.ship = ship

		# Load the kimchi image and set its rect attribute.
		self.image = pygame.image.load('images/kimchi.bmp')
		self.rect = self.image.get_rect()
		

		# Store the kimchi's exact position.
		self.x = float(self.rect.x)
		

		# # Store and randomize the kimchi's direction.
		# self.kimchi_direction_factor = 1
		# numbers =  [x for x in range(-4, 4) if x != 0]
		# self.direction = random.choice(numbers)
		# print(self.direction)

	def blitme(self):
		"""Draw the kimchi at its current location."""
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		"""Return True if kimchi is at edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
		elif self.rect.top <= 0:
			return True
		elif self.rect.bottom >= screen_rect.bottom:
			return True


	def update(self, ship):
		"""Make kimchi chase the player."""
		
		# find normalized direction vector (dx, dy) between enemy and player
		dx, dy = self.rect.x - self.ship.rect.x, self.rect.y - self.ship.rect.y
		dist = math.hypot(dx, dy)
		dx, dy = dx / dist, dy / dist
		# move along this normalized vector towards the player at current speed
		self.rect.x += dx * self.bs_settings.kimchi_speed_factor
		self.rect.y += dy * self.bs_settings.kimchi_speed_factor




		# self.speed = self.bs_settings.kimchi_speed_factor 
		# self.direction_factor = self.kimchi_direction_factor
		
		# if self.direction == -4:
		# 	self.y += (1 * self.speed * self.direction_factor) 
		# elif self.direction == -3:
		# 	self.y -= (1 * self.speed * self.direction_factor)
		# elif self.direction == -2:
		# 	self.x += (1 * self.speed * self.direction_factor)
		# elif self.direction == -1:
		# 	self.x -= (1 * self.speed * self.direction_factor)
		# elif self.direction == 1:
		# 	self.y += (1 * self.speed * self.direction_factor)
		# 	self.x += (1 * self.speed * self.direction_factor)
		# elif self.direction == 2:
		# 	self.y -= (1 * self.speed * self.direction_factor)
		# 	self.x -= (1 * self.speed * self.direction_factor)
		# elif self.direction == 3:
		# 	self.x += (1 * self.speed * self.direction_factor)
		# 	self.y -= (1 * self.speed * self.direction_factor)
		# elif self.direction == 4:
		# 	self.x -= (1 * self.speed * self.direction_factor)
		# 	self.y += (1 * self.speed * self.direction_factor)
		# self.rect.x = self.x 
		# self.rect.y = self.y 
		