#######################
# Failed attempt at part 2
########################

from guard import Guard

with open('input.txt', 'r') as file:
    lines = file.readlines()
    
with open('sample.txt', 'r') as file:
     lines = file.readlines()

basemap = []
for line in lines:
    basemap.append(list(line.strip()))

spotmap = []
for line in lines:
	spotmap.append(list(line.strip()))

original = []
for line in lines:
	original.append(list(line.strip()))

g = Guard()
g.width = len(lines[0].strip())
g.height = len(lines)
    
# The guard is represented by the ^ character, find it's position in the array
for y, row in enumerate(basemap):
	for x, cell in enumerate(row):
		if cell == "^":
			g.start_x = x
			g.start_y = y
			break

g.move_to_start()

# Loop until the guard is out of bounds
while not g.isOutOfBounds():
	if g.isLookAheadOutOfBounds():
		spotmap[g.y][g.x] = "X"
		g.move()
		continue
	
	x, y = g.lookAhead()
	if spotmap[y][x] == "#":
		g.turnRight()
		continue

	spotmap[g.y][g.x] = "X"
	g.move()

# Find all X,Y locations in spotmap that have an X in them
spots = []
# for y, row in enumerate(spotmap):
# 	for x, cell in enumerate(row):
# 		if cell == "X":
# 			spots.append((x, y))

# # Remove the spot that matches the guards start_x and start_y
# spots = [spot for spot in spots if spot != (g.start_x, g.start_y)]

for y in range(g.height):
	for x in range(g.width):
		spots.append((x, y))

#print (spots)
# print (len(spots))

loopGenerators = 0

for spot in spots:
	# print("Spot", spot)
	# Copy original map to basemap
	for y, row in enumerate(original):
		for x, cell in enumerate(row):
			basemap[y][x] = cell

	basemap[spot[1]][spot[0]] = "#"		# Place a wall at the spot

	g.move_to_start()	# Move the guard back to the start
	while not g.isOutOfBounds():         # Loop until the guard is out of bounds
		if g.isLookAheadOutOfBounds():
			basemap[g.y][g.x] = str(g.direction)
			g.move()
			break
		
		x, y = g.lookAhead()
		if basemap[y][x] == "#":
			g.turnRight()
			continue

		if basemap[y][x] == ".":
			# print("Not Seen", x, y)
			basemap[g.y][g.x] = str(g.direction)
		elif basemap[y][x] != str(g.direction):
			# print("Seen but not from this angle", x, y)
			basemap[g.y][g.x] = str(g.direction)
		else:
			print("Seen at this angle", x, y)
			loopGenerators += 1			# Found a loop generator
			break					    # Break out of the while loop
		g.move()

print(loopGenerators)
	
# # Write the final map to a file sample_solve.txt
# with open('sample_part_02_spotmap.txt', 'w') as file:
# 	for row in spotmap:
# 		file.write("".join(row) + "\n")

# print(basemap[0][0])

# print(spots)

# for y, row in enumerate(basemap):
# 	print("".join(row))
# print(basemap)