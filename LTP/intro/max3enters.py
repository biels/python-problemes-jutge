
import sys, re

input = sys.stdin.readline()
input = re.findall('-?\d+', input)

numbers = map(int, input)

print(max(numbers))



