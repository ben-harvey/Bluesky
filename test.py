import random



numbers = [x for x in range(-4, 4) if x != 0]

direction = random.choice(numbers)
print(direction)