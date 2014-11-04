import sys, re

input = sys.stdin.readline()
numAs = re.findall('a+', input)

print(len(numAs))