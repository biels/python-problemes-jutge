

import sys, re

line = 1
while line:
		line = sys.stdin.readline()

		numbers = re.findall('-?\d+', line)
		numbers = list(map(int, numbers))

		base = numbers[0]
		exponent = numbers[1]

		print(base**exponent)
