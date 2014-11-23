
import sys, re
from math import radians, sin, cos

line = 1
while line:
	
	line = sys.stdin.readline()
	angle = re.findall('-?\d*\.?\d+', line)
	angle = int(angle[0])
	rads = radians(angle)

	print('%.6f %.6f' %(sin(rads), cos(rads)))