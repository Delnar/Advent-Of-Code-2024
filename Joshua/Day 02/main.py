with open('input.txt', 'r') as file:
    lines = file.readlines()

def GetMaxIncrease(numbers):
	maxIncrease = 0
	for i in range(0, len(numbers)):
		if i == len(numbers) - 1:
			continue
		if numbers[i] < numbers[i+1]:
			increase = numbers[i+1] - numbers[i]
			maxIncrease = increase if increase > maxIncrease else maxIncrease		
	return maxIncrease

def GetMaxDecrease(numbers):
	maxDecrease = 0
	for i in range(0, len(numbers)):
		if i == len(numbers) - 1:
			continue
		if numbers[i] > numbers[i+1]:
			decrease = numbers[i] - numbers[i+1]
			maxDecrease = decrease if decrease > maxDecrease else maxDecrease		
	return maxDecrease

def GetEqualCount(numbers):
	equalCount = 0
	for i in range(0, len(numbers)):
		if i == len(numbers) - 1:
			continue
		if numbers[i] == numbers[i+1]:
			equalCount += 1
	return equalCount

def getNumberArrayFromLine(line):
	return list(map(int, line.split()))

def isSafe(numbers):
	# If there are any equal numbers, then it is not safe
	if GetEqualCount(numbers) > 0:
		return False
	
	MaxIncrease = GetMaxIncrease(numbers)
	MaxDecrease = GetMaxDecrease(numbers)

	# If there is a max increase and a max decrease, then it is not safe
	if MaxIncrease != 0 and MaxDecrease != 0:
		return False

	# If the max increase or max decrease is less than 1, then it is not safe
	maxValue = max(MaxIncrease, MaxDecrease)
	if maxValue < 1:
		return False
		
	# If the max increase or max decrease is greater than 3, then it is not safe
	if maxValue > 3:
		return False	
	
	return True

def isSafeLine(line):
	numbers = getNumberArrayFromLine(line)
	return isSafe(numbers)

safeCount = 0
for line in lines:
	if isSafeLine(line):
		safeCount += 1

print(safeCount)