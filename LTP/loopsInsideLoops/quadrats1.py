
import sys, re

line = 1
while line:

	line = sys.stdin.readline()
	line = re.findall('\d', line) #1 digit
	rows = int(line[0])

	for row in range(rows):
		print(rows * str(rows))
	print()




	
