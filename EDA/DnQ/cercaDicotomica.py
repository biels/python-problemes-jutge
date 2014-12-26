
#v.index(x)
def posicio (x, v, esq, dre) :
	print(x, v, esq, dre)
	if esq >= dre - 1 :
		if v[esq] == x :
			return esq
		else :
			return -1
	else :
		mid = int((esq + dre) / 2)
		if v[mid] > x :
			return posicio(x, v, esq, mid)
		else :
			return posicio(x, v, mid, dre)

