

def es_creixent_rec (a):

	if len(a) == 1:
		return True
	else:
		currentdigit = a[0]
		a = a[1:] #remove 1st digit
		if(currentdigit > a[0]):
			return False
		else:
			return es_creixent_rec(a)	


def es_creixent (a):
	#int --> str
	return es_creixent_rec(str(a))


print(es_creixent(123378))
print(es_creixent(125433))  
print(es_creixent(7))






	
