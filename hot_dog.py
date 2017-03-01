import pygame
from pygame.sprite import Sprite

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

	def blitme(self):
		"""Draw the hot dog at its current location."""
		self.screen.blit(self.image, self.rect)