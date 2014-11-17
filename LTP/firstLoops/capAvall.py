
import sys, re

numbers = sys.stdin.readline()
numbers = re.findall('-?\d+', numbers)

numbers = list(map(int, numbers))

mx = max(numbers)
mn = min(numbers) - 1 

for num in range(mx, mn, -1):
	print(num)
