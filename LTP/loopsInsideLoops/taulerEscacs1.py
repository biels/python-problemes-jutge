
import sys, re

numbers = sys.stdin.readline()
numbers = re.findall('\d+', numbers)

rows = int(numbers[0])
cols = int(numbers[0]) #not used

totalSum = 0
for i in range(rows):
    row = sys.stdin.readline()
    row = re.findall('\d', row)
    row = list(map(int, row))
    totalSum += sum(row)

print(totalSum)
