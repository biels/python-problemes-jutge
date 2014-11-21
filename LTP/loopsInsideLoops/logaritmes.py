
import sys, re
from math import log, floor

line = 1
while line:
		line = sys.stdin.readline()

		numbers = re.findall('-?\d+', line)
		numbers = list(map(int, numbers))

		base = numbers[0]
		number = numbers[1]

		exponent = floor(log(number, base))

		print(exponent)

'''
	precission error
	ex: log(1000, 10)
		shoud be 3 but the result is 2.9999999999999996			
'''
