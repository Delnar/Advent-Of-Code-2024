# Read the file input.txt
with open('input.txt', 'r') as file:
    lines = file.readlines()

# Initialize lists to store columns
leftColumn = []
rightColumn = []

# Process each line
for line in lines:
    parts = line.split()
    leftColumn.append(parts[0])
    rightColumn.append(parts[1])    
    # # Split the line by spaces and convert to numbers
    # numbers = list(map(float, line.split()))
    
    # # Add numbers to corresponding columns
    # for i, number in enumerate(numbers):
    #     if len(columns) <= i:
    #         columns.append([])
    #     columns[i].append(number)
    
#  Sort the left column
leftColumn.sort()
#  Sort the right column
rightColumn.sort()

diff = 0
for i, number in enumerate(leftColumn):
    # Count the number of times number is found in the right column array
    count = rightColumn.count(number)
    diff += float(number) * float(count)
	

print (diff)
