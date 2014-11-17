import sys, re

As = sys.stdin.readline()
numAs = re.findall('a+', As)

print(len(numAs))