
def mcd (a ,b):

	x = max(a, b)
	y = min(a, b)

	if y == 0:
		return x
	else:
		return mcd(y, x % y)


print(mcd(66, 12))
print(mcd(100, 21))
print(mcd(0, 10))





	
