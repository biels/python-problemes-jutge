
import sys, re

input = sys.stdin.readline()
input = re.findall('-?\d+', input)

number = int(input[0])

for num in range(number):
	sys.stdout.write(str(num**3) + ',')

sys.stdout.write(str(number**3) + '\n')
	