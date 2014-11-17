
import sys, re

number = sys.stdin.readline()
number = re.findall('-?\d+', input)

number = int(number[0])
result = 0

for num in range(1, number + 1):
	result += 1/num

# precission 4
print("%.4f" % result)
