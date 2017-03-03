class Settings():
	"""A class to store all settings for Blue Sky"""

	def __init__(self):
		"""Initialize the game's settings."""
		
		# Ship settings
		self.ship_speed_factor = 10

		# Screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (255, 255, 255)

				# Bullet settings
		self.bullet_speed_factor = 1
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = 60, 60, 60
		self.bullets_allowed = 3

		# Hot dog settings
		self.hot_dog_direction_factor = 1
		self.hot_dog_speed_factor = .5