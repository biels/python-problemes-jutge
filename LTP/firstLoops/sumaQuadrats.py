
import sys, re

number = sys.stdin.readline()
number = re.findall('-?\d+', number)

number = int(number[0])

result = 0

for num in range(1, number+1):
	result += num*num

print(result)
	