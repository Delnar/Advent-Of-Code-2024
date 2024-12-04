from node import Node

class NodeCollection:
	def __init__(self, lines):
		self.nodes = []
		self.w = 0
		self.h = 0
		for y, line in enumerate(lines):
			for x, character in enumerate(line):
				if character != ' ' and character != '\n':
					self.add_node(character, x, y)
		self.w = max([node.x for node in self.nodes]) + 1  # +1 because we start at 0
		self.h = max([node.y for node in self.nodes]) + 1  # +1 because we start at 0

	def print(self):
		for node in self.nodes:
			print(node)
		print (f"Total nodes: {len(self.nodes)}")

	def add_node(self, character, x, y):
		node = Node(character, x, y)
		self.nodes.append(node)	
	
	def __iter__(self):
		return iter(self.nodes)
	
	def __len__(self):
		return len(self.nodes)
	
	def compWord(self, word, x, y, dx, dy):
		wlen = len(word)				# get the length of the word
		w = self.getWord(wlen, x, y, dx, dy)	# get the word at the x,y position
		# print(f"Word: {w}")
		if w == word:					# if the word matches the word to lookup
			return True					# return true
		return False					# return false

	def getXWord(self, x, y):
		line1 = self.getWord(3, x-1, y-1, 1, 0)	# Get the Down Right word
		line2 = self.getWord(3, x-1, y,   1, 0)	# Get the Down Right word
		line3 = self.getWord(3, x-1, y+1, 1, 0)	# Get the Down Right word

		if line1 == "" or line2 == "" or line3 == "":
			return None

		# replace the second character with a . in line1
		line1 = line1[:1] + "." + line1[2:]
		# replace the first character and last character with a . in line2
		line2 = "." + line2[1] + "."
		# replace the second character with a . in line3
		line3 = line3[:1] + "." + line3[2:]

		ret = []
		ret.append(line1)
		ret.append(line2)
		ret.append(line3)
		return ret

	def printXWord(self, x, y):
		p = self.getXWord(x, y)
		if p is None:
			return
		
		print("---")
		print(f"{p[0]}")
		print(f"{p[1]}")
		print(f"{p[2]}")
		print("---")
		print("")
		

	def compXMASWord(self, x, y):
		p = self.getXWord(x, y)
		if p is None:
			return False

		if p[0] == "M.S" and p[2] == "M.S":
			return True
		
		if p[0] == "S.M" and p[2] == "S.M":
			return True

		if p[0] == "S.S" and p[2] == "M.M":
			return True

		if p[0] == "M.M" and p[2] == "S.S":
			return True

		return False

	def getWord(self, wlen, x, y, dx, dy, ox=0, oy=0):
		word = ""						# word to construct
		for i in range(wlen):			# for each character in the word to lookup			
			node = self.getNode(x+ox, y+oy)	# get the node at the current x,y position
			
			if node is None:			# if the node is None, return word (out of bounds)
				return word
			word += node.character	    # add the character to the word
			x += dx						# move to the next x,y position 
			y += dy						
		return word						# return the word

	def getNode(self, x, y):
		# print(f"Getting node at {x}, {y} [0,0, {self.w}, {self.h}]")
		if x < 0 or x >= self.w:
			return None
		if y < 0 or y >= self.h:
			return None
		
		for node in self.nodes:
			if node.x == x and node.y == y:
				return node
		return None