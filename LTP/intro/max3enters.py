
import sys, re

numbers = sys.stdin.readline()
numbers = re.findall('-?\d+', numbers)

numbers = list(map(int, numbers))

print(max(numbers))



