
import sys, re

input = sys.stdin.readline()
input = re.findall('-?\d+', input)

number = int(input[0])
number = bin(number)[:1:-1] #returns '0bnumber' --> reverse and slice 0b 

print(number)
	