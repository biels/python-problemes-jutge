
import sys, re

input = sys.stdin.readline()
input = re.findall('-?\d+', input)

numbers = list(map(int, input))

mx = max(numbers)
mn = min(numbers) - 1 

for num in range(mx, mn, -1):
	print(num)
