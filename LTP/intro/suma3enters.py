
import sys

input =  sys.stdin.readline()
# the line is a string ex: '1 2 3'
input = input.split(' ')
#parse to int
numbers = map(int, input)

print sum(numbers)