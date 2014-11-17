
import sys, re

number = sys.stdin.readline()
number = re.findall('-?\d+', number)

number = int(number[0])

for num in range(number):
	sys.stdout.write(str(num**3) + ',')

sys.stdout.write(str(number**3) + '\n')
	