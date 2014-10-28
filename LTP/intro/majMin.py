
import sys

letter = sys.stdin.readline()

'''
if letter.islower():
	letter = letter.upper()
else:
	letter = letter.lower()
'''

letter = letter.upper() if(letter.islower()) else letter.lower() 

# print(letter) ads new line
sys.stdout.write(letter)