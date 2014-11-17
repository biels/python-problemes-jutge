
import sys, re

# the line is a string; ex: '1 
numbers = sys.stdin.readline()
# string to digit array; ex:['1', '2', '3']
numbers = re.findall('-?\d+', numbers)
#parse to int
numbers = list(map(int, numbers))

print(sum(numbers))
