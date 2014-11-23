
import sys, re

#functions
def factorial(n):

	if n > 1:
		return n * factorial(n - 1)
	else:
		return 1


#
line = 1
while line:
	
	line = sys.stdin.readline()
	number = re.findall('\d+', line)
	number = int(number[0])
	print(factorial(number))


	
