from guard import Guard

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
# with open('sample.txt', 'r') as file:
#      lines = file.readlines()

basemap = []
for line in lines:
    basemap.append(list(line.strip()))

g = Guard()
g.width = len(lines[0].strip())
g.height = len(lines)
    
# The guard is represented by the ^ character, find it's position in the array
for y, row in enumerate(basemap):
	for x, cell in enumerate(row):
		if cell == "^":
			g.x = x
			g.y = y
			break

moveNum = 0

while not g.isOutOfBounds():
	if g.isLookAheadOutOfBounds():
		basemap[g.y][g.x] = "X"
		g.move()
		print(f"[{moveNum}] OUT {g.x}, {g.y}")		
		moveNum += 1
		continue
	
	x, y = g.lookAhead()
	if basemap[y][x] == "#":
		print(f"[{moveNum}] turn")
		moveNum += 1
		g.turnRight()
		continue
	basemap[g.y][g.x] = "X"
	print(f"[{moveNum}] {g.x}, {g.y}")
	g.move()
	moveNum += 1

# Count the # of X's in the map
spots = 0
for row in basemap:
	for cell in row:
		if cell == "X":
			spots += 1

# Print the number of spots
print(spots)
	
# Write the final map to a file sample_solve.txt
with open('sample_solve.txt', 'w') as file:
	for row in basemap:
		file.write("".join(row) + "\n")

# print(basemap[0][0])

# print(spots)

# for y, row in enumerate(basemap):
# 	print("".join(row))
# print(basemap)