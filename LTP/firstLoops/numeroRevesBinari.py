
import sys, re

number = sys.stdin.readline()
number = re.findall('-?\d+', number)

number = int(number[0])
number = bin(number)[:1:-1] #returns '0bnumber' --> reverse and slice 0b 

print(number)
	