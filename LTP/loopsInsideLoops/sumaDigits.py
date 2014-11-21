
import sys, re

line = 1
while line:
		line = sys.stdin.readline()
		digits = re.findall('\d', line)

		number = str(''.join(digits))
		digits = list(map(int, number))
		digitSum = sum(digits)

		print('La suma de digits de {} es {}.'.format(number, digitSum))
