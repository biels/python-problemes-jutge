
def suma_digits (n):

	if n < 10:
		return n
	else:
		return (n % 10) + suma_digits(int(n / 10)) 

def reduccio_digits (x):
	
	if x < 10:
		return x
	else:
		return reduccio_digits(suma_digits(x))

print(reduccio_digits(33))
print(reduccio_digits(5699))
print(reduccio_digits(0))




	
