
import sys, re

numbers = sys.stdin.readline()
numbers = re.findall('-?\d+', numbers)

numbers = list(map(int, numbers))

if (numbers[0] <= numbers[1]):
	for num in range(numbers[0], numbers[1]):
		sys.stdout.write(str(num) + ',')
	sys.stdout.write(str(numbers[1]) + '\n')
