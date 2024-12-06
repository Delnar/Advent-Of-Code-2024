class Guard:
	def __init__(self):
		self.x = 0
		self.y = 0
		self.width = 0
		self.height = 0
		self.direction = 0
		self.start_x = 0
		self.start_y = 0

	# 0 = up, 1 = right, 2 = down, 3 = left
	def lookAhead(self):
		if self.direction == 0:
			return self.x, self.y - 1
		elif self.direction == 1:
			return self.x + 1, self.y
		elif self.direction == 2:
			return self.x, self.y + 1
		elif self.direction == 3:
			return self.x - 1, self.y

	def isOutOfBounds(self):
		if self.x < 0 or self.x >= self.width:
			return True
		if self.y < 0 or self.y >= self.height:
			return True
		return False
	
	def isLookAheadOutOfBounds(self):
		x, y = self.lookAhead()
		if x < 0 or x >= self.width:
			return True
		if y < 0 or y >= self.height:
			return True
		return False
	
	def move(self):
		self.x, self.y = self.lookAhead()

	def move_to_start(self):
		self.x = self.start_x
		self.y = self.start_y

	def turnRight(self):
		self.direction = abs((self.direction + 1) % 4)

	def turnLeft(self):
		self.direction = abs((self.direction - 1) % 4)

