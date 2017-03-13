from random import randint

class Settings():
	"""A class to store all settings for Blue Sky"""

	def __init__(self):
		"""Initialize the game's settings."""
		# Ship settings
		self.ship_limit = 3
		
		

		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		
		# How quickly the game speeds up
		self.speedup_scale = 1.1
		self.score_scale = 1.3

		self.initialize_dynamic_settings()

	def initialize_dynamic_settings(self):
		"""Initialize setting that change throughout the game."""
		# Ship settings
		self.ship_speed_factor = 3
		
		# Hot dog settings
		self.hot_dog_speed_factor = 1
		
		# Kimchi settings
		self.kimchi_speed_factor = 0.9
		self.kimchi_number = 1
		
		# Scoring
		self.hot_dog_points = 50
		

		# Background color
		self.bg_color = ()

		

	def increase_speed(self):
		"""Increase speed settings."""
		self.ship_speed_factor *= self.speedup_scale
		self.hot_dog_speed_factor *= self.speedup_scale
		self.kimchi_speed_factor *= self.speedup_scale

		self.hot_dog_points = int(self.hot_dog_points * self.score_scale)
		

	def random_bg(self):
		"""Define random background color."""
		self.r = randint(0, 255)
		self.g = randint(0, 255)
		self.b = randint(0, 255)
		self.bg_color = (self.r, self.g, self.b)
		self.bg_color = tuple(self.bg_color)