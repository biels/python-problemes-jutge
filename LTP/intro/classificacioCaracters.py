import sys

letter = sys.stdin.readline()[0]

print('minuscula') if(letter.islower()) else print('majuscula')
	
vowels = 'aeiouAEIOU'
print('vocal') if(letter in vowels) else print('consonant')	