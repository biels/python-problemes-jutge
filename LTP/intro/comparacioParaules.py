
import sys, re

input =  sys.stdin.readline()

input = re.findall('\w+', input)

comp = ' = '
if(input[0] > input[1]): 
	comp = ' > '
elif(input[0] < input[1]):
	comp = ' < '

print(input[0] + comp + input[1])