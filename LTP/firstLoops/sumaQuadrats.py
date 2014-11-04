
import sys, re

input = sys.stdin.readline()
input = re.findall('-?\d+', input)

number = int(input[0])

result = 0

for num in range(1, number+1):
	result += num*num

print(result)
	