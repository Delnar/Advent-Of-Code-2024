import re

# Read the file input.txt
with open('input.txt', 'r') as file:
    content = file.read()

lookupExpression = r"mul\(\d+,\d+\)"

# Find all matches
matches = re.findall(lookupExpression, content)

# Count the number of matches
count = len(matches)

sumTotal = 0

for match in matches:
    # Extract the numbers from the match
	numbers = re.findall(r"\d+", match)
	# Multiply the numbers
	result = int(numbers[0]) * int(numbers[1])
	sumTotal += result
	print(f"{match} = {result}")	

print(f"The sum of all the expressions is {sumTotal}.")
print(f"The expression '{lookupExpression}' was found {count} times.")