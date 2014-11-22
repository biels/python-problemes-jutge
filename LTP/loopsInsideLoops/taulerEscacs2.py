
import sys, re

numbers = sys.stdin.readline()
numbers = re.findall('\d+', numbers)

rows = int(numbers[0])
cols = int(numbers[0]) #not used

total = 0
for i in range(rows):
    row = sys.stdin.readline()
    row = re.findall('\d', row)

    #even: start at col 0 . odd: start at col 1
    start = i % 2
    for j in range(start, len(row), 2):
        total += int(row[j])

print(total)
