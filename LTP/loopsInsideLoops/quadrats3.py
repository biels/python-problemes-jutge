
import sys, re

line = 1
number = 0
while line:

	line = sys.stdin.readline()
	line = re.findall('\d', line) #1 digit
	rows = int(line[0])
	
	for row in range(rows):
		for col in range(rows):
			sys.stdout.write(str(number))
			number += 1
			if number > 9:
				number = 0
		sys.stdout.write('\n')

	print()




	
