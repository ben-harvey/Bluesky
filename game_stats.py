class GameStats():
	"""Track statistics for game."""

	def __init__(self, bs_settings):
		"""Initialize statistics."""
		self.bs_settings = bs_settings
		self.reset_stats()
		
		# Start AI in an active state.
		self.game_active = False

	def reset_stats(self):
		"""Initialize stats that can change during the game."""
		self.ships_left = self.bs_settings.ship_limit