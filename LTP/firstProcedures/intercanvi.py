
def swap2 (a, b):
	
	aux = a;
	a = b;
	b = aux;

	return a, b;

print(swap2(1, 2))