
import sys, re

input = sys.stdin.readline()
input = re.findall('-?\d+', input)

number = int(input[0])
number = hex(number)[:1:-1] #returns '0xnumber' --> reverse and slice 0x 

print(number.upper())
	