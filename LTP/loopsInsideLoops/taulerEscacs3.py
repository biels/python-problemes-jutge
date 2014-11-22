
import sys, re

number = sys.stdin.readline()
number = re.findall('\d+', number)

rows = int(number[0])

total = 0
for i in range(rows):
    row = sys.stdin.readline()
    row = re.findall('\d', row)

    total += int(row[i]) #diagonal1
    total += int(row[rows - i - 1]) #diagonal2

print(total)
