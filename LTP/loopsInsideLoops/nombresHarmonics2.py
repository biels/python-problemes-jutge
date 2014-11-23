
import sys, re

def harmonic (number):
	result = 0
	for i in range(1, number + 1):
		result += float(1/i)
	return result


line = 1
while line:
	line = sys.stdin.readline()

	numbers = re.findall('\d+', line)
	first = int(numbers[0])
	second = int(numbers[1])

	result = harmonic(first) - harmonic(second)
	print('%.10f' %result)





	
