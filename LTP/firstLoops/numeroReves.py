
import sys, re

input = sys.stdin.readline()
input = re.findall('-?\d+', input)

#slice --> http://stackoverflow.com/questions/509211/explain-pythons-slice-notation
number = input[0][::-1]

print(number)
	