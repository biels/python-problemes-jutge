
def nombre_digits (n):

	if (n / 10) >= 1:
		return 1 + nombre_digits(n / 10)
	else:
		return 1




	
