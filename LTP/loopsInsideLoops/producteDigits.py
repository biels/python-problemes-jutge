
import sys, re
from functools import reduce

#functions
def digitsProduct(number):
	digits = list(map(int, str(number)))
	product = reduce(lambda x, y: x * y, digits)

	return product

#
line = 1
while line:
		line = sys.stdin.readline()
		number = re.findall('\d+', line)
		number = int(number[0])

		product = digitsProduct(number)
		while (product/10) > 1:
			print('El producte dels digits de {} es {}.'.format(number, product))
			number = product
			product = digitsProduct(product)
		
		print('El producte dels digits de {} es {}.'.format(number, product))
		print('----------')