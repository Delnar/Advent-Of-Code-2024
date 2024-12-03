import re

# Read the file input.txt
with open('input.txt', 'r') as file:
    content = file.read()

lookupExpression = r"mul\(\d+,\d+\)"
lookupDoExpression = r"do\(\)"
lookupDonotExpression = r"don't\(\)"

# Find all matches
matches = list(re.finditer(lookupExpression, content))
domatches = list(re.finditer(lookupDoExpression, content))
donotmatches = list(re.finditer(lookupDonotExpression, content))

# Merge these three list together
matches += domatches
matches += donotmatches

# Sort the matches by their starting position
matches.sort(key=lambda x: x.start())

# Count the number of matches
count = len(matches)

doFlag = True
sumTotal = 0

for match in matches:
	text = match.group()
	if "do()" in text:
		doFlag = True
		print(f"do() at position {match.start()}")
		continue
	elif "don't()" in text:
		doFlag = False
		print(f"don't() at position {match.start()}")
		continue

	if not doFlag:
		print(f"{match.group()} skipped at position {match.start()}")
		continue

    # Extract the numbers from the match
	numbers = re.findall(r"\d+", text)
    # Multiply the numbers
	result = int(numbers[0]) * int(numbers[1])
	sumTotal += result
	print(f"{match.group()} = {result}, starts at position {match.start()}")

print(f"The sum of all the expressions is {sumTotal}.")
print(f"The expression '{lookupExpression}' was found {count} times.")