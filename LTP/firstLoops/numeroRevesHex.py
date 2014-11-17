
import sys, re

number = sys.stdin.readline()
number = re.findall('-?\d+', number)

number = int(number[0])
number = hex(number)[:1:-1] #returns '0xnumber' --> reverse and slice 0x 

print(number.upper())
	