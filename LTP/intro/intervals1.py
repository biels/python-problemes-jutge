
import sys, re

input =  sys.stdin.readline()
# find the numbers
input = re.findall('-?\d+', input)
#parse to int
numbers = map(int, input)

result = []

first = max(numbers[0], numbers[2])
second = min(numbers[1], numbers[3])

if(numbers[1] > numbers[2]):
	result = '[' + str(first) + ',' + str(second) + ']'

print result
