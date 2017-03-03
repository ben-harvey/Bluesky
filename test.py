from random import randint
def update():
	"""Move the hot dog."""
	# self.speed = self.bs_settings.hot_dog_speed_factor 
	direction_list = [randint(1,4)]
	direction_tuple = tuple(direction_list)
	print(direction_tuple)
	# if 1 in direction_tuple:
	# 	self.y += 1
	# elif 2 in direction_tuple:
	# 	self.y -= 1
	# elif 3 in direction_tuple:
	# 	self.x += 1
	# elif 4 in direction_tuple:
	# 	self.x -= 1	
	# self.rect.y = self.y
	# self.rect.y = self.y

update()
update()