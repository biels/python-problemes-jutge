
import sys, re

numbers =  sys.stdin.readline()
# find the numbers
numbers = re.findall('-?\d+', numbers)
#parse to int
numbers = list(map(int, numbers))

result = []

first = max(numbers[0], numbers[2])
second = min(numbers[1], numbers[3])

if(numbers[1] >= numbers[2]):
	result = '[' + str(first) + ',' + str(second) + ']'

print(result)
