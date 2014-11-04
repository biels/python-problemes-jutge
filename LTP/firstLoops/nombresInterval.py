
import sys, re

input = sys.stdin.readline()
input = re.findall('-?\d+', input)

numbers = list(map(int, input))

if (numbers[0] <= numbers[1]):
	for num in range(numbers[0], numbers[1]):
		sys.stdout.write(str(num) + ',')
	sys.stdout.write(str(numbers[1]) + '\n')
