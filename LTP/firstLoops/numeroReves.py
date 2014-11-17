
import sys, re

number = sys.stdin.readline()
number = re.findall('-?\d+', number)

#slice --> http://stackoverflow.com/questions/509211/explain-pythons-slice-notation
number = number[0][::-1]

print(number)
	