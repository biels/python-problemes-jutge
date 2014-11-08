
import sys, re

#read variable
input = sys.stdin.readline()
input = re.findall('-?\d*\.?\d+', input)
var = float(input[0])

#read coefficients
input = sys.stdin.readline()
input= re.findall('-?\d*\.?\d+', input)
coeffs = [float(each) for each in input]

numCoeffs = len(coeffs)
result = coeffs[0]

for i in range(1, numCoeffs):
	result += coeffs[i] * var**i

print("%.4f" %result) #precission 4'''
