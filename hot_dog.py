import pygame
from pygame.sprite import Sprite
import random


class Hotdog(pygame.sprite.Sprite):
	"""A class to represent a single hot dog in the fleet."""

	def __init__(self, bs_settings, screen):
		"""Initialize the hot dog and set its starting position."""
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.bs_settings = bs_settings

		# Load the hot dog image and set its rect attribute.
		self.image = pygame.image.load('images/hot_dog.bmp')
		self.rect = self.image.get_rect()

		# Start each new hot dog near the top left of the screen. 
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height

		# Store the hot dog's exact position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

		# Store and randomize the hot dog's direction.
		self.hot_dog_direction_factor = 1
		numbers =  [x for x in range(-4, 4) if x != 0]
		self.direction = random.choice(numbers)
		print(self.direction)

	def blitme(self):
		"""Draw the hot dog at its current location."""
		self.screen.blit(self.image, self.rect)

	def check_edges(self):
		"""Return True if hot dog is at edge of screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right:
			return True
		elif self.rect.left <= 0:
			return True
		elif self.rect.top <= 0:
			return True
		elif self.rect.bottom >= screen_rect.bottom:
			return True


	def update(self):
		"""Move the hot dog."""
		self.speed = self.bs_settings.hot_dog_speed_factor 
		self.direction_factor = self.hot_dog_direction_factor
		
		if self.direction == -4:
			self.y += (1 * self.speed * self.direction_factor) 
		elif self.direction == -3:
			self.y -= (1 * self.speed * self.direction_factor)
		elif self.direction == -2:
			self.x += (1 * self.speed * self.direction_factor)
		elif self.direction == -1:
			self.x -= (1 * self.speed * self.direction_factor)
		elif self.direction == 1:
			self.y += (1 * self.speed * self.direction_factor)
			self.x += (1 * self.speed * self.direction_factor)
		elif self.direction == 2:
			self.y -= (1 * self.speed * self.direction_factor)
			self.x -= (1 * self.speed * self.direction_factor)
		elif self.direction == 3:
			self.x += (1 * self.speed * self.direction_factor)
			self.y -= (1 * self.speed * self.direction_factor)
		elif self.direction == 4:
			self.x -= (1 * self.speed * self.direction_factor)
			self.y += (1 * self.speed * self.direction_factor)
		self.rect.x = self.x 
		self.rect.y = self.y 
		

	def kill_offscreen(self):
		"""Kill hot dogs that wander off screen."""
		screen_rect = self.screen.get_rect()
		if self.rect.left >= screen_rect.right:
			return True
		elif self.rect.right <= 0:
			return True
		elif self.rect.bottom <= 0:
			return True
		elif self.rect.top >= screen_rect.bottom:
			return True