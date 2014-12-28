
import sys, re

def barres (n) :
	if n <= 1 :
		print('*')
	else :
		barres(n - 1)
		barres(n - 1)
		print(n * '*')

#
number = sys.stdin.readline()
number = int(re.findall('\d+', number)[0])
barres(number)