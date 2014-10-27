
import sys, re

# the line is a string; ex: '1 2 3'
input = sys.stdin.readline()
# string to digit array; ex:['1', '2', '3']
input = re.findall('-?\d+', input)
#parse to int
numbers = map(int, input)

print sum(numbers)
