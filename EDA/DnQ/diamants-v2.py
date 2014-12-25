
import sys, re

#Functions
def canMarry (dValue, values) :

	if values == [] :
		print('single')
		return

	currentValue = values[0] + values[-1]

	if currentValue == dValue :
		print('married')
		return
	else :
		if currentValue > dValue :
 			values = values[:-1]
		else :
			values = values[1:]
		canMarry(dValue, values)

#
line = sys.stdin.readline()

while line != '0 0\n' :

	diamondValue = int(re.findall('\d+', line)[0])

	values = sys.stdin.readline()
	values = re.findall('\d+', values)
	values = list(map(int, values))
	values.sort()

	canMarry(diamondValue, values)
	
	line = sys.stdin.readline()

