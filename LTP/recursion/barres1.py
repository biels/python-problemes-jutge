
import sys, re

def barres (n) :
	if n > 1 :
		barres(n - 1)
	print(n * '*')
	if n > 1 :
		barres(n - 1)

#
number = sys.stdin.readline()
number = int(re.findall('\d+', number)[0])
barres(number)