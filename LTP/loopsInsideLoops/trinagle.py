
import sys, re

number = sys.stdin.readline()
number = re.findall('\d+', number)
number = int(number[0])

for i in range(number):
	print('*' * (i + 1))
