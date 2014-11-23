
import sys, re

line = 1
while line:
	line = sys.stdin.readline()

	number = re.findall('-?\d+', line)
	number = int(number[0])

	steps = 0
	while (number != 1):
		if(number % 2 == 0):
			number /= 2
		else:
			number = (number * 3) + 1
		steps += 1
	
	print(steps)
