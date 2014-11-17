
import sys, re

words =  sys.stdin.readline()
words = re.findall('\w+', words)

comp = ' = '
if(words[0] > words[1]): 
	comp = ' > '
elif(words[0] < words[1]):
	comp = ' < '

print(words[0] + comp + wordss[1])