
import sys, re

number = sys.stdin.readline()
number = re.findall('\d+', number)
number = int(number[0])

#upper and mid
for i in range(number):
	whitespaces = ' ' * (number - i - 1)
	stars = '*' * (i * 2 + 1)
	print('%s%s'%(whitespaces, stars))

#lower
for j in range(number-1, 0, -1):
	whitespaces = ' ' * (number - j)
	stars = '*' * (j * 2 - 1)
	print('%s%s'%(whitespaces, stars))
