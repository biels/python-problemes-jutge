
import sys, re
from math import sqrt

line = 1
while line:
	
	line = sys.stdin.readline()
	number = re.findall('\d+', line)
	number = int(number[0])

	print('%.d %.6f' %( number * number, sqrt(number)))
