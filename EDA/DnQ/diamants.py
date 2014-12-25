
import sys, re

#Functions
def canMarry (dValue, values, start, end) :

	if start > end :
		print('single')
		return

	currentValue = values[start] + values[end]

	if currentValue == dValue :
		print('married')
		return
	else :
		if currentValue > dValue :
 			end -= 1
		else :
			start += 1
		canMarry(dValue, values, start, end)

#
line = sys.stdin.readline()

while line != '0 0\n' :

	diamondValue = int(re.findall('\d+', line)[0])

	values = sys.stdin.readline()
	values = re.findall('\d+', values)
	values = list(map(int, values))
	values.sort()

	canMarry(diamondValue, values, 0, len(values) - 1)
	
	line = sys.stdin.readline()



