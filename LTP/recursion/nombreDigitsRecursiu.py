
import sys, re

#functions
def nombre_digits (n):

	if (n / 10) >= 1:
		return 1 + nombre_digits(n / 10)
	else:
		return 1


#
line = 1
while line:
	
	line = sys.stdin.readline()
	number = re.findall('\d+', line)
	number = int(number[0])
	print(nombre_digits(number))


	
