# Create a node class for the linked list

class Node:
	def __init__(self, character, x, y):
		self.character = character
		self.x = x
		self.y = y
		self.word_count = 0

	def __str__(self):
		return f"Node at ({self.x}, {self.y}) with character {self.character}"