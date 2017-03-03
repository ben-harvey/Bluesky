import pygame
from pygame.sprite import Sprite
from random import randint


class Hotdog(Sprite):
	"""A class to represent a single hot dog in the fleet."""

	def __init__(self, bs_settings, screen):
		"""Initialize the hot dog and set its starting position."""
		super().__init__()
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

		# Randomize the hot dog's direction.
		self.direction = [randint(1,4)]

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
		# self.direction.append(randint(1,4))
		
		if 1 in self.direction:
			self.y += 1 
		elif 2 in self.direction:
			self.y -= 1
		elif 3 in self.direction:
			self.x += 1
		elif 4 in self.direction:
			self.x -= 1	
		self.rect.x = self.x * self.bs_settings.hot_dog_speed_factor
		self.rect.y = self.y *  self.bs_settings.hot_dog_speed_factor
		print(self.direction)
		# self.x += randint(-1,   1) * self.speed
		
		
		# self.y += randint(-1, 1) * self.speed
							
		# self.rect.x = self.x
		# self.rect.y = self.y